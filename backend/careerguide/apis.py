from .serializers import (
    ProfileSerializer,
    StaffSerializer,
    StudentSerializer,
    ScheduleSerializer,
    QuestionnaireSerializer,
    ObservationSerializer,
    ResultSerializer,
    QuestionSerializer,
)
from .models import (
    Staff,
    Student,
    Schedule,
    Questionnaire,
    Observation,
    Result,
    Question,
)
from django.utils.translation import ugettext_lazy as _
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework.response import Response
from rest_framework.reverse import reverse
from . import permissions as custom_perm
from rest_framework.views import APIView
from rest_framework import permissions
from rest_framework import viewsets
from rest_framework import status
from django.utils import timezone
from django.db.models import Q

# get the current user model
Profile = get_user_model()


class APIRootView(APIView):
    """
    API root view, returns the urls to top api endpoint.
    """
    authentication_classes = []
    permission_classes = [permissions.AllowAny]

    def get(self, request, format=None, *args, **kwargs):
        profiles = reverse("careerguide:profile-list", request=request, format=format)
        staffs = reverse("careerguide:staff-list", request=request, format=format)
        students = reverse("careerguide:student-list", request=request, format=format)
        questions = reverse(
            "careerguide:questions-list", request=request, format=format
        )

        serializer = {
            "profiles": profiles,
            "staffs": staffs,
            "students": students,
            "questions": questions,
        }
        return Response(data=serializer, status=status.HTTP_200_OK)


# create views
class ProfileViewSet(viewsets.GenericViewSet):
    """
    Profiles endpoint
    """

    lookup_field = "id"
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer

    def list(self, request, *args, **kwargs):
        """
        Returns all profiles in the system.
        """
        serializer = self.serializer_class(
            self.get_queryset(), many=True, context={"request": request}
        )
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        """
        Returns a specific profile instance as indicated by the provided profile id.
        """
        serializer = self.serializer_class(
            self.get_object(), context={"request": request}
        )
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        """
        Creates a new profile instance, returns the newly created profile data.
        """
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        """
        Updates the profile instance as indicated by the provided profile id, returns the updated data.
        """
        serializer = self.serializer_class(
            data=request.data, context={"request": request}, partial=True
        )

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        """
        Permanently deletes the profile instance as indicated by the provided profile id, returns a minimal data
        of the deleted instance for reference.
        """
        user = self.get_object()
        userid = user.id
        user.delete()
        serializer = {"profile_id": userid, "detail": "Deleted successfully"}
        return Response(data=serializer, status=status.HTTP_204_NO_CONTENT)


class StaffViewSet(viewsets.GenericViewSet):
    """
    Staffs endpoints
    """

    lookup_field = "staff_id"
    queryset = Staff.objects.all()
    serializer_class = StaffSerializer

    def get_object(self, *args, **kwargs):
        """
        Edited so as to perform a case insensitive search.
        """
        queryset = self.get_queryset()
        obj = get_object_or_404(
            queryset, staff_id__iexact=self.request.user.staff.staff_id
        )

        self.check_object_permissions(self.request, obj)
        return obj

    def get_permissions(self, *args, **kwargs):
        if self.action == "create":
            permission_classes = [
                permissions.AllowAny,
            ]
        elif self.action == "list":
            permission_classes = [
                permissions.IsAdminUser,
            ]
        else:
            permission_classes = [
                custom_perm.IsOwnerStaff,
            ]
        return [perm() for perm in permission_classes]

    def list(self, request, *args, **kwargs):
        """
        Returns all staffs data in the system.
        """
        serializer = self.get_serializer(
            self.get_queryset(), many=True, context={"request": request}
        )
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        """
        Returns the data of the currently authenticated staff.
        """
        serializer = self.get_serializer(
            self.get_object(), context={"request": request}
        )
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        """
        Creates a new staff instance, returns the newly created staff data.
        """
        serializer = self.get_serializer(
            data=request.data, context={"request": request}
        )
        print(serializer.initial_data)
        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        """
        Update the data of the currently authenticated staff, returns the updated staff data.
        """
        serializer = self.get_serializer(
            instance=self.get_object(),
            data=request.data,
            context={"request": request},
            partial=True,
        )

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        """
        Permanently deletes the currently authenticated staff from the system,
        returns a minimal data of the deleted staff for reference.
        """
        staff = self.get_object()
        name, id = [staff.staff_full_name(), staff.staff_id]
        staff.delete()
        serializer = {
            "fullname": name,
            "staff_id": id,
            "detail": "Deleted successfully",
        }
        return Response(data=serializer, status=status.HTTP_204_NO_CONTENT)


