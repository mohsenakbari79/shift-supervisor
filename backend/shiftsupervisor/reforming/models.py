from django.db import models
from django.core.exceptions import ValidationError





class BaseUnitReforming(models.Model):
    date = models.DateField(null=True, blank=True, verbose_name='تاریخ')
    capacity_percent = models.FloatField(
        null=True,
        blank=True,
        verbose_name="Capacity (%)",
        help_text="Enter capacity percentage",
    )

    class Meta:
        abstract = True


class Unit100(BaseUnitReforming):
    # General Data

    feed_rate_t_hr = models.FloatField(
        null=True, blank=True, verbose_name="Feed Rate (t/hr)", help_text="34.1"
    )
    mav = models.FloatField(null=True, blank=True, verbose_name="MAV", help_text="<148")
    aromatic_content = models.FloatField(
        null=True, blank=True, verbose_name="Aromatic content (%)", help_text="MAX 70"
    )
    olefine_content = models.FloatField(
        null=True, blank=True, verbose_name="Olefine content (%)", help_text="MAX 20"
    )
    total_c4 = models.FloatField(
        null=True, blank=True, verbose_name="TOTAL C4", help_text="<7"
    )

    # Density Data
    density = models.FloatField(
        null=True, blank=True, verbose_name="DENSITY", help_text="Enter density value"
    )

    # Reactor Data
    r1001_inlet_temp = models.FloatField(
        null=True,
        blank=True,
        verbose_name="R-1001 Inlet Temp. [ºC]",
        help_text="60 ~ 120",
    )
    r1001_1st_bed_dt = models.FloatField(
        null=True,
        blank=True,
        verbose_name="R-1001 1st Bed ΔT [ºC]",
        help_text="55 ~ 60",
    )
    r1001_2nd_bed_dt = models.FloatField(
        null=True,
        blank=True,
        verbose_name="R-1001 2nd Bed ΔT [ºC]",
        help_text="40 ~ 50",
    )
    r1001_dp = models.FloatField(
        null=True, blank=True, verbose_name="R-1001 ΔP", help_text="3"
    )

    # C5 Cut Data
    c5_cut_rate_t_hr = models.FloatField(
        null=True, blank=True, verbose_name="C5 CUT: Rate (t/hr)", help_text="5.96"
    )

    # HYE Data
    hye_rate_t_hr = models.FloatField(
        null=True, blank=True, verbose_name="HYE: Rate (t/hr)", help_text="2.6"
    )
    flash_point = models.FloatField(
        null=True, blank=True, verbose_name="Flash Point [ºC]", help_text="> 60"
    )

    # MAV on T-1002
    mav_on_t1002_top = models.FloatField(
        null=True, blank=True, verbose_name="MAV on T-1002 Top", help_text="< 17"
    )

    # R-1002 Data
    r1002_inlet_temp = models.FloatField(
        null=True,
        blank=True,
        verbose_name="R-1002 Inlet Temp. [ºC]",
        help_text="290 ~ 320",
    )
    r1002_1st_bed_dt = models.FloatField(
        null=True,
        blank=True,
        verbose_name="R-1002 1st Bed ΔT [ºC]",
        help_text="15 ~ 50",
    )
    r1002_2nd_bed_dt = models.FloatField(
        null=True, blank=True, verbose_name="R-1002 2nd Bed ΔT [ºC]", help_text="MAX 13"
    )
    r1002_dp = models.FloatField(
        null=True, blank=True, verbose_name="R-1002 ΔP", help_text="2.5"
    )

    # E-1012 Data
    e1012_shell_side_dp = models.FloatField(
        null=True, blank=True, verbose_name="E-1012 Shell side ΔP", help_text="1.7"
    )
    e1012_tube_side_dp = models.FloatField(
        null=True, blank=True, verbose_name="E-1012 Tube side ΔP", help_text="1.2"
    )

    # HPYG Data
    hpyg_rate_t_hr = models.FloatField(
        null=True, blank=True, verbose_name="HPYG: Rate (t/hr)", help_text="25.2"
    )

    # Br.I Data
    br_i = models.FloatField(
        null=True, blank=True, verbose_name="Br.I (g/100ml)", help_text="< 100"
    )

    # TS Data
    ts_ppm = models.FloatField(
        null=True, blank=True, verbose_name="TS (ppm)", help_text="< 1"
    )

    def __str__(self):
        return f"Unit100 Data - Capacity: {self.capacity}%, Feed Rate: {self.feed_rate_t_hr} t/hr"


