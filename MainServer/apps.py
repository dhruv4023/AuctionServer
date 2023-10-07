from django.apps import AppConfig

class MyAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'djangoserver'

    def ready(self):
        from . import scheduler
        print("scheduler is started...")
        scheduler.schedule_task()
