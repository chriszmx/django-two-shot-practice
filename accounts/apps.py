from django.apps import AppConfig


# this is a new APP so we need to install
# this into the projects settings.py using the file path


class AccountsConfig(AppConfig):
    default_auto_field = "django.db.models.BigAutoField"
    name = "accounts"
