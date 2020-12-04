from django.urls import path
from. import views


urlpatterns = [
    path('joblab/', views.JoblabView.as_view()),
    path('hh/', views.HHView.as_view()),
    path('', views.MainView.as_view()),
]