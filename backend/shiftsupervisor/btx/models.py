from django.db import models
from django.core.exceptions import ValidationError


class BaseUnitBtx(models.Model):
    date = models.DateField(null=True, blank=True, verbose_name="تاریخ")
    capacity_percent = models.FloatField(
        null=True, blank=True, verbose_name="Capacity %"
    )

    class Meta:
        abstract = True

    def __str__(self):
        return f"Data on {self.date} with capacity {self.capacity_percent}%"


class U500(BaseUnitBtx):
    t_5001_feed_rate = models.FloatField(
        null=True, blank=True, verbose_name="T-5001[T/Hr]", help_text="126.88"
    )
    t_5002_feed_rate = models.FloatField(
        null=True, blank=True, verbose_name="T-5002[T/Hr]", help_text="537.596"
    )
    raffinate = models.FloatField(
        null=True, blank=True, verbose_name="Raffinate[T/Hr]", help_text="47.808"
    )
    bt_rate = models.FloatField(
        null=True, blank=True, verbose_name="BT[T/Hr]", help_text="79.072"
    )
    bt_water_content = models.FloatField(
        null=True, blank=True, verbose_name="BT Water Content (ppm)", help_text="<100"
    )
    bz_on_raffinate = models.CharField(
        max_length=10, verbose_name="Bz cont. on Raffinate", help_text="<4%"
    )
    nfm_on_raffinate = models.FloatField(
        null=True, blank=True, verbose_name="NFM on RAFFINATE (ppm)", help_text="1~3ppm"
    )
    morpholin_in_raffinate = models.FloatField(
        null=True,
        blank=True,
        verbose_name="Morpholin In Raffinate (ppm)",
        help_text="<50",
    )
    na_in_bt = models.FloatField(
        null=True, blank=True, verbose_name="N.A. in BT", help_text="<2%"
    )
    nfm_on_bt = models.FloatField(
        null=True, blank=True, verbose_name="NFM on BT (ppm)", help_text="1-3 ppm"
    )
    morpholin_in_bt = models.FloatField(
        null=True, blank=True, verbose_name="Morpholin In BT (ppm)", help_text="<50"
    )
    total_lean_solvent = models.FloatField(
        null=True,
        blank=True,
        verbose_name="Total Lean Solvent [M3/Hr]",
        help_text="432",
    )

    def __str__(self):
        return f"U-500 Operation on {self.date}"


class U600(BaseUnitBtx):
    t_6001_feed_rate = models.FloatField(
        null=True, blank=True, verbose_name="T-6001[T/Hr]", help_text="94.276"
    )
    t_6002_feed_rate = models.FloatField(
        null=True, blank=True, verbose_name="T-6002[T/Hr]", help_text="174.24"
    )
    tk_6001_bt_from_sec_500 = models.FloatField(
        null=True,
        blank=True,
        verbose_name="TK-6001[T/Hr]+BT from SEC-500",
        help_text="80.954",
    )
    t_6003_feed_rate = models.FloatField(
        null=True, blank=True, verbose_name="T-6003[T/Hr]", help_text="119.804"
    )
    bz_production_rate = models.FloatField(
        null=True,
        blank=True,
        verbose_name="Bz production rate[T/Hr]",
        help_text="54.435",
    )
    r_6001_press = models.FloatField(
        null=True, blank=True, verbose_name="R-6001 Press", help_text="28"
    )
    r_6001_temp = models.FloatField(
        null=True, blank=True, verbose_name="R-6001 Temp (°C)", help_text="360-480"
    )
    r_6001_dp = models.FloatField(
        null=True, blank=True, verbose_name="R-6001 ΔP", help_text="0.7"
    )
    r_6001_dt = models.FloatField(
        null=True, blank=True, verbose_name="R-6001 ΔT", help_text="25"
    )
    benzene_purity = models.FloatField(
        null=True, blank=True, verbose_name="Benzene Purity", help_text="0.999"
    )
    t_6002_non_aro_side_cut = models.FloatField(
        null=True,
        blank=True,
        verbose_name="T-6002 Non Aro% Side Cut",
        help_text="0.05(0.07ims)",
    )
    r_6001_feed_non_aro = models.FloatField(
        null=True, blank=True, verbose_name="R-6001 Feed Non Aro %", help_text="<2%"
    )
    t_6003_bott_non_aro = models.FloatField(
        null=True, blank=True, verbose_name="T-6003 Bott. Non Aro", help_text="0.0017"
    )
    t_6003_toluene_bott = models.FloatField(
        null=True, blank=True, verbose_name="T-6003 Toluene Bott. %", help_text="0.1"
    )
    conversion_rate = models.FloatField(
        null=True, blank=True, verbose_name="Conversion Rate %", help_text="47-49"
    )
    xylene_yield = models.FloatField(
        null=True, blank=True, verbose_name="Xylene Yield", help_text="21-23%"
    )
    h2_hc_ratio = models.FloatField(
        null=True, blank=True, verbose_name="H2/HC Ratio", help_text="3 min"
    )
    water_content_recycle_gas = models.FloatField(
        null=True,
        blank=True,
        verbose_name="Water Content (Recycle gas)",
        help_text="10 ppm",
    )
    d_6004_ـAB_inlet_temp = models.FloatField(
        null=True,
        blank=True,
        verbose_name="D-6004A/B : Inlet Temp (°C)",
        help_text="150-200",
    )
    d_6004_A_dp = models.FloatField(
        null=True, blank=True, verbose_name="D-6004A    ΔP", help_text="..."
    )
    d_6004_B_dp = models.FloatField(
        null=True, blank=True, verbose_name="D-6004B   ΔP", help_text="..."
    )
    mx_production_rate = models.FloatField(
        null=True, blank=True, verbose_name="MX Production Rate (T/Hr)", help_text=""
    )
    br_i_in_clay_outlet = models.FloatField(
        null=True, blank=True, verbose_name="Br.I in clay outlet", help_text="10 max"
    )
    compressor_hp_purge = models.FloatField(
        null=True,
        blank=True,
        verbose_name="(Compressor HP Purge)(Nm3/hr)",
        help_text="",
    )
    unit_600_recycle = models.FloatField(
        null=True, blank=True, verbose_name="Unit 600 Recycle", help_text="Sm3/hr"
    )

    def __str__(self):
        return f"U-600 Operation on {self.date}"


