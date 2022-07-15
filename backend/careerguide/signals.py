# NOTE: this signals are explicitly connected to in th apps.py file
from django.contrib.auth import get_user_model

Profile = get_user_model()


def delete_staff_profile(sender, instance, **kwargs):
    """
    When a staff instance is deleted, we need to also delete
    the corresponding staff profile
    """
    try:
        profile = Profile.objects.get(username__iexact=instance.staff_id)
    except Profile.DoesNotExist:
        pass
    else:
        profile.delete()

def delete_student_profile(sender, instance, **kwargs):
    """
    When a students instance is deleted, we need to also delete
    the corresponding student profile
    """
    try:
        profile = Profile.objects.get(username__iexact=instance.sid)
    except Profile.DoesNotExist:
        pass
    else:
        profile.delete()