class Unit200(BaseUnitReforming):
    # General Data

    feed_from = models.FloatField(
        null=True, blank=True, verbose_name="Feed From", help_text="Phase, Tank"
    )
    t2001_t_hr = models.FloatField(
        null=True, blank=True, verbose_name="T-2001 [T/Hr]", help_text="568.182"
    )
    light_end_t_hr = models.FloatField(
        null=True, blank=True, verbose_name="LIGHT END [T/Hr]", help_text="25"
    )
    t2001_top_temp = models.FloatField(
        null=True, blank=True, verbose_name="T-2001 TOP TEMP [ºC]", help_text="95~105"
    )
    t2002_bottom_temp = models.FloatField(
        null=True,
        blank=True,
        verbose_name="T-2002 BOTTOM TEMP [ºC]",
        help_text="240~250",
    )
    t2002_t_hr = models.FloatField(
        null=True, blank=True, verbose_name="T-2002 [T/Hr]", help_text="423.441"
    )
    heart_cut_t_hr = models.FloatField(
        null=True, blank=True, verbose_name="Heart Cut [T/Hr]", help_text="234.822"
    )
    heavy_end_t_hr = models.FloatField(
        null=True, blank=True, verbose_name="Heavy End [T/Hr]", help_text="250.164"
    )
    heart_cut_c6_paraffins = models.FloatField(
        null=True,
        blank=True,
        verbose_name="Heart Cut C6 Paraffins <",
        help_text="0.113",
    )
    heart_cut_c10_plus = models.FloatField(
        null=True, blank=True, verbose_name="Heart Cut C10+ <", help_text="0.012"
    )
    heart_cut_olefine_percent = models.FloatField(
        null=True,
        blank=True,
        verbose_name="Heart Cut Olefine [%]",
        help_text="Enter percentage value",
    )
    hye_flash_point = models.FloatField(
        null=True,
        blank=True,
        verbose_name="HYE: FLASH POINT [ºC]",
        help_text="Min 60 ºC",
    )

    def __str__(self):
        return f"Unit200 Data - Capacity: {self.capacity}%, Feed From: {self.feed_from}"


class Unit250(BaseUnitReforming):
    
    feed_rate = models.FloatField(
        null=True, blank=True, verbose_name="FEED RATE [T/Hr]", help_text="234.822"
    )

    pph2 = models.FloatField(
        null=True, blank=True, verbose_name="PPH2", help_text=">8 bar"
    )
    reactor_inlet_temp = models.FloatField(
        null=True,
        blank=True,
        verbose_name="Reactor Inlet Temp [ºC]",
        help_text="270-320",
    )
    reactor_dt = models.FloatField(
        null=True, blank=True, verbose_name="Reactor ΔT", help_text="2~5"
    )
    reactor_dp = models.FloatField(verbose_name="Reactor ΔP", help_text="2")

    total_sulphur = models.FloatField(
        verbose_name="Total Sulphur [PPM]", help_text="≤0.5"
    )

    off_gas = models.FloatField(
        verbose_name="Off gas to FG / Flare / VG [t/hr]", help_text="1.707"
    )

    def __str__(self):
        return f"Unit250 Data - Capacity: {self.capacity} - Feed Rate: {self.feed_rate}"