class U650(BaseUnitBtx):
    t_6501_feed_rate = models.FloatField(
        null=True, blank=True, verbose_name="T-6501[T/Hr]", help_text="76.691"
    )
    t_6502_feed_rate = models.FloatField(
        null=True, blank=True, verbose_name="T-6502[T/Hr]", help_text="114.046"
    )
    t_6503_feed_rate = models.FloatField(
        null=True, blank=True, verbose_name="T-6503[T/Hr]", help_text="106.059"
    )
    conversion_rate = models.FloatField(
        null=True, blank=True, verbose_name="Conversion Rate %", help_text="80-87"
    )
    xylene_yield = models.FloatField(
        null=True, blank=True, verbose_name="Xylene Yield", help_text="31-35%"
    )
    r_6501_press = models.FloatField(
        null=True, blank=True, verbose_name="R-6501 Press", help_text="28"
    )
    r_6501_temp = models.FloatField(
        null=True, blank=True, verbose_name="R-6501 Temp (°C)", help_text="360-472"
    )
    r_6501_dp = models.FloatField(
        null=True, blank=True, verbose_name="R-6501 ΔP", help_text="0.7"
    )
    r_6501_dt = models.FloatField(
        null=True, blank=True, verbose_name="R-6501 ΔT", help_text="50"
    )
    t_6501_side_cut_c10 = models.FloatField(
        null=True, blank=True, verbose_name="T-6501 Side Cut C10+", help_text="0.25"
    )
    t_6503_toluene_bott = models.FloatField(
        null=True, blank=True, verbose_name="T-6503 Bott. Toluene", help_text="0.05"
    )
    water_content_recycle_gas = models.FloatField(
        null=True,
        blank=True,
        verbose_name="Water Content (Recycle Gas)",
        help_text="10 ppm",
    )
    heavy_aro = models.FloatField(
        null=True, blank=True, verbose_name="Heavy Aro [T/Hr]", help_text="2.009"
    )
    h2_hc_ratio = models.FloatField(
        null=True, blank=True, verbose_name="H2/HC Ratio", help_text="3 MIN"
    )
    d_6505_inlet_temp = models.FloatField(
        null=True,
        blank=True,
        verbose_name="D-6505A/B : Inlet Temp",
        help_text="150-200",
    )
    d_6505_A_dp = models.FloatField(
        null=True, blank=True, verbose_name="D-6505A    ΔP", help_text="..."
    )
    d_6505_B_dp = models.FloatField(
        null=True, blank=True, verbose_name="D-6505B ΔP", help_text="..."
    )
    mx_production_rate = models.FloatField(
        null=True,
        blank=True,
        verbose_name="MX Production Rate (T/Hr)",
        help_text="64.984",
    )
    br_i_in_clay_outlet = models.FloatField(
        null=True, blank=True, verbose_name="Br.I in clay outlet", help_text="10 max"
    )
    mx_production_rate = models.FloatField(
        null=True, blank=True, verbose_name="Unit 650 Recycle", help_text="Sm3/hr"
    )

    def __str__(self):
        return f"U-650 Operation on {self.date}"




class DailyDataBtx(models.Model):
    user = models.ForeignKey("accounts.Profile",on_delete=models.CASCADE,related_name="user_daily_btx")
    date = models.DateField(verbose_name="تاریخ")
    u500_data = models.OneToOneField(U500, on_delete=models.CASCADE, null=True, blank=True, related_name="daily_data_u500")
    u600_data = models.OneToOneField(U600, on_delete=models.CASCADE, null=True, blank=True, related_name="daily_data_u600")
    u650_data = models.OneToOneField(U650, on_delete=models.CASCADE, null=True, blank=True, related_name="daily_data_u650")

    def clean(self):
        """ چک کردن اینکه آیا تاریخ‌ها یکسان هستند """
        if self.u500_data and self.u500_data.date != self.date:
            raise ValidationError("تاریخ U500 با تاریخ DailyData یکسان نیست.")
        if self.u600_data and self.u600_data.date != self.date:
            raise ValidationError("تاریخ U600 با تاریخ DailyData یکسان نیست.")
        if self.u650_data and self.u650_data.date != self.date:
            raise ValidationError("تاریخ U650 با تاریخ DailyData یکسان نیست.")

    def save(self, *args, **kwargs):
        """ قبل از ذخیره، روش clean را فراخوانی می‌کند """
        self.clean()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"Daily Data for {self.date}"