from django.db import models
from django.contrib.auth.models import User

from weather.utils import AbstractModel


class SearchHistory(AbstractModel):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    city = models.CharField(max_length=100)

    def __str__(self):
        return f"Пользователь: {self.user.username}, город: {self.city}"