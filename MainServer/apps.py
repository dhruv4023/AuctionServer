from django.apps import AppConfig

class MyAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'djangoserver'

    def ready(self):
        # This method is called when the application is ready to start.
        # It's a good place to perform any initialization or setup.
        from . import scheduler  # Import your scheduler module
        print("Scheduler is started...")
        scheduler.schedule_task()  # Call a function to start your scheduler
