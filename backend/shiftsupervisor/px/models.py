from django.db import models





class BaseUnitPx(models.Model):
    date = models.DateField(null=True, blank=True, verbose_name="تاریخ")
    capacity_percent = models.FloatField(
        null=True, blank=True, verbose_name="Capacity %"
    )

    class Meta:
        abstract = True

    def __str__(self):
        return f"Data on {self.date} with capacity {self.capacity_percent}%"


class U400(BaseUnitPx):
    feed_rate = models.FloatField(
        null=True, blank=True, verbose_name="FEED RATE [T/Hr]", help_text="646.858"
    )
    t_4001_feed_rate = models.FloatField(
        null=True, blank=True, verbose_name="T-4001[T/Hr]", help_text="238.26"
    )
    t_4002_total_feed_rate = models.FloatField(
        null=True, blank=True, verbose_name="T-4002[T/Hr] Total", help_text="375.2"
    )
    t_4003_total_feed_rate = models.FloatField(
        null=True, blank=True, verbose_name="T-4003[T/Hr] Total", help_text="144.8"
    )
    t_4004_feed_rate = models.FloatField(
        null=True, blank=True, verbose_name="T-4004[T/Hr]", help_text="46.079"
    )
    edf_feed_rate = models.FloatField(
        null=True, blank=True, verbose_name="EDF[T/Hr]", help_text="126.88"
    )
    non_aro_t_4002_top = models.FloatField(
        null=True, blank=True, verbose_name="Non Aro at T-4002 top", help_text="0.1"
    )
    non_aro_t_4003_top = models.FloatField(
        null=True, blank=True, verbose_name="Non Aro at T-4003 top", help_text="0.1"
    )
    c8a_t_4002_bott = models.FloatField(
        null=True, blank=True, verbose_name="C8A at T-4002 Bott", help_text="0.3"
    )
    c8a_t_4004_bott = models.FloatField(
        null=True, blank=True, verbose_name="C8A at T-4004 Bott", help_text="Nil"
    )
    non_aro_t_4001_bott = models.FloatField(
        null=True, blank=True, verbose_name="Non Aro at T-4001 Bott", help_text="0.3"
    )
    bz_t_4001_bott = models.FloatField(
        null=True, blank=True, verbose_name="BZ at T-4001 Bott", help_text="0"
    )
    tol_t_4001_bott = models.FloatField(
        null=True, blank=True, verbose_name="TOL at T-4001 Bott", help_text="0.4"
    )
    d_4005a_b_inlet_temp = models.FloatField(
        null=True,
        blank=True,
        verbose_name="D-4005A/B : Inlet Temp",
        help_text="170-199",
    )
    d_4005a_dp = models.FloatField(
        null=True, blank=True, verbose_name="D-4005A ΔP", help_text="1.5"
    )
    d_4005b_dp = models.FloatField(
        null=True, blank=True, verbose_name="D-4005B ΔP", help_text="1.5"
    )
    bri_clay_outlet_a = models.FloatField(
        null=True, blank=True, verbose_name="BrI in clay outlet(A)", help_text="10 max"
    )
    bri_clay_outlet_b = models.FloatField(
        null=True, blank=True, verbose_name="BrI in clay outlet(B)", help_text="10 max"
    )
    c8_aro_top_t_4001 = models.FloatField(
        null=True, blank=True, verbose_name="C8 ARO (Top T-4001) (%)", help_text="0.1"
    )
    c9_aro_top_t_4002 = models.FloatField(
        null=True, blank=True, verbose_name="C9 ARO (Top T-4002) (%)", help_text="0.05"
    )
    c9_aro_top_t_4003 = models.FloatField(
        null=True, blank=True, verbose_name="C9 ARO (Top T-4003) (%)", help_text="0.05"
    )
    ox_production_rate = models.FloatField(
        null=True, blank=True, verbose_name="OX PRODUCTION RATE T/h", help_text="12.626"
    )
    non_aro_on_ox = models.FloatField(
        null=True, blank=True, verbose_name="Non Aro. On OX", help_text="1% IMS"
    )
    ox_purity = models.FloatField(
        null=True, blank=True, verbose_name="OX PURITY(%)", help_text="0.985"
    )

    def __str__(self):
        return f"U-400 Operation on {self.date}"


