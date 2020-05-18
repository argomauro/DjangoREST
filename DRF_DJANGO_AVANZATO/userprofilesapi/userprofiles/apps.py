from django.apps import AppConfig


class UserprofilesConfig(AppConfig):
    name = 'userprofiles'
    verbose_name = "Profili Utente"

    def ready(self):
        import userprofiles.signals