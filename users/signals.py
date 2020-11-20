from django.db.models import signals
from django.dispatch import receiver
from django.contrib.auth import get_user_model

from users.models import UserLog


User = get_user_model()


@receiver(signals.post_save, sender=User, dispatch_uid="user_create_log")
def create_log(sender, instance, created, **kwargs):
    case = 1 if created else 2
    log = UserLog.objects.create(
        user=str(instance.email),
        case=case
    )


@receiver(signals.pre_delete, sender=User, dispatch_uid="user_create_delete_log")
def create_deletion_log(sender, instance, **kwargs):
    log = UserLog.objects.create(
        user=str(instance.email),
        case=3
    )