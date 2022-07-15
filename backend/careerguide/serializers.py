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
    profile = ProfileSerializer(required=False)

    class Meta:
        model = Staff
        fields = ("id", "staff_id", "level" , "profile")

    def validate_staff_id(self, value):
        # Validate the staff id field
        if (len(value) == 7) and (value[:3].lower() == 'stf') and (value[3:].isnumeric()):
            try:
                Profile.objects.get(username__iexact=value)
            except Profile.DoesNotExist:
                return value.lower()
            else:
                raise serializers.ValidationError(_("Staff id belongs to a different staff. Please contact admin"))
        else:
            raise serializers.ValidationError(_("Incorrect staff id. HINT: STFxxxx"))

    def create(self, validated_data):
        # A new profile object has to be created first, because the staff model
        # has a one-to-one relationship to the Profile model which is used
        # for the django auth backend.
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
        # get the instance corresponding profile
        try:
            profile_data = validated_data.pop("profile")
        except KeyError:
            profile_data = {}
        finally:
            profile = instance.profile
            
            # update the staff fields and save
            instance.staff_id = validated_data.get("staff_id", instance.staff_id)
            instance.level = validated_data.get("level", instance.level)
            instance.save()

            # update the profile fields
            profile.username = validated_data.get("staff_id", instance.staff_id)
            profile.first_name = profile_data.get("first_name", profile.first_name)
            profile.other_name = profile_data.get("other_name", profile.other_name)
            profile.last_name = profile_data.get("last_name", profile.last_name)
            profile.dob = profile_data.get("dob", profile.dob)
            profile.gender = profile_data.get("gender", profile.gender)
            profile.image = profile_data.get("image", profile.image)
            profile.about = profile_data.get("about", profile.about)
            profile.email = profile_data.get("email", profile.email)
            profile.phone_1 = profile_data.get("phone_1", profile.phone_1)
            profile.phone_2 = profile_data.get("phone_2", profile.phone_2)
            profile.country = profile_data.get("country", profile.country)
            profile.state = profile_data.get("state", profile.state)
            profile.postal = profile_data.get("postal", profile.postal)
            profile.save()

            return instance


class StudentSerializer(serializers.ModelSerializer):
    profile = ProfileSerializer(required=False)

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
            try:
                Profile.objects.get(username__iexact=value)
            except Profile.DoesNotExist:
                return value.lower()
            else:
                raise serializers.ValidationError(_("Reg number belongs to a different student. Please contact admin"))
        else:
            raise serializers.ValidationError(_("Incorrect registration number!"))

    def create(self, validated_data):
        # A new profile object has to be created first, because the student model
        # has a one-to-one relationship to the Profile model which houses
        # the default django auth backend.
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
        # get the profile of the corresponding student instance
        try:
            profile_data = validated_data.pop("profile")
        except KeyError:
            profile_data = {}
        finally:
            profile = instance.profile

            instance.reg_no = validated_data.get("reg_no", instance.reg_no)
            instance.level = validated_data.get("level", instance.level)
            instance.department = validated_data.get("department", instance.department)
            instance.parent = validated_data.get("parent", instance.parent)
            instance.save()

            profile.username = instance.sid
            profile.first_name = profile_data.get("first_name", profile.first_name)
            profile.other_name = profile_data.get("other_name", profile.other_name)
            profile.last_name = profile_data.get("last_name", profile.last_name)
            profile.dob = profile_data.get("dob", profile.dob)
            profile.gender = profile_data.get("gender", profile.gender)
            profile.image = profile_data.get("image", profile.image)
            profile.about = profile_data.get("about", profile.about)
            profile.email = profile_data.get("email", profile.email)
            profile.phone_1 = profile_data.get("phone_1", profile.phone_1)
            profile.phone_2 = profile_data.get("phone_2", profile.phone_2)
            profile.country = profile_data.get("country", profile.country)
            profile.state = profile_data.get("state", profile.state)
            profile.postal = profile_data.get("postal", profile.postal)
            profile.save()

            return instance


class ScheduleSerializer(serializers.ModelSerializer):
    staff = serializers.SlugRelatedField(read_only=True, slug_field="staff_id")

    class Meta:
        model = Schedule
        fields = ("id", "staff", "title", "slug", "detail", "created", "expire", "completed")
        extra_kwargs = {
            "title": {"required": True},
            "detail": {"required": True},
        }


class QuestionnaireSerializer(serializers.ModelSerializer):
    valid_data = (
        ('male', 'male'),
        ('female', 'female'),
        ('jss1', 'jss1'),
        ('jss2', 'jss2'),
        ('jss3', 'jss3'),
        ('sss1', 'sss1'),
        ('sss2', 'sss2'),
        ('sss3', 'sss3'),
        ('art', 'art'),
        ('science', 'science'),
        ('commercial', 'commercial'),
        ('social_science', 'social_science'),
    )
    staff = serializers.SlugRelatedField(read_only=True, slug_field="staff_id")
    students = serializers.SlugRelatedField(queryset=Student.objects.all(), many=True, slug_field="sid", required=False)
    categories = serializers.ListField(child=serializers.ChoiceField(choices=valid_data, allow_blank=True), required=False)

    class Meta:
        model = Questionnaire
        fields = ("id", "staff", "students", "categories", "created", "title", "slug", "question", "completed")

    def to_internal_value(self, data):
        if data.get('categories'):
            # remove duplicate choices from the categories field
            data['categories'] = list(set(data['categories']))
        return super().to_internal_value(data)


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
