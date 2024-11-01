from django.db import models


class NameService(models.Model):
    name = models.CharField(max_length=20, unique=True)
    ename = models.CharField(max_length=50, null=True,blank=True)
    pname = models.CharField(max_length=50, null=True,blank=True)
    comment =models.CharField(max_length=100, null=True,blank=True)



# Create your models here.
class AdditionalServices(models.Model):
    name = models.OneToOneField(
        NameService,
        on_delete=models.CASCADE,
        unique=True,
        related_name = "service"
    )    
    related_name = "servicename"
    
    def __str__(self):
        return self.name
    
class ServiceConsumedAndShippedDaily(models.Model):
    additionalServices  = models.ForeignKey(AdditionalServices, on_delete=models.CASCADE,related_name="service_report")
    shippedaily = models.FloatField(default=0, null=True, blank=True)
    # Consumed
    date = models.DateField(verbose_name="تاریخ")
    pass
    

class Product(models.Model):
    parent_product = models.ForeignKey(
        'self',  # Self-referential ForeignKey for hierarchical relationships
        on_delete=models.CASCADE,
        null=True,  # Allow root products without a parent
        blank=True, # Optional to be filled
        related_name='sub_products' # Optional: makes querying easier
    )
    name = models.OneToOneField(
        NameService,
        on_delete=models.CASCADE,
        unique=True,
        related_name = "product"
    )

    def __str__(self):
        return self.name  # Representing the object
    
    
    
class IntermediateProducts(models.Model):
    name = models.OneToOneField(
        NameService,
        on_delete=models.CASCADE,
        unique=True,
        related_name = "intermediateproduct"
    )
    
class UtilitySystem(models.Model):
    name = models.OneToOneField(
        NameService,
        on_delete=models.CASCADE,
        unique=True,
        related_name = "otherproduct"
    )

class InventoryUtilitySystem(models.Model):
    utility_system = models.ForeignKey(
        UtilitySystem,
        on_delete=models.CASCADE,
        related_name="inventory_records"
    )
    date = models.DateField(verbose_name="Date")
    quantity = models.FloatField(verbose_name="Inventory Quantity")

    class Meta:
        ordering = ['-date']  # رکوردها را براساس تاریخ از جدید به قدیم مرتب می‌کند

    def __str__(self):
        return f"{self.utility_system.name} - {self.date}: {self.quantity} units"


    

class ProductProducedAndShippeDaily(models.Model):
    product  = models.ForeignKey(Product, on_delete=models.CASCADE,related_name="product_report")
    IntermediateProducts  = models.ForeignKey(Product, on_delete=models.CASCADE,null=True,blank=True)

    produced = models.FloatField(default=0,null=True, blank=True)
    shippedaily = models.FloatField(default=0,null=True, blank=True)

    date = models.DateField(verbose_name="تاریخ")

    def clean(self):
        # بررسی اینکه حداقل یکی از فیلدها پر باشد
        if not self.product and not self.intermediate_products:
            raise ValidationError("حداقل یکی از فیلدهای 'product' یا 'intermediate_products' باید پر باشد.")

    def save(self, *args, **kwargs):
        # اجرای اعتبارسنجی‌ها قبل از ذخیره
        self.clean()
        super().save(*args, **kwargs)


 

class Tanker(models.Model):
    name = models.CharField(max_length=50)
    quantity = models.IntegerField(verbose_name="quantity", default=0)
    weight = models.FloatField(default=0)
    



class CargoLoading(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE,related_name='CargoLoading')
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


class SubProductCargoLoading(models.Model):
    # ارتباط با عملیات بارگیری اصلی
    cargo_loading = models.ForeignKey(
        CargoLoading,
        on_delete=models.CASCADE,
        related_name='sub_CargoLoading'
    )

    # زیرمحصولی که بارگیری می‌شود
    sub_product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='sub_loadings'
    )

    # مقدار بارگیری زیرمحصول خاص
    quantity = models.FloatField(verbose_name="Quantity", default=0)

    def __str__(self):
        return f"{self.sub_product.name} - {self.quantity} units in {self.cargo_loading}"


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
    percentage = models.FloatField(verbose_name="درصد موجودی", null=True, blank=True)  
    date = models.DateField(auto_now_add=True, verbose_name="تاریخ")

    def clean(self):
        """اعتبارسنجی بر اساس نوع مخزن"""
        if self.tank.tank_type == 'other' and self.percentage is None:
            raise ValidationError("برای مخازن 'سایر' باید درصد موجودی مشخص شود.")
        if self.tank.tank_type != 'other' and self.percentage is not None:
            raise ValidationError("درصد موجودی فقط برای مخازن 'سایر' معتبر است.")

    def __str__(self):
        return f"Inventory of {self.tank.name} on {self.date}"
    
    

