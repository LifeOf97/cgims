from django.db.models.signals import post_save, post_delete
from django.apps import AppConfig
import uuid


class CareerguideConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'careerguide'

    def ready(self) -> None:
        from . import signals
        from . import models

        post_delete.connect(signals.delete_staff_profile, sender=models.Staff, dispatch_uid=uuid.uuid4)
        post_delete.connect(signals.delete_student_profile, sender=models.Student, dispatch_uid=uuid.uuid4)