class StudentViewSet(viewsets.GenericViewSet):
    """
    Students endpoints
    """

    queryset = Student.objects.all()
    serializer_class = StudentSerializer

    def get_object(self):
        # Get an object instance with the following lookup fields.
        # make sure to edit the hyperlink identity field on the serializer class to make use
        # of two url kwargs
        lookup_kwargs = {
            "department": self.kwargs["department"].lower(),
            "level": self.kwargs["level"].lower(),
            "reg_no": self.kwargs["reg_no"].lower(),
        }

        obj = get_object_or_404(self.get_queryset(), **lookup_kwargs)
        # make sure to check for object level perfomission
        self.check_object_permissions(self.request, obj)
        # then return obj instance
        return obj

    def list(self, request, *args, **kwargs):
        """
        Returns all students data in the system.
        """
        serializer = self.serializer_class(
            self.get_queryset(), many=True, context={"request": request}
        )
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        """
        Returns the data of the currently authenticated student.
        """
        serializer = self.serializer_class(
            self.get_object(), context={"request": request}
        )
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        """
        Creates a new student, returns the newly created student data.
        """
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_201_CREATED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        """
        Update the data of the currently authenticated student, returns the updated student data.
        """
        serializer = self.serializer_class(
            instance=self.get_object(),
            data=request.data,
            context={"request": request},
            partial=True,
        )

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        """
        Permanently deletes the currently authenticated student from the system, returns a minimal
        data of the deleted student for reference.
        """
        student = self.get_object()
        fullname, dept, level, reg_no = [
            student.student_full_name(),
            student.department,
            student.level,
            student.reg_no,
        ]
        student.delete()
        serializer = {
            "fullname": fullname,
            "Reg number": reg_no,
            "level": level,
            "department": dept,
            "detail": "Deleted successfully",
        }
        return Response(data=serializer, status=status.HTTP_204_NO_CONTENT)


