# Generated by Django 4.0.2 on 2022-03-07 14:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='student',
            old_name='name',
            new_name='first_name',
        ),
        migrations.AddField(
            model_name='student',
            name='city',
            field=models.CharField(default='Nairobi', max_length=100),
        ),
        migrations.AddField(
            model_name='student',
            name='country',
            field=models.CharField(default='Kenya', max_length=100),
        ),
        migrations.AddField(
            model_name='student',
            name='last_name',
            field=models.CharField(default='', max_length=100),
        ),
    ]