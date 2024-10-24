# Generated by Django 5.1.2 on 2024-10-24 11:56

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
        ('px', '0002_alter_u400_bz_t_4001_bott_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='DailyDataPX',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='تاریخ')),
                ('u400_data', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='daily_data_u400', to='px.u400')),
                ('u700_data', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='daily_data_u700', to='px.u700')),
                ('u800_data', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='daily_data_u800', to='px.u800')),
                ('u950_data', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='daily_data_u950', to='px.u950')),
                ('u970_data', models.OneToOneField(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='daily_data_u970', to='px.u970')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_daily_px', to='accounts.profile')),
            ],
        ),
    ]
