from .models import Question, Staff, Student, Schedule, Questionnaire, Observation, Result
from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers, validators
from django.contrib.auth import get_user_model
from . import others


Profile = get_user_model()

# create serializers here
class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        exclude = ("user_permissions", "groups", "date_joined", "is_superuser", "is_active")
        extra_kwargs = {"password": {"write_only": True},}

    def create(self, validated_data):
        # pop the password field
        password = validated_data.pop("password")

        # create a new user
        profile = Profile.objects.create(**validated_data)
        profile.set_password(password)
        profile.save()
        return profile


class StaffSerializer(serializers.ModelSerializer):
    # nested relationship
    # profile = ProfileSerializer()

    class Meta:
        model = Staff
        fields = ("id", "staff_id", "level")
        extra_kwargs = {"profile": {"read_only": True},}

    def validate_staff_id(self, value):
        # Validate the staff id field
        if (len(value) == 7) and (value[:3].lower() == 'stf') and (value[3:].isnumeric()):
            try:
                Profile.objects.get(username__iexact=value)
            except Profile.DoesNotExist:
                return value.upper()
            else:
                raise serializers.ValidationError(_("Staff id belongs to a different staff. Please contact admin"))
        else:
            raise serializers.ValidationError(_("Incorrect staff id. HINT: STFxxxx"))

    def create(self, validated_data):
        # A new profile object has to be created first, because the staff model
        # has a one-to-one relationship to the Profile (user) model which is used
        # for the django auth backend.

        # create new profile
        profile = Profile.objects.create(username=validated_data.get('staff_id'))
        profile.set_password('p@ssw0rd')
        profile.is_staff = True
        profile.save()

        # after successful creation of the corresponding profile, then
        # create the staff instance passing the newly created profile instance
        # as the profile field
        staff = Staff.objects.create(profile=profile, **validated_data)
        return staff

    def update(self, instance, validated_data):
        # update the staff fields and save
        instance.staff_id = validated_data.get("staff_id", instance.staff_id)
        instance.level = validated_data.get("level", instance.level)
        instance.save()
        return instance


class StudentSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer()

    class Meta:
        model = Student
        fields = ("id", "sid", "reg_no", "level", "department", "parent", "profile")
        validators = [
            validators.UniqueTogetherValidator(
                queryset=Student.objects.all(),
                fields=["reg_no", "level", "department"],
                message=_("Student with this Reg no, level and department already exists.")
            ),
        ]

    def validate_reg_no(self, value):
        # Validate the student reg number id field
        if (len(value) == 4) and (value.isnumeric()):
            return value
        else:
            raise serializers.ValidationError(_("Incorrect registration number!"))

    def create(self, validated_data):
        # A new profile object has to be created first, because the student model
        # has a one-to-one relationship to the Profile (user) model which houses
        # the default django auth backend. Get the profile data and password
        username = F"{validated_data.get('department')}/{validated_data.get('level')}/{validated_data.get('reg_no')}"
        profile = Profile.objects.create(username=username)
        profile.set_password('p@ssw0rd')
        profile.is_staff = False
        profile.save()

        # after successful creation of the corresponding profile, i then
        # create the student instance passing the newly created profile instance
        # as the profile field
        student = Student.objects.create(profile=profile, **validated_data)
        return student

    def update(self, instance, validated_data):    
        instance.reg_no = validated_data.get("reg_no", instance.reg_no)
        instance.level = validated_data.get("level", instance.level)
        instance.department = validated_data.get("department", instance.department)
        instance.parent = validated_data.get("parent", instance.parent)
        instance.save()
        return instance


class ScheduleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Schedule
        fields = ("id", "staff", "title", "slug", "detail", "created", "expire", "completed")
        extra_kwargs = {"staff": {"read_only": True},}


class QuestionnaireSerializer(serializers.ModelSerializer):
    students = serializers.SlugRelatedField(queryset=Student.objects.all(), many=True, slug_field="sid")

    class Meta:
        model = Questionnaire
        fields = ("id", "staff", "students", "categories", "created", "title", "slug", "question", "completed")
        extra_kwargs = {"staff": {"read_only": True},}


class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Question
        fields = ("id", "title", "slug", "question", "created")


class ObservationSerializer(serializers.ModelSerializer):
    student = serializers.SlugRelatedField(queryset=Student.objects.all(), slug_field="sid")
    staff_id = serializers.PrimaryKeyRelatedField(read_only=True)

    class Meta:
        model = Observation
        fields = ("id", "staff", "staff_id", "student", "detail", "created")
        extra_kwargs = {"staff": {"read_only": True},}


class ResultSerializer(serializers.ModelSerializer):
    student = serializers.SlugRelatedField(queryset=Student.objects.all(), slug_field="sid")

    class Meta:
        model = Result
        fields = "__all__"
