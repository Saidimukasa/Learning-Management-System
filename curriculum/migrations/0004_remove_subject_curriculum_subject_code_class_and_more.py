# Generated by Django 4.0.2 on 2022-03-08 15:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0003_rename_descrption_curriculum_description'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subject',
            name='curriculum',
        ),
        migrations.AddField(
            model_name='subject',
            name='code',
            field=models.CharField(default=1, max_length=10, unique=True),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('code', models.CharField(max_length=10, unique=True)),
                ('curriculum', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='curriculum.curriculum')),
            ],
        ),
        migrations.AddField(
            model_name='subject',
            name='c_class',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='curriculum.class'),
            preserve_default=False,
        ),
    ]