class Unit300(BaseUnitReforming):
    # General Data
    feed_rate = models.FloatField(
        null=True, blank=True, verbose_name="FEED RATE [T/Hr]", help_text="233.64"
    )

    # Reactor Temperatures
    r_3001_temp = models.FloatField(
        null=True, blank=True, verbose_name="R-3001 Temp [ºC]", help_text="< 550"
    )
    r_3002_temp = models.FloatField(
        null=True, blank=True, verbose_name="R-3002 Temp [ºC]", help_text="< 550"
    )
    r_3003_temp = models.FloatField(
        null=True, blank=True, verbose_name="R-3003 Temp [ºC]", help_text="< 550"
    )
    r_3004_temp = models.FloatField(
        null=True, blank=True, verbose_name="R-3004 Temp [ºC]", help_text="< 550"
    )

    # ΔT Data
    dt_r1 = models.FloatField(
        null=True, blank=True, verbose_name="ΔT R1", help_text="< 103"
    )
    dt_r2 = models.FloatField(
        null=True, blank=True, verbose_name="ΔT R2", help_text="< 77"
    )
    dt_r3 = models.FloatField(
        null=True, blank=True, verbose_name="ΔT R3", help_text="< 61"
    )
    dt_r4 = models.FloatField(
        null=True, blank=True, verbose_name="ΔT R4", help_text="< 40"
    )

    # ΔP Data
    dp_r1 = models.FloatField(
        null=True, blank=True, verbose_name="ΔP R1", help_text="0.2"
    )
    dp_r2 = models.FloatField(
        null=True, blank=True, verbose_name="ΔP R2", help_text="0.2"
    )
    dp_r3 = models.FloatField(
        null=True, blank=True, verbose_name="ΔP R3", help_text="0.2"
    )
    dp_r4 = models.FloatField(
        null=True, blank=True, verbose_name="ΔP R4", help_text="0.2"
    )

    # Reformate and LPG Data
    reformate = models.FloatField(
        null=True, blank=True, verbose_name="REFORMATE [T/Hr]", help_text="213-209.7"
    )
    lpg = models.FloatField(
        null=True, blank=True, verbose_name="LPG [T/Hr]", help_text="9.6-10.6"
    )
    total_fuel_gas = models.FloatField(
        null=True, blank=True, verbose_name="TOTAL FUEL GAS [Nm3/h]", help_text="..."
    )

    # Component Data
    c6_paraffins_1 = models.FloatField(
        null=True, blank=True, verbose_name="C6 Paraffins <", help_text="0.112"
    )
    c10_plus_1 = models.FloatField(
        null=True, blank=True, verbose_name="C10+ <", help_text="0.012"
    )
    naphthenes_c6_c9 = models.FloatField(
        null=True, blank=True, verbose_name="Naphthenes C6N-C9N", help_text="0.1835"
    )
    total_aromatic = models.FloatField(
        null=True, blank=True, verbose_name="Total Aromatic (SP-25007)", help_text=">5%"
    )
    c6_paraffins_2 = models.FloatField(
        null=True, blank=True, verbose_name="C6 Paraffins", help_text="0.083"
    )
    c10_plus_2 = models.FloatField(
        null=True, blank=True, verbose_name="C10+", help_text="0.007"
    )
    outlet_olefine = models.FloatField(
        null=True, blank=True, verbose_name="Outlet Olefine", help_text="0.8-1.1%"
    )
    aromatic_content = models.FloatField(
        null=True, blank=True, verbose_name="Aromatic Content", help_text="0.782"
    )

    c6a = models.FloatField(null=True, blank=True, verbose_name="C6A", help_text="9.8")
    c7a = models.FloatField(null=True, blank=True, verbose_name="C7A", help_text="18.7")
    c8a = models.FloatField(null=True, blank=True, verbose_name="C8A", help_text="31.7")
    c9a = models.FloatField(null=True, blank=True, verbose_name="C9A", help_text="17.2")
    h2_hc_ratio = models.FloatField(
        null=True, blank=True, verbose_name="H2 / HC Ratio", help_text="2.5"
    )
    h2o = models.FloatField(
        null=True, blank=True, verbose_name="H2O", help_text="15~25 ppm"
    )
    hcl = models.FloatField(
        null=True, blank=True, verbose_name="HCL", help_text="1-2 ppm"
    )
    h2s = models.FloatField(
        null=True, blank=True, verbose_name="H2S (MAX)", help_text="0.5 ppm"
    )

    e_3001_hot_side_dp = models.FloatField(
        null=True, blank=True, verbose_name="E-3001 Hot side ΔP", help_text="0.6"
    )
    r_3005_inlet_temp = models.FloatField(
        null=True,
        blank=True,
        verbose_name="R-3005 Inlet Temp (°C)",
        help_text="150~170°C",
    )
    r_3005_dt = models.FloatField(
        null=True, blank=True, verbose_name="R-3005 ΔT", help_text="6"
    )
    r_3005_dp = models.FloatField(
        null=True, blank=True, verbose_name="R-3005 ΔP", help_text="3"
    )
    r_3005_press = models.FloatField(
        null=True, blank=True, verbose_name="R-3005 PRESS (bar)", help_text="24.5"
    )
    reactor_by_pass_valve_opening = models.FloatField(
        null=True,
        blank=True,
        verbose_name="Opening of Reactor By-Pass Valve (Thread)",
        help_text="0",
    )
    ft_3002_dp = models.FloatField(
        null=True, blank=True, verbose_name="FT-3002 ΔP", help_text="1"
    )
    ft_3002_ab = models.FloatField(
        null=True, blank=True, verbose_name="FT-3002 A, B", help_text="A,B"
    )

    def __str__(self):
        return f"Unit300 Data - Capacity: {self.capacity} - Feed Rate: {self.feed_rate}"


