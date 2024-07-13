from django.apps import AppConfig


class BasededatosConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'BaseDeDatos'
    verbose_name='perfiles'
    
    def ready(self):
        import BaseDeDatos.signals