class ScheduleViewSet(viewsets.GenericViewSet):
    """
    Staffs scheduls endpoint.
    """
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
        obj = get_object_or_404(
            self.get_queryset(), staff=self.request.user.staff, id=self.kwargs["id"]
        )

        # Make sure to check if the user has object level permission
        self.check_object_permissions(self.request, obj)
        return obj

    def list(self, request, *args, **kwargs):
        """
        Returns all schedules belonging to the currently authenticated staff.
        """
        serializer = self.serializer_class(
            self.get_queryset(), many=True, context={"request": request}
        )
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        """
        Returns a particular schedule belonging to the currently authenticated staff,
        as indicated by the provided schedule id.
        """
        serializer = self.serializer_class(
            self.get_object(), context={"request": request}
        )
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        """
        Creates a new schedule for the currently authenticated staff, returns the newly created
        schedule data.
        """
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )

        # check to make sure the expire field was filled with a date, else populate
        # it with a date 7 days in the future.
        if serializer.initial_data.get("expire"):
            if timezone.datetime.date(
                timezone.datetime.fromisoformat(serializer.initial_data["expire"])
            ) < timezone.datetime.date(timezone.datetime.now()):
                return Response(
                    data={"detail": _("Expire Date cannot be in the past")},
                    status=status.HTTP_400_BAD_REQUEST,
                )
            else:
                pass
        else:
            serializer.initial_data["expire"] = timezone.datetime.date(
                timezone.datetime.now()
            ) + timezone.timedelta(days=7)

        if self.get_queryset().count() < 8:
            if serializer.is_valid():
                serializer.save(staff=request.user.staff)
                return Response(data=serializer.data, status=status.HTTP_201_CREATED)
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        return Response(
            data={"error": "Maximum schedule limit reached."},
            status=status.HTTP_406_NOT_ACCEPTABLE,
        )

    def update(self, request, *args, **kwargs):
        """
        Updates the data of the schedule instance as provided by the schedule id, returns
        the newly updated schedule data.
        """
        serializer = self.serializer_class(
            instance=self.get_object(),
            data=request.data,
            context={"request": request},
            partial=True,
        )

        if serializer.is_valid():
            serializer.save(staff=request.user.staff)
            return Response(data=serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        """
        Parmanently deletes a schedule instance as indicated by the provided by the schedule id
        from the system, returns a minimal data of the deleted schedule for reference.
        """
        schedule = self.get_object()
        id, staff, title, created = [
            schedule.id,
            schedule.staff.staff_id,
            schedule.title,
            schedule.created,
        ]
        schedule.delete()
        serializer = {
            "id": id,
            "staff": staff,
            "title": title,
            "created": created,
            "detail": "Deleted successfully",
        }
        return Response(data=serializer, status=status.HTTP_204_NO_CONTENT)


class QuestionnaireViewSet(viewsets.GenericViewSet):
    """
    Staffs questionnaires endpoint.
    """
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
        obj = get_object_or_404(
            self.get_queryset(), staff=self.request.user.staff, id=self.kwargs["id"]
        )

        # make sure to check for object level permissions
        self.check_object_permissions(self.request, obj)
        return obj

    def list(self, request, *args, **kwargs):
        """
        Returns all questionnaires created by the currently authenticated staff.
        """
        serializer = self.serializer_class(
            self.get_queryset(), many=True, context={"request": request}
        )
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        """
        Returns a particular questionnaire belonging to the currently authenticated staff,
        as indicated by the provided questionnaire id.
        """
        serializer = self.serializer_class(
            self.get_object(), context={"request": request}
        )
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        """
        Creates a new questionnaire belonging to the currently authenticated staff,
        return the newly created questionnaire.
        """
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )

        categories = list(
            set([cat.lower() for cat in serializer.initial_data.get("categories")])
        )

        student_category = [
            student
            for student in Student.objects.filter(
                Q(department__in=[dept for dept in categories])
                | Q(level__in=[lvl for lvl in categories])
                | Q(profile__gender__in=[gender for gender in categories])
            )
        ]

        # set the students field to the all students that fit into any of the categories
        serializer.initial_data["students"] = [
            student.sid for student in student_category
        ]

        if serializer.is_valid():
            serializer.save(staff=request.user.staff)
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        """
        Updates the data of the questionnaire instance as indicated by the provided questionnaire
        id, returns the newly updated questionnaire data.
        """
        serializer = self.serializer_class(
            instance=self.get_object(),
            data=request.data,
            context={"request": request},
            partial=True,
        )

        categories = list(
            set([cat.lower() for cat in serializer.initial_data.get("categories")])
        )

        student_category = [
            student
            for student in Student.objects.filter(
                Q(department__in=[dept for dept in categories])
                | Q(level__in=[lvl for lvl in categories])
                | Q(profile__gender__in=[gender for gender in categories])
            )
        ]

        # set the students field to the all students that fit into any of the categories
        serializer.initial_data["students"] = [
            student.sid for student in student_category
        ]

        if serializer.is_valid():
            serializer.save(staff=request.user.staff)
            return Response(data=serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        """
        Parmanently deletes a questionnaire instance as indicated by the provided questionnaire
        id from the system and returns a minimal data for reference.
        """
        question = self.get_object()
        id, staff, title, completed = [
            question.id,
            question.staff.staff_id,
            question.title,
            question.completed,
        ]
        question.delete()
        serializer = {
            "id": id,
            "staff": staff,
            "title": title,
            "completed": completed,
            "detail": "Deleted successfully",
        }
        return Response(data=serializer, status=status.HTTP_200_OK)


class QuestionViewSet(viewsets.GenericViewSet):
    """
    Custom Questionnaire endpoint.
    """
    lookup_field = "id"
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer

    def list(self, request, *args, **kwargs):
        """
        Returns a list of all custom questionnaires in the system.
        """
        serializer = self.serializer_class(
            self.get_queryset(), many=True, context={"request": request}
        )
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def retrieve(self, request, *args, **kwargs):
        """
        Returns a particular questionnaire data as indicated by the provided questionnaire id.
        """
        serializer = self.serializer_class(
            self.get_object(), context={"request": request}
        )
        return Response(data=serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        """
        Creates a new questionnaire data made available to all staffs, returns the newly created
        questionnaire.
        """
        serializer = self.serializer_class(
            data=request.data, context={"request": request}
        )

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_200_OK)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def update(self, request, *args, **kwargs):
        """
        Updates a particular questionnaire data as indicated by the provided questionnaire id,
        returns the newly updated questionnaire.
        """
        serializer = self.serializer_class(
            instance=self.get_object(),
            data=request.data,
            context={"request": request},
            partial=True,
        )

        if serializer.is_valid():
            serializer.save()
            return Response(data=serializer.data, status=status.HTTP_202_ACCEPTED)
        return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, *args, **kwargs):
        """
        Parmanently deletes a particular questionnaire data as indicated by thge provided questionnaire id
        from the system, returns a minimal data for reference.
        """
        question = self.get_object()
        id, title, created = [question.id, question.title, question.created]
        question.delete()
        serializer = {
            "id": id,
            "title": title,
            "created": created,
            "detail": "Deleted successfully",
        }
        return Response(data=serializer, status=status.HTTP_204_NO_CONTENT)