class Unit350(BaseUnitReforming):
    # no capacity
    
    # Basic Operation Data
    oxychlo_calci = models.FloatField(
        null=True,
        blank=True,
        verbose_name="OXYCHLO/CALCI ON or OFF",
        help_text="ON/OFF",
    )
    operation_mode = models.FloatField(
        null=True, blank=True, verbose_name="Operation Mode", help_text="B/C"
    )
    catalyst_transfer_velocity = models.FloatField(
        null=True,
        blank=True,
        verbose_name="Catalyst Transfer Medium Velocity (kg/hr)",
        help_text="1350 Kg/hr",
    )

    ft_3501 = models.FloatField(
        null=True, blank=True, verbose_name="FT-3501 (kg)", help_text="..."
    )
    ft_3502 = models.FloatField(
        null=True, blank=True, verbose_name="FT-3502 (kg)", help_text="..."
    )
    broken_catalyst = models.FloatField(
        null=True, blank=True, verbose_name="Broken Catalyst (kg)", help_text="..."
    )
    fine = models.FloatField(
        null=True, blank=True, verbose_name="Fine (kg)", help_text="..."
    )
    make_up_fresh_cat = models.FloatField(
        null=True,
        blank=True,
        verbose_name="Make Up Fresh Catalyst (Barrel)",
        help_text="...",
    )
    make_up_used_cat = models.FloatField(
        null=True,
        blank=True,
        verbose_name="Make Up Used Catalyst (Barrel)",
        help_text="...",
    )

    dt_1st_bed = models.FloatField(
        null=True, blank=True, verbose_name="ΔT 1st Bed", help_text="50~80"
    )
    dt_2nd_bed = models.FloatField(
        null=True, blank=True, verbose_name="ΔT 2nd Bed", help_text="30~50"
    )
    dt_checking_bed = models.FloatField(
        null=True, blank=True, verbose_name="ΔT Checking Bed", help_text="0~5"
    )

    dp_1st_bed = models.FloatField(
        null=True, blank=True, verbose_name="ΔP 1st Bed", help_text="..."
    )
    dp_2nd_bed = models.FloatField(
        null=True, blank=True, verbose_name="ΔP 2nd Bed", help_text="..."
    )
    dp_checking_bed = models.FloatField(
        null=True, blank=True, verbose_name="ΔP Checking Bed", help_text="..."
    )
    dp_oxy_calci = models.FloatField(
        null=True, blank=True, verbose_name="ΔP Oxy/Calci", help_text="..."
    )

    sp_cat_coke = models.FloatField(
        null=True, blank=True, verbose_name="SP. CAT COKE%", help_text="4-6% [MAX]"
    )
    chloride_1 = models.FloatField(
        null=True, blank=True, verbose_name="CHLORIDE %", help_text="1~1.1"
    )
    regn_cat_coke = models.FloatField(
        null=True, blank=True, verbose_name="REGN. CAT. COKE%", help_text="0.6~0.8"
    )
    chloride_2 = models.FloatField(
        null=True, blank=True, verbose_name="2nd CHLORIDE %", help_text="1~1.1"
    )

    d_3501_level = models.FloatField(
        null=True, blank=True, verbose_name="D-3501 Level %", help_text="..."
    )
    d_3503_level = models.FloatField(
        null=True, blank=True, verbose_name="D-3503 Level %", help_text="..."
    )
    d_3510_level = models.FloatField(
        null=True, blank=True, verbose_name="D-3510 Level %", help_text="..."
    )
    d_3512_level = models.FloatField(
        null=True, blank=True, verbose_name="D-3512 Level %", help_text="..."
    )
    d_3513_level = models.FloatField(
        null=True, blank=True, verbose_name="D-3513 Level %", help_text="..."
    )
    d_3514_level = models.FloatField(
        null=True, blank=True, verbose_name="D-3514 Level %", help_text="..."
    )

    tk_3501_level = models.FloatField(
        null=True, blank=True, verbose_name="TK-3501 LEVEL (mm)", help_text="..."
    )
    du_3504_level = models.FloatField(
        null=True, blank=True, verbose_name="DU-3504 LEVEL %", help_text="..."
    )
    d_3022_level = models.FloatField(
        null=True, blank=True, verbose_name="D-3022 LEVEL %", help_text="..."
    )

    h_3001_temp = models.FloatField(
        null=True, blank=True, verbose_name="H-3001 (TI-30001B)", help_text="<655"
    )
    h_3002_temp = models.FloatField(
        null=True, blank=True, verbose_name="H-3002 (TI-30007C)", help_text="<800"
    )
    h_3003_temp = models.FloatField(
        null=True, blank=True, verbose_name="H-3003 (TI-30012A)", help_text="<640"
    )
    h_3004_temp = models.FloatField(
        null=True, blank=True, verbose_name="H-3004 (TI-30017C)", help_text="<700"
    )

    def __str__(self):
        return f"Unit350 Data - Mode: {self.operation_mode} - OXYCHLO/CALCI: {self.oxychlo_calci}"



