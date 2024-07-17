from django.urls import include, path
from rest_framework import routers
from . import views

app_name = 'api'

router = routers.DefaultRouter()

urlpatterns = [
    path('', include(router.urls)),
    path('city-counts/', views.CityCountView.as_view(), name='city-counts'),
]