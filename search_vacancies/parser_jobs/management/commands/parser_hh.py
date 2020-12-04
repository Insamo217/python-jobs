import requests
import json
from django.core.management.base import BaseCommand
from parser_jobs.models import Vacancies, Source


def get_hh_snippets(page = 0):
    params = {
        'text': 'NAME:Python',
        'experience': 'noExperience',
        'schedule': 'remote',
        'employment': 'full',
        'order_by': 'publication_time',
        'search_period': 30,
        'area': 1,
        'page': page,
        'per_page': 50
    }
    req = requests.get('https://api.hh.ru/vacancies', params)
    data = req.json()
    for i in data['items']:
        name = (i['name'])
        url = (i['alternate_url'])
        published = (i['created_at'])
        vacancies_exists = Vacancies.objects.filter(url=url).count()
        if not vacancies_exists:
            save_vacancies = Vacancies(
                title=name,
                url=url,
                published=published,
                source_id=2
            ).save()

            '''
            source_id=1 - Joblab.ru
            source_id=2 - HH.ru
            '''


class Command(BaseCommand):
    help = 'Парсинг HH'

    def handle(self, *args, **options):
        a = get_hh_snippets()