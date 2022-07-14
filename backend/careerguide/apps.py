from django.apps import AppConfig


class CareerguideConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'careerguide'

    def ready(self) -> None:
        import careerguide.signals