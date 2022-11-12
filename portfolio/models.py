from django.db import models


class Project(models.Model):
    title = models.CharField('Заголовок', max_length=100)
    description = models.CharField('Описание', max_length=250)
    image = models.ImageField('Загрузить изображение', upload_to='portfolio/images/')
    url = models.URLField('Ссылка', blank=True)
