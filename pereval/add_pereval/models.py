from django.db import models

# Create your models here.
new = 'NE'
pending = 'PE'
accepted = 'AC'
rejected = 'RE'

STAT = [
    (new, 'новая'),
    (pending, 'модератор взял в работу'),
    (accepted, 'модерация прошла успешно'),
    (rejected, 'модерация прошла, информация не принята'),
]


class User(models.Model):
    email = models.EmailField(primary_key=True)
    fam = models.CharField(max_length=35)
    name = models.CharField(max_length=35)
    otc = models.CharField(max_length=35)
    phone = models.CharField(max_length=35)


class Pereval(models.Model):
    beauty_title = models.CharField(max_length=35)
    title = models.CharField(max_length=35)
    other_titles = models.CharField(max_length=35)
    connect = models.TextField()
    add_time = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    status = models.CharField(max_length=2, choices=STAT)


class Coords(models.Model):
    latitude = models.FloatField()
    longitude = models.FloatField()
    height = models.FloatField()
    pereval = models.OneToOneField(Pereval, on_delete=models.CASCADE)


class Level(models.Model):
    winter = models.CharField(max_length=35)
    summer = models.CharField(max_length=35)
    autumn = models.CharField(max_length=35)
    spring = models.CharField(max_length=35)
    pereval = models.OneToOneField(Pereval, on_delete=models.CASCADE)


class Images(models.Model):
    data = models.URLField()
    title = models.CharField(max_length=35)
    pereval = models.ForeignKey(Pereval, related_name='images', on_delete=models.CASCADE)
