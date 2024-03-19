from django.apps import AppConfig


class AccountsConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'budget_tracker.accounts'

    def ready(self):
        import budget_tracker.accounts.signals
