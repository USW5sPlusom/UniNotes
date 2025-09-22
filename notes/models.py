from django.db import models

class Note(models.Model):
    name = models.CharField(max_length=200, verbose_name='Введите заголовок')
    content = models.TextField(verbose_name='Введите текст', blank= True)
    subtag = models.CharField(max_length=200, verbose_name='Предмет')

    class Meta:
        pass
