from rest_framework import viewsets
from tanks.models import (
    AdditionalServices, ServiceConsumedAndShippedDaily, Product, 
    ProductProducedAndShippeDaily, Tanker, CargoLoading, Tank, 
    TankInventory, Feed, FeedReception
)
from .serializers import (
    AdditionalServicesSerializer, ServiceConsumedAndShippedDailySerializer, 
    ProductSerializer, ProductProducedAndShippedDailySerializer, TankerSerializer, 
    CargoLoadingSerializer, TankSerializer, TankInventorySerializer, 
    FeedSerializer, FeedReceptionSerializer
)

class AdditionalServicesViewSet(viewsets.ModelViewSet):
    queryset = AdditionalServices.objects.all()
    serializer_class = AdditionalServicesSerializer

class ServiceConsumedAndShippedDailyViewSet(viewsets.ModelViewSet):
    queryset = ServiceConsumedAndShippedDaily.objects.all()
    serializer_class = ServiceConsumedAndShippedDailySerializer

class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer

class ProductProducedAndShippedDailyViewSet(viewsets.ModelViewSet):
    queryset = ProductProducedAndShippeDaily.objects.all()
    serializer_class = ProductProducedAndShippedDailySerializer

class TankerViewSet(viewsets.ModelViewSet):
    queryset = Tanker.objects.all()
    serializer_class = TankerSerializer

class CargoLoadingViewSet(viewsets.ModelViewSet):
    queryset = CargoLoading.objects.all()
    serializer_class = CargoLoadingSerializer

class TankViewSet(viewsets.ModelViewSet):
    queryset = Tank.objects.all()
    serializer_class = TankSerializer

class TankInventoryViewSet(viewsets.ModelViewSet):
    queryset = TankInventory.objects.all()
    serializer_class = TankInventorySerializer

class FeedViewSet(viewsets.ModelViewSet):
    queryset = Feed.objects.all()
    serializer_class = FeedSerializer

class FeedReceptionViewSet(viewsets.ModelViewSet):
    queryset = FeedReception.objects.all()
    serializer_class = FeedReceptionSerializer
