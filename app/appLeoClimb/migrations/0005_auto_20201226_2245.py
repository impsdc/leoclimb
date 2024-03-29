# Generated by Django 3.1.1 on 2020-12-26 22:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appLeoClimb', '0004_auto_20201226_1911'),
    ]

    operations = [
        migrations.CreateModel(
            name='Palmare',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('update_at', models.DateTimeField(auto_now=True)),
                ('titre', models.CharField(max_length=50)),
                ('date', models.DateField()),
                ('image', models.FileField(blank=True, null=True, upload_to='palmares/')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.DeleteModel(
            name='Palmares',
        ),
        migrations.AddField(
            model_name='membre',
            name='menbre',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='appLeoClimb.palmare'),
        ),
    ]
