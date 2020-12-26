# Generated by Django 3.1.1 on 2020-12-22 11:29

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('title', models.CharField(max_length=100)),
                ('main', models.TextField(max_length=255)),
                ('date', models.DateField()),
                ('image', models.FileField(blank=True, null=True, upload_to='actualite/')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]