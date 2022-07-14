from .serializers import (
    ProfileSerializer, StaffSerializer, StudentSerializer,
    ScheduleSerializer, QuestionnaireSerializer, ObservationSerializer,
    ResultSerializer, QuestionSerializer
)
from .models import Staff, Student, Schedule, Questionnaire, Observation, Result, Question
from django.utils.translation import ugettext_lazy as _
from rest_framework import permissions, authentication
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.decorators import action
from rest_framework.reverse import reverse
from . import permissions as custom_perm
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework import status
from django.utils import timezone

# get the current user model
Profile = get_user_model()


class APIRootView(APIView):
    """
    API root view, returns the urls to all api endpoint.
    """
    permission_class = [permissions.AllowAny]

    def get(self, request, format=None, *args, **kwargs):
        profiles = reverse("careerguide:profile-list", request=request, format=format)
        staffs = reverse("careerguide:staff-list", request=request, format=format)
        students = reverse("careerguide:student-list", request=request, format=format)
        questions = reverse("careerguide:questions-list", request=request, format=format)

        serializer = {"profiles": profiles, "staffs": staffs, "students": students, "questions": questions}
        return Response(data=serializer, status=status.HTTP_200_OK)



# create views
class ProfileViewSet(viewsets.GenericViewSet):
    lookup_field = "id"
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def list(self, request, *args, **kwargs):
        serializer = self.serializer_class(self.get_queryset(), many=True, context={"request": request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        serializer = self.serializer_class(self.get_object(), context={"request": request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={"request": request})

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={"request": request}, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        user = self.get_object()
        userid = user.id
        user.delete()
        serializer = {"profile_id": userid, "detail": "Deleted successfully"}
        return Response(data=serializer, status=status.HTTP_204_NO_CONTENT)


class StaffViewSet(viewsets.GenericViewSet):
    lookup_field = "staff_id"
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer

    def get_object(self, *args, **kwargs):
        """
        Edited so as to perform a case insensitive search.
        """
        queryset = self.get_queryset()
        obj = get_object_or_404(queryset, staff_id__iexact=self.kwargs['staff_id'])

        self.check_object_permissions(self.request, obj)
        return obj

    def get_permissions(self, *args, **kwargs):
        if self.action is 'create':
            permission_classes = [permissions.AllowAny,]
        elif self.action == 'list':
            permission_classes = [permissions.IsAdminUser,]
        else:
            permission_classes = [custom_perm.IsOwnerStaff,]
        return [perm() for perm in permission_classes]

    def list(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_queryset(), many=True, context={"request": request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        serializer = self.get_serializer(self.get_object(), context={"request": request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data, context={"request": request})

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        serializer = self.get_serializer(instance=self.get_object(), data=request.data, context={"request": request}, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        staff = self.get_object()
        name, id = [staff.staff_full_name(), staff.staff_id]
        staff.delete()
        serializer = {"fullname": name, "staff_id": id, "detail": "Deleted successfully"}
        return Response(data=serializer, status=status.HTTP_204_NO_CONTENT)


class StudentViewSet(viewsets.GenericViewSet):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    permission_classes = [permissions.AllowAny]

    def get_object(self):
        # Get an object instance with the following lookup fields.
        # make sure to edit the hyperlink identity field on the serializer class to make use
        # of two url kwargs
        lookup_kwargs = {
            "department": self.kwargs["department"],
            "level": self.kwargs["level"],
            "reg_no": self.kwargs["reg_no"]
        }

        obj  = get_object_or_404(self.get_queryset(), **lookup_kwargs)
        # make sure to check for object level perfomission
        self.check_object_permissions(self.request, obj)
        # then return obj instance
        return obj

    def list(self, request, *args, **kwargs):
        serializer = self.serializer_class(self.get_queryset(), many=True, context={"request": request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        serializer = self.serializer_class(self.get_object(), context={"request": request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={"request": request})

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        serializer = self.serializer_class(instance=self.get_object(), data=request.data, context={"request": request}, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        student = self.get_object()
        fullname, dept, level, reg_no = [student.student_full_name(), student.department, student.level, student.reg_no]
        student.delete()
        serializer = {
            "fullname": fullname,
            "Reg number": reg_no,
            "level": level,
            "department": dept,
            "detail": "Deleted successfully"
        }
        return Response(data=serializer, status=status.HTTP_204_NO_CONTENT)


class ScheduleViewSet(viewsets.GenericViewSet):
    queryset = Schedule.objects.all()
    serializer_class = ScheduleSerializer

    def get_queryset(self):
        # modified queryset to return a list of schedules belonging to the
        # logged in user.
        queryset = super().get_queryset()
        queryset = queryset.filter(staff=self.request.user.staff).order_by("-created")
        return queryset

    def get_object(self):
        # Modified to return an instance of the logged in users schedule.
        # make sure to edit the hyperlink identity field on the serializer class to make use
        # of two url kwargs [staff_id and instance id]
        obj = get_object_or_404(self.get_queryset(), staff__staff_id=self.request.user.staff.staff_id, id=self.kwargs["id"])

        # Make sure to check if the user has object level permission
        self.check_object_permissions(self.request, obj)
        return obj

    def list(self, request, *args, **kwargs):
        serializer = self.serializer_class(self.get_queryset(), many=True, context={"request": request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        serializer = self.serializer_class(self.get_object(), context={"request": request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={"request": request})

        # make sure this schedule belongs to the currently logged in staff
        if request.user.staff.staff_id == self.kwargs["staff_id"].upper():

            # check to make sure the expire field was filled with a date, else populate
            # it with a date 7 days in the future.
            if serializer.initial_data.get('expire'):
                if timezone.datetime.fromisoformat(serializer.initial_data["expire"]) < timezone.datetime.now():
                    return Response(data={"detail": _("Expire Date cannot be in the past")}, status=status.HTTP_400_BAD_REQUEST)
                else:
                    pass
            else:
                serializer.initial_data["expire"] = timezone.datetime.now() + timezone.timedelta(days=7)

            if serializer.is_valid():
                serializer.save(staff=request.user.staff)
                return Response(data=serializer.data, status=status.HTTP_201_CREATED)
            # else if serializer is not valid
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # else if logged the in staff is not the owner of this schedule
        serializer = {"detail": "You are not the owner of the account you are trying to create a schedule for!"}
        return Response(data=serializer, status=status.HTTP_406_NOT_ACCEPTABLE)

    def update(self, request, *args, **kwargs):
        serializer = self.serializer_class(instance=self.get_object(), data=request.data, context={"request": request}, partial=True)

        # make sure this schedule belongs to the currently logged in staff
        if request.user.staff.staff_id == self.kwargs["staff_id"].upper():
            if serializer.is_valid():
                serializer.save(staff=request.user.staff)
                return Response(data=serializer.data, status=status.HTTP_202_ACCEPTED)
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # else if logged the in staff is not the owner of this schedule
        serializer = {"detail": "You are not the owner of the account you are trying to create a schedule for!"}
        return Response(data=serializer, status=status.HTTP_406_NOT_ACCEPTABLE)

    def destroy(self, request, *args, **kwargs):
        schedule = self.get_object()
        staff, title = [schedule.staff.staff_id, schedule.title]
        schedule.delete()
        serializer = {"staff id": staff, "title": title, "detail": "Deleted successfully"}
        return Response(data=serializer, status=status.HTTP_204_NO_CONTENT)


class QuestionnaireViewSet(viewsets.GenericViewSet):
    queryset = Questionnaire.objects.all()
    serializer_class = QuestionnaireSerializer

    def get_queryset(self):
        # return a list of questionnaire created by the logged in staff
        queryset = super().get_queryset()
        queryset = queryset.filter(staff=self.request.user.staff).order_by("-created")
        return queryset

    def get_object(self):
        # return an instance of a questionnaire for the logged in staff and the specified id.
        # make sure to edit the hyperlink identity field on the serializer class to make use
        # of two url kwargs [staff_id and intance id]
        obj = get_object_or_404(self.get_queryset(), staff__staff_id=self.request.user.staff.staff_id, id=self.kwargs["id"])

        # make sure to check for object level permissions
        self.check_object_permissions(self.request, obj)
        return obj

    def list(self, request, *args, **kwargs):
        serializer = self.serializer_class(self.get_queryset(), many=True, context={"request": request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        serializer = self.serializer_class(self.get_object(), context={"request": request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={"request":  request})

        # First, we need to retrieve reg_no's belonging to students in each category.
        # get the categories field from the initial_data
        categories = serializer.initial_data.get("categories")
        # print(F"categories: {categories}")
        # default categories
        all_department = set({"art", "commercial", "science", "social science"})
        all_level = set({"jss1", "jss2", "jss3", "sss1", "sss2", "sss3"})
        all_gender = set({"male", "female"})
        
        # retrieved categories
        try:
            categories = set({cat for cat in categories})
        except TypeError:
            categories = set({})
        # else:
        #     categories = set({cat for cat in categories})

        student_queryset = Student.objects.all()

        # Here i made use of the set intersection method to provide only the supplied categories
        # from the frontend or non at all.
        student_category = [student for student in student_queryset.filter(
            department__in=[dept for dept in all_department.intersection(categories)],
            level__in=[lvl for lvl in all_level.intersection(categories)],
            profile__gender__in=[sex for sex in all_gender.intersection(categories)]
        )]

        # then update the students field with the reg number of students in each category
        serializer.initial_data["students"] = [student.profile.id for student in student_category]
        # and also update the category field to contain a string of space delimated values of the
        # student_category
        serializer.initial_data["categories"] = ",".join(categories)
        print(serializer.initial_data["categories"])
        print(serializer.initial_data["students"])

        if serializer.is_valid():
            serializer.save(staff=request.user.staff)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        serializer = self.serializer_class(instance=self.get_object(), data=request.data, context={"request": request}, partial=True)

        # First, we need to retrieve reg_no's belonging to students in each category.
        # get the categories field from the validated serializer
        categories = serializer.initial_data.get("categories")
        # default categories
        all_department: set = set({"art", "commercial", "science", "social science"})
        all_level: set = set({"jss1", "jss2", "jss3", "sss1", "sss2", "sss3"})
        all_gender: set = set({"male", "female"})
        
        # retrieved categories
        try:
            categories: set = set({cat for cat in categories})
        except TypeError:
            categories: set = set({})
        else:
            categories: set = set({cat for cat in categories})

        student_queryset = Student.objects.all()

        student_category: set = [student for student in student_queryset.filter(
            department__in=[dept for dept in all_department.intersection(categories)],
            level__in=[lvl for lvl in all_level.intersection(categories)],
            profile__gender__in=[sex for sex in all_gender.intersection(categories)]
        )]

        # then update the students field with the reg number of students in each category
        serializer.initial_data["students"] = [student.profile.id for student in student_category]
        # and also update the category field to contain a string of space delimated values of the
        # student_category
        serializer.initial_data["categories"] = ",".join(categories)
        print(serializer.initial_data["categories"])
        print(serializer.initial_data["students"])

        if serializer.is_valid():
            serializer.save(staff=request.user.staff)
            return Response(data=serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        question = self.get_object()
        q_id, q_title, q_completed = [question.id, question.title, question.completed]
        question.delete()
        serializer = {"id": q_id, "title": q_title, "completed": q_completed, "detail": "Deleted successfully"}
        return Response(data=serializer, status=status.HTTP_200_OK)


class QuestionViewSet(viewsets.GenericViewSet):
    lookup_field = "id"
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    
    def list(self, request, *args, **kwargs):
        serializer = self.serializer_class(self.get_queryset(), many=True, context={"request": request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        serializer = self.serializer_class(self.get_object(), context={"request": request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={"request":  request})

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        serializer = self.serializer_class(instance=self.get_object(), data=request.data, context={"request": request}, partial=True)

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        question = self.get_object()
        id, title, created = [question.id, question.title, question.created]
        question.delete()
        serializer = {"id": id, "title": title, "created": created, "detail": "Deleted successfully"}
        return Response(data=serializer, status=status.HTTP_204_NO_CONTENT)



class ObservationViewSet(viewsets.GenericViewSet):
    queryset = Observation.objects.all()
    serializer_class = ObservationSerializer

    def get_queryset(self):
        # return a list of observations created by the logged in staff
        queryset = super().get_queryset()

        # lookup fields from url to filter the object.
        lookup_kwargs = {
            "student__department": self.kwargs["department"],
            "student__level": self.kwargs["level"],
            "student__reg_no": self.kwargs["reg_no"],
        }
        queryset = queryset.filter(**lookup_kwargs).order_by("-created")
        return queryset

    def get_object(self):
        # return an instance of a observation for the student instance.
        # make sure to edit the hyperlink identity field on the serializer class to make use
        # of the appropriate lookup fields.
        lookup_kwargs = {
            "student__department": self.kwargs["department"],
            "student__level": self.kwargs["level"],
            "student__reg_no": self.kwargs["reg_no"],
            "id": self.kwargs["id"],
        }
        obj = get_object_or_404(self.get_queryset(), **lookup_kwargs)
        # make sure to check for object level permissions
        self.check_object_permissions(self.request, obj)
        return obj

    def list(self, request, *args, **kwargs):
        serializer = self.serializer_class(self.get_queryset(), many=True, context={"request": request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        serializer = self.serializer_class(self.get_object(), context={"request": request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={"request":  request})

        try:
            serializer.initial_data["student"] = Student.objects.get(department=self.kwargs["department"], level=self.kwargs["level"], reg_no=self.kwargs["reg_no"])
        except Student.DoesNotExist:
            return Response(data={"datail": "Student with that ID does not exists."}, status=status.HTTP_404_NOT_FOUND)

        if serializer.is_valid():
            serializer.save(staff=request.user.staff)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        serializer = self.serializer_class(instance=self.get_object(), data=request.data, context={"request": request}, partial=True)

        if serializer.is_valid():
            serializer.save(staff=request.user.staff)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        observation = self.get_object()
        id, student, created = [observation.id, observation.student.reg_no, observation.created]
        observation.delete()
        serializer = {"id": id, "student": student, "created": created, "detail": "Deleted successfully"}
        return Response(data=serializer, status=status.HTTP_204_NO_CONTENT)


class ResultViewSet(viewsets.GenericViewSet):
    queryset = Result.objects.all()
    serializer_class = ResultSerializer

    def get_queryset(self):
        # return a list of observations created by the logged in user (staff)
        queryset = super().get_queryset().order_by("-updated")
        return queryset

    def get_object(self):
        # return an instance of a observation for the student instance.
        # make sure to edit the hyperlink identity field on the serializer class to make use
        # of the appropriate lookup fields.
        lookup_kwargs = {
            "student__department": self.kwargs["department"],
            "student__level": self.kwargs["level"],
            "student__reg_no": self.kwargs["reg_no"],
        }
        obj = get_object_or_404(self.get_queryset(), **lookup_kwargs)
        # make sure to check for object level permissions
        self.check_object_permissions(self.request, obj)
        return obj

    def list(self, request, *args, **kwargs):
        serializer = self.serializer_class(self.get_queryset(), many=True, context={"request": request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        serializer = self.serializer_class(self.get_object(), context={"request": request})
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={"request":  request})

        try:
            serializer.initial_data["student"] = Student.objects.get(department=self.kwargs["department"], level=self.kwargs["level"], reg_no=self.kwargs["reg_no"])
        except Student.DoesNotExist:
            return Response(data={"datail": "Student with that ID does not exists."}, status=status.HTTP_404_NOT_FOUND)

        if serializer.is_valid():
            serializer.save(staff=request.user.staff)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        serializer = self.serializer_class(instance=self.get_object(), data=request.data, context={"request": request}, partial=True)

        if serializer.is_valid():
            serializer.save(staff=request.user.staff)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        result = self.get_object()
        id, student, staff = [result.id, result.student.sid, result.staff.staff_id]
        result.delete()
        serializer = {"id": id, "student": student, "staff": staff, "detail": "Deleted successfully"}
        return Response(data=serializer, status=status.HTTP_204_NO_CONTENT)