from django.views import View
from django.shortcuts import render

from common.views import TitleMixin, WeatherTitleMixin
from .forms import CityForm
from .utils import get_weather
from .models import SearchHistory

class WeatherView(WeatherTitleMixin, View):
    form_class = CityForm
    template_name = 'weather/index.html'
    title = 'Погода'
    
    def get(self, request):
        form = self.form_class()
        weather_data = None
        last_city = None

        if request.user.is_authenticated:
            last_city = SearchHistory.objects.filter(user=request.user).last()

        city = request.GET.get('city')
        if city:
            form = self.form_class(initial={'city': city})
            weather_data = get_weather(city)

        return render(request, self.template_name, {
            'form': form,
            'weather_data': weather_data,
            'last_city': last_city,
            'title': self.get_title()
        })

    def post(self, request):
        form = self.form_class(request.POST)
        last_city = None

        if request.user.is_authenticated:
            history = SearchHistory.objects.filter(user=request.user).order_by('-created_at')
            if history.count() > 1:
                last_city = history[1]

        if form.is_valid():
            city = form.cleaned_data['city']
            weather_data = get_weather(city)
            if request.user.is_authenticated:
                SearchHistory.objects.create(user=request.user, city=city)
                history = SearchHistory.objects.filter(user=request.user).order_by('-created_at')
                if history.count() > 1:
                    last_city = history[1]
            return render(request, self.template_name, {
                'form': form,
                'weather_data': weather_data,
                'last_city': last_city,
                'title': self.get_title()
            })
        return render(request, self.template_name, {
            'form': form,
            'last_city': last_city,
            'title': self.get_title()
        })
