# Generated by Django 3.1.1 on 2021-10-20 10:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appLeoClimb', '0020_auto_20210326_1707'),
    ]

    operations = [
        migrations.AddField(
            model_name='accueil',
            name='image',
            field=models.FileField(blank=True, null=True, upload_to='home/'),
        ),
        migrations.AddField(
            model_name='accueil',
            name='logo',
            field=models.FileField(blank=True, null=True, upload_to='home/'),
        ),
    ]