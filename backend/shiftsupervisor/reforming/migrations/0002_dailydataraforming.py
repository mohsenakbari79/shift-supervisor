# Generated by Django 5.1.2 on 2024-10-24 11:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('reforming', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='DailyDataRaforming',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='تاریخ')),
                ('unit100', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='unit_100', to='reforming.unit100')),
                ('unit200', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='unit_200', to='reforming.unit200')),
                ('unit250', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='unit_250', to='reforming.unit250')),
                ('unit300', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='unit_300', to='reforming.unit300')),
                ('unit350', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='unit_350', to='reforming.unit350')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_daily_reforming', to='accounts.profile')),
            ],
        ),
    ]
