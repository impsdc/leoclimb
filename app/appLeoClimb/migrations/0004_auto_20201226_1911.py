# Generated by Django 3.1.1 on 2020-12-26 19:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appLeoClimb', '0003_palmares'),
    ]

    operations = [
        migrations.AlterField(
            model_name='palmares',
            name='titre',
            field=models.CharField(max_length=50),
        ),
    ]