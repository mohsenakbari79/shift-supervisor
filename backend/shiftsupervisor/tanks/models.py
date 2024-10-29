from django.db import models

# Create your models here.
class AdditionalServices(models.Model):
    name = models.charfield(max_length=50)
    description = models.CharField(max_length=100,null=True, blank=True)
    
    def __str__(self):
        return self.name
    
class ServiceConsumedAndShippedDaily(models.Model):
    additionalServices  = models.ForeignKey(Product, on_delete=models.CASCADE)
    shippedaily = models.FloatField(defualt=0,null=True, blank=True)
    # Consumed
    date = models.DateField(verbose_name="تاریخ")
    pass
    

class Product(models.Model):
    name = models.charfield(max_length=50)
    description = models.CharField(max_length=100,null=True, blank=True)
    
    
class ProductProducedAndShippeDaily(models):
    product  = models.ForeignKey(Product, on_delete=models.CASCADE)
    produced = models.FloatField(defualt=0,null=True, blank=True)
    shippedaily = models.FloatField(defualt=0,null=True, blank=True)

    date = models.DateField(verbose_name="تاریخ")

    pass

class ProductCombination(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    loading = ProductProducedAndShippeDaily(ProductProducedAndShippeDaily,on_delete=models.CASCADE,null=True, blank=True)
    quantity = models.FloatField(defualt=0)
    
    pass
 

class Tanker(models.Medel):
    name = models.CharField(max_length=50)
    quantity = models.IntgerField(verbose_name="quantity",defualt=0)
    weight = models.FloatField(defualt=0)
    pass



class CargoLoading(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    ship_quantity = models.FloatField(null=True, blank=True, verbose_name="Ship Quantity")
    truck_quantity = models.FloatField(null=True, blank=True, verbose_name="Truck Quantity")
    tanker = models.ForeignKey(Tanker, on_delete=models.CASCADE, null=True, blank=True)
    tanker_quantity = models.FloatField(null=True, blank=True, verbose_name="Tanker Quantity")
    total_quantity = models.IntegerField(verbose_name="Total Quantity", default=0)

    def clean(self):
        """Ensure only one type of loading (ship, truck, or tanker) is used."""
        quantities = [self.ship_quantity, self.truck_quantity, self.tanker_quantity]
        non_null_quantities = [q for q in quantities if q is not None]

        # بررسی اینکه فقط یکی از فیلدهای بارگیری پر شده باشد
        if len(non_null_quantities) != 1:
            raise ValidationError("Exactly one of 'ship_quantity', 'truck_quantity', or 'tanker_quantity' must be specified.")

        # اگر تانکر انتخاب شده باشد، مقدار بارگیری تانکر باید مشخص شود
        if self.tanker and self.tanker_quantity is None:
            raise ValidationError("Tanker quantity must be specified if a tanker is selected.")

    def __str__(self):
        if self.ship_quantity:
            return f"{self.product.name} - Ship: {self.ship_quantity}"
        elif self.truck_quantity:
            return f"{self.product.name} - Truck: {self.truck_quantity}"
        elif self.tanker:
            return f"{self.product.name} - Tanker: {self.tanker.name} - Quantity: {self.tanker_quantity}"
        else:
            return f"{self.product.name} - Total: {self.total_quantity}"


class Combinations(models.Model):
    # F:product
    # subproduct manytoone
    pass


class Tank(models.Model):
    TANK_TYPES = [
        ('feed', 'مخازن خوراک و محصولات فرعی'),
        ('intermediate', 'مخازن میانی و حلال'),
        ('main', 'مخازن محصولات اصلی'),
        ('other', 'سایر مخازن'),
    ]

    name = models.CharField(max_length=100, verbose_name="نام مخزن")
    tank_type = models.CharField(max_length=20, choices=TANK_TYPES, verbose_name="نوع مخزن")
    capacity = models.FloatField(verbose_name="ظرفیت مخزن (تن)")

    def __str__(self):
        return f"{self.name} - {self.get_tank_type_display()}"

class TankInventory(models.Model):
    tank = models.ForeignKey(Tank, on_delete=models.CASCADE, related_name='inventories')
    produced = models.ForeignKey(Product,on_delete=models.CASCADE,verbose_name="مقدار تولید (تن)", null=True, blank=True)
    service = models.ForeignKey(AdditionalServices,on_delete=models.CASCADE,verbose_name="مصرف سرویس (تن)", null=True, blank=True)
    inventory = models.FloatField(verbose_name="موجودی (تن)", null=True, blank=True)
    percentage = models.FloatField(verbose_name="درصد موجودی", null=True, blank=True)  # فقط برای مخازن سایر
    date = models.DateField(auto_now_add=True, verbose_name="تاریخ")

    def clean(self):
        """اعتبارسنجی بر اساس نوع مخزن"""
        if self.tank.tank_type == 'other' and self.percentage is None:
            raise ValidationError("برای مخازن 'سایر' باید درصد موجودی مشخص شود.")
        if self.tank.tank_type != 'other' and self.percentage is not None:
            raise ValidationError("درصد موجودی فقط برای مخازن 'سایر' معتبر است.")

    def __str__(self):
        return f"Inventory of {self.tank.name} on {self.date}"
    
    pass



class Feed(models.Model):
    FEED_TYPES = [
        ('gas_condensate', 'میعانات گازی'),
        ('raw_pyrolysis_gasoline', 'بنزین پیرولیز خام'),
    ]

    date = models.DateField(auto_now_add=True, verbose_name="تاریخ")
    feed_type = models.CharField(max_length=30, choices=FEED_TYPES, verbose_name="نوع خوراک")
    quantity = models.FloatField(verbose_name="مقدار (تن)")

    def __str__(self):
        return f"{self.get_feed_type_display()} - {self.quantity} تن در تاریخ {self.date}"
    
    
    
    

class FeedReception(models.Model):
    feed = models.ForeignKey(Feed, on_delete=models.CASCADE, verbose_name="نوع خوراک")
    tank = models.ForeignKey(Tank, on_delete=models.SET_NULL, null=True, verbose_name="تانک")
    phase = models.CharField(max_length=50, verbose_name="فاز", null=True, blank=True)
    date = models.DateField(auto_now_add=True, verbose_name="تاریخ دریافت")
    daily_total = models.FloatField(default=0, verbose_name="جمع روزانه (تن)")
    monthly_total = models.FloatField(default=0, verbose_name="جمع ماهانه (تن)")
    connect_time = models.TimeField(null=True, blank=True, verbose_name="زمان وصل")
    disconnect_time = models.TimeField(null=True, blank=True, verbose_name="زمان قطع")

    def __str__(self):
        return f"{self.feed} - {self.tank or 'بدون تانک'} - {self.date}"