# Generated by Django 4.0.2 on 2022-02-26 18:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Teacher',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('contact_no', models.CharField(default='98xxxxxxxx', max_length=20)),
                ('department', models.CharField(blank=True, max_length=50, null=True)),
                ('profile', models.ImageField(blank=True, null=True, upload_to='profile/')),
                ('subject', models.BooleanField(blank=True, max_length=200, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='account.account')),
            ],
        ),
    ]
