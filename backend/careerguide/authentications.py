from django.contrib.auth.backends import ModelBackend
from django.contrib.auth import get_user_model
from rest_framework import authentication


User = get_user_model()


class CustomAuthBackend(ModelBackend):
    """
    Custom model backend that just to apply a case insensitive search
    """
    def authenticate(self, request, username=None, password=None):
        if username is None or password is None:
            return
        
        try:
            user = User.objects.get(username__iexact=username)
        except User.DoesNotExist:
            return
        else:
            if user.check_password(password) and self.user_can_authenticate(user):
                return user
