from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class EventsConfig(AppConfig):
    name = "simple_event_management_backend.events"
    verbose_name = _("Events")

    def ready(self):
        try:
            import simple_event_management_backend.events.signals  # noqa F401
        except ImportError:
            pass
