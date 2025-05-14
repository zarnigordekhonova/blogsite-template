import json
import requests
from pathlib import Path
from apps.common.models import Country
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "Loads country information from json file"

    def add_arguments(self, parser):
        parser.add_argument("ico_code", nargs="+", type=str)

    def handle(self, *args, **options):
        if options['ico_code']:
            for ico_code in options['ico_code']:
                try:
                    country = Country.objects.get(ico_code=ico_code)
                    country.delete()
                    self.stdout.write(self.style.SUCCESS(f"Country with ICO Code {ico_code} deleted successfully."))
                except Country.DoesNotExist:
                    self.stdout.write(self.style.ERROR(f"Country with ICO code {ico_code} does not exist!"))
        else:
            self.stdout.write(self.style.ERROR("Please provide at least one ICO code to delete!"))
            return



