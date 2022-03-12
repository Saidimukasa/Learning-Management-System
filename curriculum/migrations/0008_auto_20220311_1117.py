# Generated by Django 3.2.7 on 2022-03-11 08:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0007_auto_20220311_1054'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='resource',
        ),
        migrations.AddField(
            model_name='resource',
            name='subject',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='curriculum.subject'),
            preserve_default=False,
        ),
    ]
