from django.shortcuts import render
from django.views.generic.base import View

from .models import *


class MainView(View):
    def get(self, request):
        return render(request, 'search_vacancies/index.html')


class JoblabView(View):
    def get(self, request):
        vacancies = Vacancies.objects.filter(source_id=1).order_by('-published')
        return render(request, 'search_vacancies/vacancies_list.html',
                      {'vacancies_list': vacancies})


class HHView(View):
    def get(self, request):
        vacancies = Vacancies.objects.filter(source_id=2).order_by('-published')
        return render(request, 'search_vacancies/vacancies_list.html',
                      {'vacancies_list': vacancies})


