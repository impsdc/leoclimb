# Generated by Django 3.1.1 on 2021-01-03 18:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appLeoClimb', '0012_auto_20201229_2301'),
    ]

    operations = [
        migrations.AlterField(
            model_name='partenaire',
            name='description',
            field=models.TextField(),
        ),
    ]