# class ObservationViewSet(viewsets.GenericViewSet):
#     """
#     Staffs observations on students endpoint.
#     """
#     queryset = Observation.objects.all()
#     serializer_class = ObservationSerializer

#     def get_queryset(self):
#         # return a list of observations created by the logged in staff
#         queryset = super().get_queryset()

#         # lookup fields from url to filter the object.
#         lookup_kwargs = {
#             "student__department": self.kwargs["department"],
#             "student__level": self.kwargs["level"],
#             "student__reg_no": self.kwargs["reg_no"],
#         }
#         queryset = queryset.filter(**lookup_kwargs).order_by("-created")
#         return queryset

#     def get_object(self):
#         # return an instance of a observation for the student instance.
#         # make sure to edit the hyperlink identity field on the serializer class to make use
#         # of the appropriate lookup fields.
#         lookup_kwargs = {
#             "student__department": self.kwargs["department"],
#             "student__level": self.kwargs["level"],
#             "student__reg_no": self.kwargs["reg_no"],
#             "id": self.kwargs["id"],
#         }
#         obj = get_object_or_404(self.get_queryset(), **lookup_kwargs)
#         # make sure to check for object level permissions
#         self.check_object_permissions(self.request, obj)
#         return obj

#     def list(self, request, *args, **kwargs):
#         serializer = self.serializer_class(
#             self.get_queryset(), many=True, context={"request": request}
#         )
#         return Response(data=serializer.data, status=status.HTTP_200_OK)

#     def retrieve(self, request, *args, **kwargs):
#         serializer = self.serializer_class(
#             self.get_object(), context={"request": request}
#         )
#         return Response(data=serializer.data, status=status.HTTP_200_OK)

#     def create(self, request, *args, **kwargs):
#         serializer = self.serializer_class(
#             data=request.data, context={"request": request}
#         )

#         try:
#             serializer.initial_data["student"] = Student.objects.get(
#                 department=self.kwargs["department"],
#                 level=self.kwargs["level"],
#                 reg_no=self.kwargs["reg_no"],
#             )
#         except Student.DoesNotExist:
#             return Response(
#                 data={"datail": "Student with that ID does not exists."},
#                 status=status.HTTP_404_NOT_FOUND,
#             )

