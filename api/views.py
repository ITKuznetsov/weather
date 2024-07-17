from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Count
from weather.models import SearchHistory
from weather.serializers import CityCountSerializer


class CityCountView(APIView):
    def get(self, request):
        city_counts = SearchHistory.objects.values('city').annotate(count=Count('city')).order_by('-count')
        serializer = CityCountSerializer(city_counts, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)