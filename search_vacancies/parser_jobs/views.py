from django.shortcuts import render
from django.views.generic.base import View

from .models import *


class VacancyView(View):
    def get(self, request):
        vacancy = Vacancies.objects.all()
        return render(request, 'search_vacancies/vacancy_list.html', {'vacancy_list': vacancy})