class U700(BaseUnitPx):
    tuning_status = models.CharField(
        max_length=100, verbose_name="Tuning Status", help_text="New Setpoint"
    )
    feed_t_7001_a_b = models.FloatField(
        null=True, blank=True, verbose_name="FEED T-7001 A/B T/H", help_text="426.57"
    )
    bri_feed_to_t_7001a_b = models.FloatField(
        null=True,
        blank=True,
        verbose_name="Br.I in Feed to T-7001A/B",
        help_text="MAX 10",
    )
    t_7001a_temp = models.FloatField(
        null=True, blank=True, verbose_name="T-7001A/B Temp.[ ºc]", help_text="175"
    )
    t_7001a_dp = models.FloatField(
        null=True,
        blank=True,
        verbose_name="T-7001A ΔP( MAX) Within 24 Hour",
        help_text="MAX 4.5",
    )
    t_7001b_dp = models.FloatField(
        null=True,
        blank=True,
        verbose_name="T-7001B ΔP(MAX) Within 24 Hour",
        help_text="MAX 4.5",
    )
    water_injection = models.FloatField(
        null=True, blank=True, verbose_name="Water injection (Kg/Hr)", help_text="100"
    )
    water_feed_ppm = models.FloatField(
        null=True, blank=True, verbose_name="Water: Feed [ ppm]", help_text="max 40"
    )
    water_desorbent_ppm = models.FloatField(
        null=True,
        blank=True,
        verbose_name="Water: Desorbent [ ppm]",
        help_text="MAx 140 ppm",
    )
    water_raff_ppm = models.FloatField(
        null=True,
        blank=True,
        verbose_name="Water: Raff [ ppm]",
        help_text="MAx 100 ppm",
    )
    px_on_raffinate = models.FloatField(
        null=True, blank=True, verbose_name="Px on Raffinate:", help_text="0.005"
    )
    px_rate = models.FloatField(
        null=True, blank=True, verbose_name="Px Rate[T/Hr.]", help_text="94.205"
    )
    tol_rate = models.FloatField(
        null=True, blank=True, verbose_name="TOL Rate[T/Hr.]", help_text="1.881"
    )
    px_purity = models.FloatField(
        null=True, blank=True, verbose_name="PURITY OF PX", help_text="99.7"
    )
    pdeb_in_px_prod = models.FloatField(
        null=True, blank=True, verbose_name="PDEB In:PX Prod.", help_text="0"
    )
    pdeb_in_side_cut = models.FloatField(
        null=True, blank=True, verbose_name="PDEB In: Side Cut:", help_text="0"
    )
    make_up_recycle_pdeb_purity = models.FloatField(
        null=True,
        blank=True,
        verbose_name="Make up/ Recycle PDEB Purity",
        help_text=">98%wt",
    )
    recovery_of_px = models.FloatField(
        null=True, blank=True, verbose_name="Recovery of PX", help_text="%"
    )

    def __str__(self):
        return f"U-700 Operation on {self.date}"


class U800(BaseUnitPx):
    feed_rate = models.FloatField(
        null=True,
        blank=True,
        verbose_name="Reaction Feed Flow(T/hr)",
        help_text="334.5",
    )
    t_8001_bottom_px_percent = models.FloatField(
        null=True, blank=True, verbose_name="T-8001 Bottom, PX%", help_text="0.2257"
    )
    recycle_flow_nm3_hr = models.FloatField(
        null=True, blank=True, verbose_name="Recycle Flow [NM3/HR]", help_text="344833"
    )
    t_8001_aro_rec = models.FloatField(
        null=True,
        blank=True,
        verbose_name="T-8001[T/Hr.](ARO+Rec)",
        help_text="335.762",
    )
    feed_to_r_8001_px_percent = models.FloatField(
        null=True, blank=True, verbose_name="Feed to R-8001, Px%", help_text="0.012"
    )
    feed_to_r_8001_h2_purity = models.FloatField(
        null=True,
        blank=True,
        verbose_name="Feed to R-8001 :H2  Purity",
        help_text="51% MOL",
    )
    r_8001_inlet_temp = models.FloatField(
        null=True,
        blank=True,
        verbose_name="R-8001 Inlet Temp[ ºc]",
        help_text="374-379",
    )
    r_8001_delta_t = models.FloatField(
        null=True, blank=True, verbose_name="R-8001 ΔT", help_text="5"
    )
    h2_hc_ratio = models.FloatField(
        null=True, blank=True, verbose_name="H2/HC RATIO", help_text="2.5~3"
    )
    r_8001_pressure = models.FloatField(
        null=True, blank=True, verbose_name="R-8001 P", help_text="9 BAR"
    )
    r_8001_dp = models.FloatField(
        null=True, blank=True, verbose_name="R-8001 ΔP", help_text="0.6"
    )
    eb_conversion = models.FloatField(
        null=True, blank=True, verbose_name="EB Conversion", help_text="0.645"
    )
    d_8004a_b_inlet_temp = models.FloatField(
        null=True,
        blank=True,
        verbose_name="D-8004A/B : Inlet Temp",
        help_text="170-200",
    )
    d_8004a_dp = models.FloatField(
        null=True, blank=True, verbose_name="D-8004A ΔP", help_text="1.5"
    )
    d_8004b_dp = models.FloatField(
        null=True, blank=True, verbose_name="D-8004B ΔP", help_text="1.5"
    )
    bri_clay_outlet_max = models.FloatField(
        null=True, blank=True, verbose_name="Br.I in clay outlet", help_text="10 MAX"
    )
    unit_800_recycle = models.FloatField(
        null=True, blank=True, verbose_name="Unit 800  Recycle", help_text="Sm3/hr"
    )

    def __str__(self):
        return f"U-800 Operation on {self.date}"


