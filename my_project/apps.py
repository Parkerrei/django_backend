from django.apps import AppConfig


class MyProjectConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'my_project'

    def ready(self):
        # import signals to ensure they are registered
        from . import signals 

    
    