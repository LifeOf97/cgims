from django.utils.crypto import get_random_string
from rest_framework.reverse import reverse
from rest_framework import serializers


class StudentHyperlinkIdentityField(serializers.HyperlinkedIdentityField):
    """
    Custom student hyperlink identity field to retrieve a student instance
    using the students department, class/level, and reg_no.
    """
    def get_url(self, obj, view_name, request, format):
        url_kwargs = {
            "department": obj.department,
            "level": obj.level,
            "reg_no": obj.reg_no,
        }
        return reverse(view_name, kwargs=url_kwargs, request=request, format=format)

    def get_object(self, view_name, view_args, view_kwargs):
        lookup_kwargs = {
            "department": view_kwargs["department"],
            "level": view_kwargs["level"],
            "reg_no": view_kwargs["reg_no"],
        }

        return self.get_queryset().get(**lookup_kwargs)


class StudentHyperlinkRelatedField(serializers.HyperlinkedRelatedField):
    """
    Custom student hyperlink related field to retrieve a student instance
    using the students department, class/level, and reg_no.
    """
    def get_url(self, obj, view_name, request, format):
        url_kwargs = {
            "department": obj.department,
            "level": obj.level,
            "reg_no": obj.reg_no,
        }
        return reverse(view_name, kwargs=url_kwargs, request=request, format=format)

    def get_object(self, view_name, view_args, view_kwargs):
        lookup_kwargs = {
            "department": view_kwargs["department"],
            "level": view_kwargs["level"],
            "reg_no": view_kwargs["reg_no"],
        }

        return self.get_queryset().get(**lookup_kwargs)


class OthersToStaffHyperlinkIdentityField(serializers.HyperlinkedIdentityField):
    """
    Custom staff hyperlink identity field to retrieve a staff instance
    using the staff_id and id fields
    """
    def get_url(self, obj, view_name, request, format):
        url_kwargs = {"staff_id": obj.staff.staff_id, "id": obj.id}
        return reverse(view_name, kwargs=url_kwargs, request=request, format=format)

    def get_object(self, view_name, view_args, view_kwargs):
        lookup_kwargs = {"staff_id": view_kwargs["staff_id"], "id": view_kwargs["id"]}
        return self.get_queryset().get(**lookup_kwargs)


class StudentObservationHyperlinkIdentityField(serializers.HyperlinkedIdentityField):
    """
    Custom student observation hyperlink identity field to retrieve an observation
    belonging to a student instance using the students department, class/level,
    and reg_no.
    """
    def get_url(self, obj, view_name, request, format):
        url_kwargs = {
            "department": obj.student.department,
            "level": obj.student.level,
            "reg_no": obj.student.reg_no,
            "id": obj.id,
        }
        return reverse(view_name, kwargs=url_kwargs, request=request, format=format)

    def get_object(self, view_name, view_args, view_kwargs):
        lookup_kwargs = {
            "student__department": view_kwargs["department"],
            "student__level": view_kwargs["level"],
            "student__reg_no": view_kwargs["reg_no"],
            "id": view_kwargs["id"],
        }

        return self.get_queryset().get(**lookup_kwargs)


class StudentResultHyperlinkIdentityField(serializers.HyperlinkedIdentityField):
    """
    Custom student result hyperlink identity field to retrieve an result
    belonging to a student instance using the students department, class/level,
    and reg_no.
    """
    def get_url(self, obj, view_name, request, format):
        url_kwargs = {
            "department": obj.student.department,
            "level": obj.student.level,
            "reg_no": obj.student.reg_no,
        }
        return reverse(view_name, kwargs=url_kwargs, request=request, format=format)

    def get_object(self, view_name, view_args, view_kwargs):
        lookup_kwargs = {
            "student__department": view_kwargs["department"],
            "student__level": view_kwargs["level"],
            "student__reg_no": view_kwargs["reg_no"],
        }

        return self.get_queryset().get(**lookup_kwargs)



def save_image(instance, filename):
    """
    Function to return the file path to save the image file of
    a staff or student.
    """
    if instance.is_staff:
        return F"staffs/{instance.id}/images/{filename}"
    return F"students/{instance.id}/images/{filename}"


def make_id(pre: str = None, length: int = 10, chars: str = 'abcdefghijklmnopqrstuvwxyz0123456789') -> str:
    """
    Function to return a unique id.
    
    [PARAMETERS]
    pre: If you want the unique id to have a prefixed value.

    length: the length of the unique id not including the PRE value if present.

    chars: a string of alphanumeric values that the unique id is derived from.
    """
    if pre:
        return F"{pre}{get_random_string(length, chars)}"
    else:
        return F"{get_random_string(length, chars)}"