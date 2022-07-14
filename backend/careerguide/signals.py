from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.conf import settings


@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_profile_token(sender, instance=None, created=False, **kwargs):
    # if the profile is created then create token for that profile.
    if created and instance.is_staff:
        Token.objects.create(user=instance)