class DailyDataRaforming(models.Model):
    user = models.ForeignKey("accounts.Profile",on_delete=models.CASCADE,related_name="user_daily_reforming")
    date = models.DateField(verbose_name="تاریخ")
    unit100 = models.OneToOneField(Unit100, on_delete=models.CASCADE, null=True, blank=True, related_name="unit_100")
    unit200 = models.OneToOneField(Unit200, on_delete=models.CASCADE, null=True, blank=True, related_name="unit_200")
    unit250 = models.OneToOneField(Unit250, on_delete=models.CASCADE, null=True, blank=True, related_name="unit_250")
    unit300 = models.OneToOneField(Unit300, on_delete=models.CASCADE, null=True, blank=True, related_name="unit_300")
    unit350 = models.OneToOneField(Unit350, on_delete=models.CASCADE, null=True, blank=True, related_name="unit_350")
    
    def clean(self):
        """ چک کردن اینکه آیا تاریخ‌ها یکسان هستند """
        if self.Unit100 and self.Unit100.date != self.date:
            raise ValidationError("تاریخ U100 با تاریخ DailyData یکسان نیست.")
        if self.Unit200 and self.Unit200.date != self.date:
            raise ValidationError("تاریخ U200 با تاریخ DailyData یکسان نیست.")
        if self.Unit250 and self.Unit250.date != self.date:
            raise ValidationError("تاریخ U250 با تاریخ DailyData یکسان نیست.")
        if self.Unit300 and self.Unit300.date != self.date:
            raise ValidationError("تاریخ U300 با تاریخ DailyData یکسان نیست.")
        if self.Unit350 and self.Unit350.date != self.date:
            raise ValidationError("تاریخ U350 با تاریخ DailyData یکسان نیست.")

    def save(self, *args, **kwargs):
        """ قبل از ذخیره، روش clean را فراخوانی می‌کند """
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Daily Data for {self.date}"

