# Generated by Django 4.0.2 on 2022-03-08 06:28

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0002_curriculum_status'),
    ]

    operations = [
        migrations.RenameField(
            model_name='curriculum',
            old_name='descrption',
            new_name='description',
        ),
    ]
