from django.apps import AppConfig


class EcwappConfig(AppConfig):
    # default_auto_field = 'django.db.models.BigAutoField'
    name = 'ecwapp'

    def ready(self):
        import ecwapp.signals
