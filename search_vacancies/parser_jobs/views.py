from django.shortcuts import render
from django.views.generic.base import View

from .models import *


class VacancyView(View):
    def get(self, request):
        vacancies = Vacancies.objects.filter().order_by('-published')
        return render(request, 'search_vacancies/vacancies_list.html',
                      {'vacancies_list': vacancies})


