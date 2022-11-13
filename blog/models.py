from django.db import models


# Create your models here.

class Post(models.Model):
    title = models.CharField("Заголовок: ", max_length=200)
    text = models.TextField("Текст поста: ", max_length=1000)
    date = models.DateField("Дата: ")

    def __str__(self):
        return self.title