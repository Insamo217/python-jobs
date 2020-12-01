import requests
from bs4 import BeautifulSoup
from datetime import datetime
from django.core.management.base import BaseCommand
from parser_jobs.models import Category, Vacancies, Source


def get_html(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Linux; Android 6.0; Nexus 5 Build/MRA58N)'
    }
    try:
        res = requests.get(url, headers=headers)
        res.raise_for_status()
        return res.text

    except(requests.RequestException, ValueError):
        print('Сетевая ошибка')
        return False


def get_joblab_snippets():
    html = get_html\
        ('https://joblab.ru/search.php?srprofecy=&kw_w1=1&kw_w2=1&prof_bl=1%F1&srregion=50&srcity%5B%5D=170&srcity%5B%5D=35&srcity%5B%5D=100&srcity%5B%5D=78&srcity%5B%5D=234&srcity%5B%5D=79&srcity%5B%5D=65&srcity%5B%5D=66&srcategory%5B%5D=16&srzpmin=&srexpir%5B%5D=0&pred=7&r=vac&submit=1')
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        all_jobs = soup.findAll(class_="prof")
        for job in all_jobs:
            title = job.find('a').text
            url = job.find('a')['href']
            url_full = 'https://joblab.ru' + url
            save_vacancies = Vacancies(
                title=title,
                url=url_full,
                published=datetime.now(),
            ).save()


class Command(BaseCommand):
    help = 'Парсинг JobLab'

    def handle(self, *args, **options):
        a = get_joblab_snippets()
