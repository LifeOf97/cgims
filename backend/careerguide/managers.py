from django.contrib.auth.models import BaseUserManager
from django.utils.translation import ugettext_lazy as _

class AppUserManager(BaseUserManager):
    """
    Creates and saves a new user or superuser
    """

    def create_user(self, username, email, password=None):
        if not username:
            return ValueError(_("User must have a username!"))

        if not email:
            return ValueError(_("User must have an email address!"))
        
        user = self.model(email=self.normalize_email(email), username=username)
        user.set_password(password)
        user.save(using=self._db)
        return user


    def create_superuser(self, username, email, password=None):
        user = self.create_user(username=username, email=email, password=password)
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user
