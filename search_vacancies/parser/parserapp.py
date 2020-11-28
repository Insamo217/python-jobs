import requests
from bs4 import BeautifulSoup


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
        all_jobs1 = soup.findAll('div', class_="small")
        all_jobs = soup.findAll(class_="prof")
        for job in all_jobs:
            title = job.find('a').text
            url = job.find('a')['href']
            url1 = 'https://joblab.ru' + url
            print(title)
            print(url1)
        for job1 in all_jobs1:
            published = job1.text
            print(published)

'''
def get_joblab_text():
    html = get_html('https://joblab.ru/vac7689229.html')
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        all_jobs = soup.findAll(class_="prof")
        for job in all_jobs:
            title = job.find('a').text
            url = job.find('a')['href']
            url1 = 'https://joblab.ru' + url
            print(title)
            print(url1)


def get_hh():
    html = get_html('https://hh.ru/search/vacancy?st=searchVacancy&text=Python&area=1&salary=&currency_code=RUR&experience=noExperience&schedule=remote&order_by=relevance&search_period=0&items_on_page=50&no_magic=true&L_save_area=true&from=suggest_post')
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        all_jobs = soup.findAll(class_="bloko-link HH-LinkModifier")
        print(all_jobs)
        for job in all_jobs:
            #title = job.find('a')
            url = job.find('a')['href']
            #url1 = 'https://joblab.ru' + url
            #print(title)
            print(url)

def get_geekjob():
    html = get_html('https://geekjob.ru/vacancies?rm=1&t=2,3,276,277,308')
    if html:
        soup = BeautifulSoup(html, 'html.parser')
        all_jobs = soup.findAll('required')
        print(all_jobs)
        #for job in all_jobs:
            #title = job.find('a').text
            #url = job.find('a')['href']
            #url1 = 'https://joblab.ru' + url
            #print(title)
            #print(url1)
'''


if __name__ == '__main__':
    get_joblab_snippets()
