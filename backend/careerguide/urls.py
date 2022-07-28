from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path
from . import apis

app_name = "careerguide"


urlpatterns = [
    # API" root view ulr path
    path("", apis.APIRootView.as_view(), name="APIRoot"),

    # Authentication url endpoints.
    path('auth/token/signin/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('auth/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    # app user urls path
    path("profiles/", apis.ProfileViewSet.as_view({"get": "list"}), name="profile-list"),
    path("profiles/create/", apis.ProfileViewSet.as_view({"post": "create"}), name="profile-create"),
    path("profiles/<uuid:id>/", apis.ProfileViewSet.as_view({"get": "retrieve"}), name="profile-detail"),
    path("profiles/<uuid:id>/update/", apis.ProfileViewSet.as_view({"put": "update", "patch": "update"}), name="profile-update"),
    path("profiles/<uuid:id>/delete/", apis.ProfileViewSet.as_view({"delete": "destroy"}), name="profile-delete"),

    # staff urls path
    path("staffs/", apis.StaffViewSet.as_view({"get": "list"}), name="staff-list"),
    path("staffs/create/", apis.StaffViewSet.as_view({"post": "create"}), name="staff-create"),
    path("staffs/me/", apis.StaffViewSet.as_view({"get": "retrieve"}), name="staff-detail"),
    path("staffs/me/update/", apis.StaffViewSet.as_view({"put": "update", "patch": "update"}), name="staff-update"),
    path("staffs/me/delete/", apis.StaffViewSet.as_view({"delete": "destroy"}), name="staff-delete"),

    # staff schedule urls
    path("staffs/me/schedules/", apis.ScheduleViewSet.as_view({"get": "list"}), name="staff-schedule-list"),
    path("staffs/me/schedules/create/", apis.ScheduleViewSet.as_view({"post": "create"}), name="staff-schedule-create"),
    path("staffs/me/schedules/<int:id>/", apis.ScheduleViewSet.as_view({"get": "retrieve"}), name="staff-schedule-detail"),
    path("staffs/me/schedules/<int:id>/update/", apis.ScheduleViewSet.as_view({"put": "update", "patch": "update"}), name="staff-schedule-update"),
    path("staffs/me/schedules/<int:id>/delete/", apis.ScheduleViewSet.as_view({"delete": "destroy"}), name="staff-schedule-delete"),
    
    # staffs questionnaire urls path
    path("staffs/me/questionnaires/", apis.QuestionnaireViewSet.as_view({"get": "list"}), name="staff-questionnaire-list"),
    path("staffs/me/questionnaires/create/", apis.QuestionnaireViewSet.as_view({"post": "create"}), name="staff-questionnaire-create"),
    path("staffs/me/questionnaires/<int:id>/", apis.QuestionnaireViewSet.as_view({"get": "retrieve"}), name="staff-questionnaire-detail"),
    path("staffs/me/questionnaires/<int:id>/update/", apis.QuestionnaireViewSet.as_view({"put": "update", "patch": "update"}), name="staff-questionnaire-update"),
    path("staffs/me/questionnaires/<int:id>/delete/", apis.QuestionnaireViewSet.as_view({"delete": "destroy"}), name="staff-questionnaire-delete"),

    # questions url
    path("questions/", apis.QuestionViewSet.as_view({"get": "list"}), name="questions-list"),
    path("questions/create/", apis.QuestionViewSet.as_view({"post": "create"}), name="questions-create"),
    path("questions/<int:id>/", apis.QuestionViewSet.as_view({"get": "retrieve"}), name="questions-detail"),
    path("questions/<int:id>/update/", apis.QuestionViewSet.as_view({"put": "update", "patch": "update"}), name="questions-update"),
    path("questions/<int:id>/delete/", apis.QuestionViewSet.as_view({"delete": "destroy"}), name="questions-delete"),

    # student urls path
    path("students/", apis.StudentViewSet.as_view({"get": "list"}), name="student-list"),
    path("students/create/", apis.StudentViewSet.as_view({"post": "create"}), name="student-create"),
    path("students/<str:department>/<str:level>/<str:reg_no>/", apis.StudentViewSet.as_view({"get": "retrieve"}), name="student-detail"),
    path("students/<str:department>/<str:level>/<str:reg_no>/update/", apis.StudentViewSet.as_view({"put": "update", "patch": "update"}), name="student-update"),
    path("students/<str:department>/<str:level>/<str:reg_no>/delete/", apis.StudentViewSet.as_view({"delete": "destroy"}), name="student-delete"),

    # # students observations urls path
    # path("students/<str:department>/<str:level>/<str:reg_no>/observations/", apis.ObservationViewSet.as_view({"get": "list"}), name="students-observation-list"),
    # path("students/<str:department>/<str:level>/<str:reg_no>/observations/create/", apis.ObservationViewSet.as_view({"post": "create"}), name="students-observation-create"),
    # path("students/<str:department>/<str:level>/<str:reg_no>/observations/<int:id>/", apis.ObservationViewSet.as_view({"get": "retrieve"}), name="students-observation-detail"),
    # path("students/<str:department>/<str:level>/<str:reg_no>/observations/<int:id>/update/", apis.ObservationViewSet.as_view({"put": "update", "patch": "update"}), name="students-observation-update"),
    # path("students/<str:department>/<str:level>/<str:reg_no>/observations/<int:id>/delete/", apis.ObservationViewSet.as_view({"delete": "destroy"}), name="students-observation-delete"),

    # # students result urls path
    # path("students/results/", apis.ResultViewSet.as_view({"get": "list"}), name="students-result-list"),
    # path("students/<str:department>/<str:level>/<str:reg_no>/results/", apis.ResultViewSet.as_view({"get": "retrieve"}), name="students-result-detail"),
    # path("students/<str:department>/<str:level>/<str:reg_no>/results/create/", apis.ResultViewSet.as_view({"post": "create"}), name="students-result-create"),
    # path("students/<str:department>/<str:level>/<str:reg_no>/results/update/", apis.ResultViewSet.as_view({"put": "update", "patch": "update"}), name="students-result-update"),
    # path("students/<str:department>/<str:level>/<str:reg_no>/results/delete/", apis.ResultViewSet.as_view({"delete": "destroy"}), name="students-result-delete"),

]
