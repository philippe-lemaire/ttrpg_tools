# Generated by Django 4.2.4 on 2025-07-03 07:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ose', '0002_alter_monster_source_alter_monster_treasure_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='monster',
            name='attacks',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
