from rest_framework import serializers
from tanks.models import (
    AdditionalServices, ServiceConsumedAndShippedDaily, Product, 
    ProductProducedAndShippeDaily, Tanker, CargoLoading, Tank, 
    TankInventory, Feed, FeedReception
)

class AdditionalServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdditionalServices
        fields = '__all__'

class ServiceConsumedAndShippedDailySerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceConsumedAndShippedDaily
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'

class ProductProducedAndShippedDailySerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductProducedAndShippeDaily
        fields = '__all__'

class TankerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tanker
        fields = '__all__'

class CargoLoadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = CargoLoading
        fields = '__all__'

class TankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tank
        fields = '__all__'

class TankInventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TankInventory
        fields = '__all__'

class FeedSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feed
        fields = '__all__'

class FeedReceptionSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedReception
        fields = '__all__'
