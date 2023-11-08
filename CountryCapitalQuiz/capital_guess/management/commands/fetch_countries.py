import requests
from django.core.management.base import BaseCommand
from capital_guess.models import Country

class Command(BaseCommand):
    help = 'Fetch country-capital data from API and populate the database'

    def handle(self, *args, **options):
        response = requests.get('https://countriesnow.space/api/v0.1/countries/capital')
        data = response.json()

        for country_data in data['data']:
            name = country_data['name']
            capital = country_data['capital']

            if capital:
                Country.objects.create(name=name, capital=capital)

        self.stdout.write(self.style.SUCCESS('Successfully fetched and populated country data.'))
