from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import AbstractUser
from django.utils.text import slugify
from django.utils import timezone
from django.conf import settings
from .others import save_image
from django.db import models
from . import managers
import uuid

# needed data
SEX: tuple = (('male', 'male'), ('female', 'female'))
STUDENT_LEVELS: tuple = (
    ('jss1', 'jss1'),
    ('jss2', 'jss2'),
    ('jss3', 'jss3'),
    ('sss1', 'sss1'),
    ('sss2', 'sss2'),
    ('sss3', 'sss3'),
)
DEPT: tuple = (
    ('art', 'art'),
    ('science', 'science'),
    ('commercial', 'commercial'),
    ('social_science', 'social_science'),
)


# Create your models here.
class Profile(AbstractUser):
    """
    Custom user model
    """
    # user identification
    id = models.UUIDField(_("ID"), primary_key=True, unique=True, editable=False, default=uuid.uuid4)
    username = models.CharField(
        _("Username"), max_length=255, unique=True, blank=False, null=False,
        help_text=_("<b>Students username syntax: department/class/reg_no</b><br><b>Staff username syntax: STF0000</b>")
    )

    # user bio
    other_name = models.CharField(_("Other Name"), max_length=255, blank=True, null=False)
    gender = models.CharField(_("Gender"), max_length=6, choices=SEX, blank=True, null=True)
    dob = models.DateField(_("Date of Birth"), auto_now=False, auto_now_add=False, blank=True, null=True)
    image = models.ImageField(_("Image"), upload_to=save_image, blank=True, null=True)
    about = models.TextField(_("About me"), blank=True, null=True)

    # user contact information
    email = models.EmailField(_("Email Address"), max_length=254, blank=True, null=True)
    phone_1 = models.CharField(_("Phone 1"), max_length=20, blank=True, null=True)
    phone_2 = models.CharField(_("Phone 2"), max_length=20, blank=True, null=True)

    # user location
    continent = models.CharField(_("Continent"), max_length=50, blank=True, null=True)
    country = models.CharField(_("Country"), max_length=50, blank=True, null=True)
    state = models.CharField(_("State"), max_length=50, blank=True, null=True)
    postal = models.CharField(_("Postal/ZIP code"), max_length=50, blank=True, null=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', ]

    objects = managers.AppUserManager()

    class Meta:
        verbose_name = 'Profile'

    def __str__(self):
        if self.is_staff:
            return F"[STAFF] - {self.username}"
        else:
            return F"[STUDENT] - {self.username}"

    def info(self) -> str:
        if self.is_staff:
            return F"[STAFF] - {self.username}"
        return F"[STUDENT] - {self.username}"


class Staff(models.Model):
    """
    Staff model
    """
    id = models.AutoField(_("ID"), primary_key=True, unique=True, editable=False)
    profile = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    staff_id = models.CharField(_("Staff ID"), max_length=7, unique=True, blank=False, null=False, help_text=_("Example: <b>STF1234</b>"))
    level = models.CharField(_("Level"), max_length=255, blank=True, null=True)

    def __str__(self):
        return F"STAFF ID: {self.staff_id}"

    def staff_full_name(self):
        return F"{self.profile.first_name or ''} {self.profile.other_name or ''} {self.profile.last_name or ''}"


class Student(models.Model):
    """
    Students model
    """
    id = models.AutoField(_("ID"), primary_key=True, unique=True, blank=False, null=False)
    sid = models.CharField(_("SID"), max_length=255, blank=True, null=True)
    profile = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    reg_no = models.CharField(_("Reg no"), max_length=4, blank=False, null=False)
    level = models.CharField(_("Student level"), max_length=4, choices=STUDENT_LEVELS, blank=False, null=False)
    department = models.CharField(_("Department"), max_length=255, choices=DEPT, blank=False, null=False)
    parent = models.CharField(_("Parent/Guardian"), max_length=255, blank=True, null=True)

    class Meta:
        constraints = [
            # every student have a unique reg no in a particular level and department.
            # so we made the fields reg_no, level, and departmanet unique.
            models.UniqueConstraint(fields=['department', 'level', 'reg_no'], name='unique student')
        ]

    def save(self, *args, **kwargs):
        self.sid = F"{self.department}/{self.level}/{self.reg_no}".lower()
        super().save(*args, **kwargs)

    def __str__(self):
        return F"Student: {self.sid}"

    def student_full_name(self):
        return F"{self.profile.first_name or ''} {self.profile.other_name or ''} {self.profile.last_name or ''}"


class Schedule(models.Model):
    """
    Schedule model for staffs to keep a todo task(s)
    a staff can have more than one schedule.
    """
    id = models.AutoField(_("ID"), primary_key=True, unique=True, blank=False, null=False)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    title = models.CharField(_("Title"), max_length=255, blank=False, null=True)
    slug = models.SlugField(_("Title slug"), max_length=255, blank=False, null=True)
    detail = models.TextField(_("Details"), blank=True, null=True)
    created = models.DateTimeField(_("Created"), auto_now=False, auto_now_add=False, default=timezone.now, blank=False, null=False)
    expire = models.DateTimeField(_("Expire"), auto_now=False, auto_now_add=False, blank=True, null=True)
    completed = models.BooleanField(_("Completed"), default=False, blank=False, null=False)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return F"[{self.staff.staff_id}] - {self.title}"


class Questionnaire(models.Model):
    """
    Questionnaire model for staffs to create questions for students.
    """
    id = models.AutoField(_("ID"), primary_key=True, unique=True, blank=False, null=False)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    students = models.ManyToManyField(Student, related_name="questions")
    created = models.DateTimeField(_("Created"), auto_now=False, auto_now_add=False, default=timezone.now, blank=False, null=True)
    title = models.CharField(_("Title"), max_length=255, blank=False, null=False)
    slug = models.SlugField(_("Title slug"), max_length=255, blank=False, null=True)
    question = models.TextField(_("Question"), blank=False, null=False)
    completed = models.BooleanField(_("Completed"), default=False, blank=False, null=False)
    categories = models.JSONField(_("Categories"), default=list)
    # categories = models.CharField(
    #     _("Categories"), max_length=255, blank=True, null=False,
    #     help_text=_("Comma/space seperated values representing the type of students this questionnaire is ment for<br>E.G: art, ss1, male")
    # )

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return F"{self.title}"


class Question(models.Model):
    """
    Model to store predefined questions
    """
    id = models.AutoField(_("ID"), primary_key=True, unique=True, blank=False, null=False)
    title = models.CharField(_("Title"), max_length=255, blank=False, null=False)
    slug = models.SlugField(_("Title slug"), max_length=255, blank=False, null=True)
    question = models.TextField(_("Question"), blank=False, null=False)
    created = models.DateTimeField(_("Created"), auto_now=False, auto_now_add=False, default=timezone.now, blank=False, null=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self):
        return F"{self.title}"


class Observation(models.Model):
    """
    Model to store comments and observation on a particular students
    sessioin.
    """
    id = models.AutoField(_("ID"), primary_key=True, unique=True, blank=False, null=False)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, help_text=_("The staff who made the comments."))
    student = models.ForeignKey(Student, on_delete=models.CASCADE, help_text=_("The student the comment is made for."))
    detail = models.TextField(_("Details"))
    created = models.DateTimeField(_("Created"), auto_now=False, auto_now_add=False, default=timezone.now, blank=False, null=True)

    def __str__(self):
        return F"{self.staff.staff_id} - {self.student}"


class Result(models.Model):
    """
    Result model for decisions given to students by the counselling staff.
    """
    id = models.AutoField(_("ID"), primary_key=True, unique=True, blank=False, null=False)
    student = models.OneToOneField("Student", on_delete=models.CASCADE)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE, help_text=_("The staff who gave this result."))
    interest = models.CharField(_("Area of interest"), max_length=255, null=True, blank=True)
    better_perf = models.CharField(_("Area of better performance"), max_length=255, null=True, blank=True)
    desired_prof = models.CharField(_("Desired profession"), max_length=255, null=True, blank=True)
    best_sub = models.CharField(_("Best subject"), max_length=255, null=True, blank=True)
    counselling = models.TextField(_("Counselling"), blank=True, null=True)
    updated = models.DateTimeField(_("Updated"), auto_now=True, auto_now_add=False, blank=True, null=True)


    def __str__(self):
        return F"{self.student.sid}"