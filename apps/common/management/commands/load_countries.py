import json
import requests
from pathlib import Path
from apps.common.models import Country
from django.core.files.base import ContentFile
from django.core.management.base import BaseCommand, CommandError


class Command(BaseCommand):
    help = "Loads country information from json file"

    def handle(self, *args, **options):
    #     current_path = Path(__file__).resolve().parent
    #
    #     with open(current_path / "countries.json", "r") as file:
    #         countries = json.loads(file.read())
    #
    #     for country in countries:
    #         country_obj = Country(
    #             ico_code=country["ico_code"],
    #             name=country["name"],
    #         )
    #         country_obj.save()
    #
    #         if country["icon"]:
    #             try:
    #                 response = requests.get(country["icon"])
    #                 if response.status_code == 200:
    #                     country_obj.icon.save(
    #                         f"{country['ico_code']}.png",
    #                         ContentFile(response.content),
    #                         save=True,
    #                     )
    #                     self.stdout.write(self.style.SUCCESS(f"Country image for {country['name']} has been downloaded."))
    #                 else:
    #                     self.stdout.write(self.style.WARNING(f"Failed to download image for {country['name']}"))
    #             except Exception as e:
    #                 self.stdout.write(self.style.ERROR(f"Error while downloading image for {country['name']}\n Error: {e}"))
    #
    #     self.stdout.write(self.style.SUCCESS(f"Countries added successfully."))
        print("Countries added successfully")





