# Generated by Django 3.2 on 2023-03-22 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cats', '0004_auto_20230322_2351'),
    ]

    operations = [
        migrations.AddField(
            model_name='cat',
            name='achievements',
            field=models.ManyToManyField(through='cats.AchievementCat', to='cats.Achievement'),
        ),
    ]
