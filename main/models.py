# from django.db import models
from django.db import models
from django.contrib.auth.models import User


# class MoodEntry(models.Model):
#     mood = models.CharField(max_length=255)
#     time = models.DateField(auto_now_add=True)
#     feelings = models.TextField()
#     mood_intensity = models.IntegerField()
#     user = models.ForeignKey(User, on_delete=models.CASCADE)

#     @property
#     def is_mood_strong(self):
#         return self.mood_intensity >= 8


class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    description = models.TextField()
    category = models.CharField(max_length=50, null=True, blank=True)
    stock = models.IntegerField(default=0)
    image = models.ImageField(upload_to='products/', null=True, blank=True)

    def __str__(self):
        return self.name
    
