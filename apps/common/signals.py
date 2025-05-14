import os
from django.db.models.signals import post_delete, pre_delete, post_migrate
from django.core.management import call_command
from django.dispatch import receiver
from apps.common.models import Country


@receiver(post_delete, sender=Country)
def country_post_delete(sender, instance, **kwargs):
    print(f"Country {instance.name} has been deleted!")

    if os.path.exists(instance.icon.path):
        os.remove(instance.icon.path)
        print(f"Flag image {instance.icon.path} has been removed successfully.")


@receiver(pre_delete, sender=Country)
def country_pre_delete(sender, instance, **kwargs):
    print(f"Preparing to delete country {instance.name} {instance.ico_code}.")


@receiver(post_migrate)
def post_migrate(sender, **kwargs):
    print(f"Migrations for {sender.name} have been applied successfully.")
    if sender.name == 'apps.common':
        call_command("load_countries")
