from . import views
from django.urls import path

app_name = 'weather'

urlpatterns = [
    path('', views.WeatherView.as_view(), name='index'),
]