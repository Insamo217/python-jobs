from django.contrib import admin
from .models import *
from .forms import VacanciesForm

#@admin.register(Vacancies)
#class VacanciesAdmin(admin.ModelAdmin):
    #list_display = ('pk', 'title', 'url', 'text', 'category', 'source')
    #form = VacanciesForm

admin.site.register(Vacancies)
admin.site.register(Category)
admin.site.register(Source)