#         if serializer.is_valid():
#             serializer.save(staff=request.user.staff)
#             return Response(data=serializer.data, status=status.HTTP_200_OK)
#         return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def update(self, request, *args, **kwargs):
#         serializer = self.serializer_class(
#             instance=self.get_object(),
#             data=request.data,
#             context={"request": request},
#             partial=True,
#         )

#         if serializer.is_valid():
#             serializer.save(staff=request.user.staff)
#             return Response(data=serializer.data, status=status.HTTP_202_ACCEPTED)
#         return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def destroy(self, request, *args, **kwargs):
#         observation = self.get_object()
#         id, student, created = [
#             observation.id,
#             observation.student.reg_no,
#             observation.created,
#         ]
#         observation.delete()
#         serializer = {
#             "id": id,
#             "student": student,
#             "created": created,
#             "detail": "Deleted successfully",
#         }
#         return Response(data=serializer, status=status.HTTP_204_NO_CONTENT)


# class ResultViewSet(viewsets.GenericViewSet):
#     """
#     Staffs
#     """
#     queryset = Result.objects.all()
#     serializer_class = ResultSerializer

#     def get_queryset(self):
#         # return a list of observations created by the logged in user (staff)
#         queryset = super().get_queryset().order_by("-updated")
#         return queryset

#     def get_object(self):
#         # return an instance of a observation for the student instance.
#         # make sure to edit the hyperlink identity field on the serializer class to make use
#         # of the appropriate lookup fields.
#         lookup_kwargs = {
#             "student__department": self.kwargs["department"],
#             "student__level": self.kwargs["level"],
#             "student__reg_no": self.kwargs["reg_no"],
#         }
#         obj = get_object_or_404(self.get_queryset(), **lookup_kwargs)
#         # make sure to check for object level permissions
#         self.check_object_permissions(self.request, obj)
#         return obj

#     def list(self, request, *args, **kwargs):
#         serializer = self.serializer_class(
#             self.get_queryset(), many=True, context={"request": request}
#         )
#         return Response(data=serializer.data, status=status.HTTP_200_OK)

#     def retrieve(self, request, *args, **kwargs):
#         serializer = self.serializer_class(
#             self.get_object(), context={"request": request}
#         )
#         return Response(data=serializer.data, status=status.HTTP_200_OK)

#     def create(self, request, *args, **kwargs):
#         serializer = self.serializer_class(
#             data=request.data, context={"request": request}
#         )

#         try:
#             serializer.initial_data["student"] = Student.objects.get(
#                 department=self.kwargs["department"],
#                 level=self.kwargs["level"],
#                 reg_no=self.kwargs["reg_no"],
#             )
#         except Student.DoesNotExist:
#             return Response(
#                 data={"datail": "Student with that ID does not exists."},
#                 status=status.HTTP_404_NOT_FOUND,
#             )

#         if serializer.is_valid():
#             serializer.save(staff=request.user.staff)
#             return Response(data=serializer.data, status=status.HTTP_200_OK)
#         return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def update(self, request, *args, **kwargs):
#         serializer = self.serializer_class(
#             instance=self.get_object(),
#             data=request.data,
#             context={"request": request},
#             partial=True,
#         )

#         if serializer.is_valid():
#             serializer.save(staff=request.user.staff)
#             return Response(data=serializer.data, status=status.HTTP_202_ACCEPTED)
#         return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#     def destroy(self, request, *args, **kwargs):
#         result = self.get_object()
#         id, student, staff = [result.id, result.student.sid, result.staff.staff_id]
#         result.delete()
#         serializer = {
#             "id": id,
#             "student": student,
#             "staff": staff,
#             "detail": "Deleted successfully",
#         }
#         return Response(data=serializer, status=status.HTTP_204_NO_CONTENT)
