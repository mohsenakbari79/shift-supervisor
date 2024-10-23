# Generated by Django 5.1.2 on 2024-10-23 21:10

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='U500',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='تاریخ')),
                ('capacity_percent', models.FloatField(verbose_name='Capacity %')),
                ('t_5001_feed_rate', models.FloatField(help_text='126.88', verbose_name='T-5001[T/Hr]')),
                ('t_5002_feed_rate', models.FloatField(help_text='537.596', verbose_name='T-5002[T/Hr]')),
                ('raffinate', models.FloatField(help_text='47.808', verbose_name='Raffinate[T/Hr]')),
                ('bt_rate', models.FloatField(help_text='79.072', verbose_name='BT[T/Hr]')),
                ('bt_water_content', models.FloatField(help_text='<100', verbose_name='BT Water Content (ppm)')),
                ('bz_on_raffinate', models.CharField(help_text='<4%', max_length=10, verbose_name='Bz cont. on Raffinate')),
                ('nfm_on_raffinate', models.CharField(help_text='1~3ppm', max_length=10, verbose_name='NFM on RAFFINATE (ppm)')),
                ('morpholin_in_raffinate', models.FloatField(help_text='<50', verbose_name='Morpholin In Raffinate (ppm)')),
                ('na_in_bt', models.FloatField(help_text='<2%', verbose_name='N.A. in BT')),
                ('nfm_on_bt', models.CharField(help_text='1-3 ppm', max_length=10, verbose_name='NFM on BT (ppm)')),
                ('morpholin_in_bt', models.FloatField(help_text='<50', verbose_name='Morpholin In BT (ppm)')),
                ('total_lean_solvent', models.FloatField(help_text='432', verbose_name='Total Lean Solvent [M3/Hr]')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='U600',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='تاریخ')),
                ('capacity_percent', models.FloatField(verbose_name='Capacity %')),
                ('t_6001_feed_rate', models.FloatField(help_text='94.276', verbose_name='T-6001[T/Hr]')),
                ('t_6002_feed_rate', models.FloatField(help_text='174.24', verbose_name='T-6002[T/Hr]')),
                ('tk_6001_bt_from_sec_500', models.FloatField(help_text='80.954', verbose_name='TK-6001[T/Hr]+BT from SEC-500')),
                ('t_6003_feed_rate', models.FloatField(help_text='119.804', verbose_name='T-6003[T/Hr]')),
                ('bz_production_rate', models.FloatField(help_text='54.435', verbose_name='Bz production rate[T/Hr]')),
                ('r_6001_press', models.FloatField(help_text='28', verbose_name='R-6001 Press')),
                ('r_6001_temp', models.FloatField(help_text='360-480', verbose_name='R-6001 Temp (°C)')),
                ('r_6001_dp', models.FloatField(help_text='0.7', verbose_name='R-6001 ΔP')),
                ('r_6001_dt', models.FloatField(help_text='25', verbose_name='R-6001 ΔT')),
                ('benzene_purity', models.FloatField(help_text='0.999', verbose_name='Benzene Purity')),
                ('t_6002_non_aro_side_cut', models.FloatField(help_text='0.05(0.07ims)', verbose_name='T-6002 Non Aro% Side Cut')),
                ('r_6001_feed_non_aro', models.FloatField(help_text='<2%', verbose_name='R-6001 Feed Non Aro %')),
                ('t_6003_bott_non_aro', models.FloatField(help_text='0.0017', verbose_name='T-6003 Bott. Non Aro')),
                ('t_6003_toluene_bott', models.FloatField(help_text='0.1', verbose_name='T-6003 Toluene Bott. %')),
                ('conversion_rate', models.FloatField(help_text='47-49', verbose_name='Conversion Rate %')),
                ('xylene_yield', models.FloatField(help_text='21-23%', verbose_name='Xylene Yield')),
                ('h2_hc_ratio', models.FloatField(help_text='3 min', verbose_name='H2/HC Ratio')),
                ('water_content_recycle_gas', models.FloatField(help_text='10 ppm', verbose_name='Water Content (Recycle gas)')),
                ('d_6004_ـAB_inlet_temp', models.FloatField(help_text='150-200', verbose_name='D-6004A/B : Inlet Temp (°C)')),
                ('d_6004_A_dp', models.FloatField(help_text='...', verbose_name='D-6004A    ΔP')),
                ('d_6004_B_dp', models.FloatField(help_text='...', verbose_name='D-6004B   ΔP')),
                ('mx_production_rate', models.FloatField(verbose_name='MX Production Rate (T/Hr)')),
                ('br_i_in_clay_outlet', models.FloatField(help_text='10 max', verbose_name='Br.I in clay outlet')),
                ('compressor_hp_purge', models.FloatField(verbose_name='(Compressor HP Purge)(Nm3/hr)')),
                ('unit_600_recycle', models.FloatField(help_text='Sm3/hr', verbose_name='Unit 600 Recycle')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='U650',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(verbose_name='تاریخ')),
                ('capacity_percent', models.FloatField(verbose_name='Capacity %')),
                ('t_6501_feed_rate', models.FloatField(help_text='76.691', verbose_name='T-6501[T/Hr]')),
                ('t_6502_feed_rate', models.FloatField(help_text='114.046', verbose_name='T-6502[T/Hr]')),
                ('t_6503_feed_rate', models.FloatField(help_text='106.059', verbose_name='T-6503[T/Hr]')),
                ('conversion_rate', models.FloatField(help_text='80-87', verbose_name='Conversion Rate %')),
                ('xylene_yield', models.FloatField(help_text='31-35%', verbose_name='Xylene Yield')),
                ('r_6501_press', models.FloatField(help_text='28', verbose_name='R-6501 Press')),
                ('r_6501_temp', models.FloatField(help_text='360-472', verbose_name='R-6501 Temp (°C)')),
                ('r_6501_dp', models.FloatField(help_text='0.7', verbose_name='R-6501 ΔP')),
                ('r_6501_dt', models.FloatField(help_text='50', verbose_name='R-6501 ΔT')),
                ('t_6501_side_cut_c10', models.FloatField(help_text='0.25', verbose_name='T-6501 Side Cut C10+')),
                ('t_6503_toluene_bott', models.FloatField(help_text='0.05', verbose_name='T-6503 Bott. Toluene')),
                ('water_content_recycle_gas', models.FloatField(help_text='10 ppm', verbose_name='Water Content (Recycle Gas)')),
                ('heavy_aro', models.FloatField(help_text='2.009', verbose_name='Heavy Aro [T/Hr]')),
                ('h2_hc_ratio', models.FloatField(help_text='3 MIN', verbose_name='H2/HC Ratio')),
                ('d_6505_inlet_temp', models.FloatField(help_text='150-200', verbose_name='D-6505A/B : Inlet Temp')),
                ('d_6505_A_dp', models.FloatField(help_text='...', verbose_name='D-6505A    ΔP')),
                ('d_6505_B_dp', models.FloatField(help_text='...', verbose_name='D-6505B ΔP')),
                ('br_i_in_clay_outlet', models.FloatField(help_text='10 max', verbose_name='Br.I in clay outlet')),
                ('mx_production_rate', models.FloatField(help_text='Sm3/hr', verbose_name='Unit 650 Recycle')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