class U950(BaseUnitPx):
    feed_rate = models.FloatField(
        null=True, blank=True, verbose_name="FEED RATE [T/Hr]", help_text="113"
    )
    reactor_inlet_temp = models.FloatField(
        null=True, blank=True, verbose_name="Reactor Inlet Temp [ ºc]", help_text="260"
    )
    r_9501_pressure = models.FloatField(
        null=True, blank=True, verbose_name="R-9501 Pressure(bar)", help_text="28.7"
    )
    reactor_delta_t = models.FloatField(
        null=True, blank=True, verbose_name="Reactor ΔT", help_text="14"
    )
    reactor_dp = models.FloatField(
        null=True, blank=True, verbose_name="Reactor ΔP", help_text="2"
    )
    recycle_flow_nm3_hr = models.FloatField(
        null=True, blank=True, verbose_name="Recycle Flow [NM3/HR]", help_text="29000"
    )
    feed_to_r_9501_h2_purity = models.FloatField(
        null=True, blank=True, verbose_name="Feed To R-9501 H2 Purity", help_text="80"
    )
    off_gas = models.CharField(
        max_length=50,
        verbose_name="Off gas to FG / Flare/ VG",
        help_text="str",
        blank=True,
        null=True,
    )
    h2_hc_ratio_min = models.FloatField(
        null=True, blank=True, verbose_name="H2/HC Ratio", help_text="MIN 0.6"
    )
    product_total_sulphur_ppm = models.FloatField(
        null=True,
        blank=True,
        verbose_name="Product Total Sulphur[PPM]",
        help_text="300 ppm(ims)",
    )
    light_end_product_t_hr = models.FloatField(
        null=True, blank=True, verbose_name="Light End product[T/Hr]", help_text="107.5"
    )

    def __str__(self):
        return f"U-950 Operation on {self.date}"


class U970(BaseUnitPx):
    feed_rate = models.FloatField(
        null=True, blank=True, verbose_name="FEED RATE [T/Hr]", help_text="150"
    )
    light_lte_product_t_hr = models.FloatField(
        null=True, blank=True, verbose_name="Light LTE Product [T/Hr]", help_text="105"
    )
    heavy_lte_product_t_hr = models.FloatField(
        null=True, blank=True, verbose_name="Heavy LTE Product [T/Hr]", help_text="45"
    )
    heavy_lte_rvp_psia = models.FloatField(
        null=True, blank=True, verbose_name="Heavy LTE RVP [Psia]", help_text="8~10"
    )
    t_9701_bottom_temp = models.FloatField(
        null=True, blank=True, verbose_name="T-9701 Bottom Temp.[ ºC]", help_text="..."
    )
    bz_hlte_percent = models.FloatField(
        null=True, blank=True, verbose_name="BZ (HLTE)", help_text="%"
    )

    def __str__(self):
        return f"U-970 Operation on {self.date}"





class DailyDataPX(models.Model):
    user = models.ForeignKey("accounts.Profile",on_delete=models.CASCADE,related_name="user_daily_px")
    date = models.DateField(verbose_name="تاریخ")
    u400_data = models.OneToOneField(U400, on_delete=models.CASCADE, null=True, blank=True, related_name="daily_data_u400")
    u700_data = models.OneToOneField(U700, on_delete=models.CASCADE, null=True, blank=True, related_name="daily_data_u700")
    u800_data = models.OneToOneField(U800, on_delete=models.CASCADE, null=True, blank=True, related_name="daily_data_u800")
    u950_data = models.OneToOneField(U950, on_delete=models.CASCADE, null=True, blank=True, related_name="daily_data_u950")
    u970_data = models.OneToOneField(U970, on_delete=models.CASCADE, null=True, blank=True, related_name="daily_data_u970")

    def clean(self):
        """ چک کردن اینکه آیا تاریخ‌ها یکسان هستند """
        if self.u400_data and self.u400_data.date != self.date:
            raise ValidationError("تاریخ U400 با تاریخ DailyData یکسان نیست.")
        if self.u700_data and self.u700_data.date != self.date:
            raise ValidationError("تاریخ U700 با تاریخ DailyData یکسان نیست.")
        if self.u800_data and self.u800_data.date != self.date:
            raise ValidationError("تاریخ U800 با تاریخ DailyData یکسان نیست.")
        if self.u950_data and self.u950_data.date != self.date:
            raise ValidationError("تاریخ U950 با تاریخ DailyData یکسان نیست.")
        if self.u970_data and self.u970_data.date != self.date:
            raise ValidationError("تاریخ U970 با تاریخ DailyData یکسان نیست.")

    def save(self, *args, **kwargs):
        """ قبل از ذخیره، روش clean را فراخوانی می‌کند """
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Daily Data for {self.date}"