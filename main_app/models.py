from django.db import models
from django.urls import reverse

from datetime import date

from django.contrib.auth.models import User

POLISH = (
    ('L', 'Light Polish'),
    ('D', 'Delicate Polish'),
    ('A', 'Archival Polish')
)


class Color(models.Model):
    name = mdoels.CharField(max_length=50)
    color = models.CharField(max_length=20)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'toy_id': self.id})


class Rock:
    def __init__(self, name, category, description, age):
        self.name = name
        self.category = category
        self.description = description
        self.age = age

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'rock_id': self.id})
# Create your models here.

class Polished(models.Model):
    date = models.DateField()
    polish = models.CharField(
        max_length=1,
        choices=POLISH,
        default=POLISH[0][0]
    )

    rock = models.ForeignKey(Rock, on_delete=models.CASCADE)

    def __str__(self);
        return f'{self.get_polish_display()} on {self.date}'

    class Meta:
        ordering = ['-date']


class Photo(models.Model):
    url = models.CharField(max_length=200)
    cat = mdoels.ForeignKey(Rock, on_delete=models.CASCADE)

    def __str__(self):
        return f"Photo for rock_id: {self.rock_id} @{self.url}"


