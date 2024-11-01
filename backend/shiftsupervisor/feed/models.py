from django.db import models

# Create your models here.

class Company(models.Model):
    name = models.CharField(max_length=40,null=True,blank=True)
    pnmme = models.CharField(max_length=40,null=True,blank=True)
    
class TankInventory(models.Model):
    company = models.ForeignKey("Company",on_delete=models.CASCADE)
    tank_name = models.CharField(max_length=10)
    description = models.CharField(max_length=20)
   

class CompanyFuelAnalysis(models.Model):
    company = models.ForeignKey(Company,on_delete=models.CASCADE,related_name='fuel_analysis')
    date = models.DateField(null=True, blank=True)
    c4 = models.FloatField(null=True, blank=True)
    c5 = models.FloatField(null=True, blank=True)
    c6 = models.FloatField(null=True, blank=True)
    
    
class TankOperation(models.Model):
    tank = models.ForeignKey("TankInventory", on_delete=models.CASCADE)
    company = models.ForeignKey("Company", on_delete=models.CASCADE)
    disconnect_time = models.TimeField(null=True, blank=True)  # زمان قطع
    connect_time = models.TimeField(null=True, blank=True)  # زمان وصل
    daily_total = models.FloatField(null=True, blank=True)  # مجموع دریافتی روزانه
    date = models.DateField(null=True, blank=True)
    def __str__(self):
        return f"Operation for {self.tank.tank_name} in {self.phasecompany.phase}"


class GlobalFuelAnalysis(models.Model):
    rvp = models.FloatField(null=True, blank=True)       # فیلد RVP
    ts_lte = models.FloatField(null=True, blank=True)    # فیلد TS-LTE

    def __str__(self):
        return f"Global Data - RVP: {self.rvp}, TS-LTE: {self.ts_lte}"
    
    



class Feed(models.Model):
    name = models.OneToOneField(
        "tanks.NameService",
        on_delete=models.CASCADE,
        unique=True,
        related_name = "feed"
    )    
    
    def __str__(self):
        return self.name

class FeedInventory(models.Model):
    feed = models.ForeignKey(Feed, on_delete=models.CASCADE,related_name="feed_report")
    date = models.DateField(auto_now_add=True, verbose_name="تاریخ")
    quantity = models.FloatField(verbose_name="مقدار (تن)")

    def __str__(self):
        return f"{self.get_feed_type_display()} - {self.quantity} تن در تاریخ {self.date}"
    
    
    
    

