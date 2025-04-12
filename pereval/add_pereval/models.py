from django.db import models

# Create your models here.


class Status(models.Model):
    title = models.CharField(verbose_name='статус', max_length=30)


class Pereval_Added(models.Model):
    date_added = models.DateTimeField('время и дата', auto_now=True)
    raw_data = models.JSONField(verbose_name='json данные')
    images = models.JSONField(verbose_name='json изображение')
    status = models.OneToOneField(Status, verbose_name='статус записи', on_delete=models.CASCADE)


class Pereval_Areas(models.Model):
    id_parent = models.IntegerField(verbose_name='родительский id')
    title = models.CharField(verbose_name='название облости', max_length=30)


class Pereval_Images(models.Model):
    date_added = models.DateTimeField('время и дата', auto_now=True)
    img = models.ImageField()


class Spr_Activities_Types(models.Model):
    title = models.CharField(verbose_name='название пути', max_length=30)

