from django.db import models

# Create your models here.
class AdditionalServices(models.Model):
    # name =
    # description
    pass
class ServiceConsumedAndShippedDaily(models.Model):
    # AdditionalServices 
    # shippedaily
    # Consumed
    # date
    pass
    

class Product(models.Model):
    # name = 
    # description
    pass

    



    
class ProductProducedAndShippeDaily(models):
    # product  = models.ForeignKey(Product, on_delete=models.CASCADE)
    # produced 
    # shippedaily
    # date
    pass

class ProductCombination(models.Model):
    # product 
    # loading = ProductProducedAndShippeDaily
    # quantity 
     pass
 

class Tanker(models.Medel):
    # name
    # quantity 
    # weight = models.IntegerField
    pass

class CargoLoading(models.Model):
    # F:product
    # ship 
    # trucks 
    # tanker forenkry
    # nubmber deufalt =1
    pass

class Combinations(models.Model):
    # F:product
    # subproduct

class Tank(models.Model):
    # name
    # tank_type multisection
    pass

class TankInventory(models.Model):
    # produced
    # service 
    # inventory
    # date
    
    
    pass