# Generated by Django 5.2 on 2025-04-18 11:29

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pereval',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('beauty_title', models.CharField(max_length=35)),
                ('title', models.CharField(max_length=35)),
                ('other_titles', models.CharField(max_length=35)),
                ('connect', models.TextField()),
                ('add_time', models.DateTimeField(auto_now=True)),
                ('status', models.CharField(choices=[('NE', 'новая'), ('PE', 'модератор взял в работу'), ('AC', 'модерация прошла успешно'), ('RE', 'модерация прошла, информация не принята')], max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('email', models.EmailField(max_length=254, primary_key=True, serialize=False)),
                ('fam', models.CharField(max_length=35)),
                ('name', models.CharField(max_length=35)),
                ('otc', models.CharField(max_length=35)),
                ('phone', models.CharField(max_length=35)),
            ],
        ),
        migrations.CreateModel(
            name='Level',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('winter', models.CharField(max_length=35)),
                ('summer', models.CharField(max_length=35)),
                ('autumn', models.CharField(max_length=35)),
                ('spring', models.CharField(max_length=35)),
                ('pereval', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='add_pereval.pereval')),
            ],
        ),
        migrations.CreateModel(
            name='Images',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.URLField()),
                ('title', models.CharField(max_length=35)),
                ('pereval', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='images', to='add_pereval.pereval')),
            ],
        ),
        migrations.CreateModel(
            name='Coords',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField()),
                ('longitude', models.FloatField()),
                ('height', models.FloatField()),
                ('pereval', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='add_pereval.pereval')),
            ],
        ),
        migrations.AddField(
            model_name='pereval',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='add_pereval.user'),
        ),
    ]
