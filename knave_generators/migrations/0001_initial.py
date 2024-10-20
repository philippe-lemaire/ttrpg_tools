# Generated by Django 4.2.4 on 2024-10-20 20:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Monster',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=120)),
                ('ac', models.IntegerField()),
                ('hp', models.IntegerField()),
                ('level', models.IntegerField()),
                ('attacks', models.CharField(max_length=200)),
                ('movement', models.CharField(max_length=200)),
                ('morale', models.CharField(max_length=100)),
                ('number_appearing', models.CharField(max_length=100)),
                ('extra_info', models.TextField(blank=True, max_length=2000, null=True)),
            ],
        ),
    ]
