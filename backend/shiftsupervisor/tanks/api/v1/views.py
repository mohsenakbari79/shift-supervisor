from rest_framework import viewsets
from rest_framework.views import APIView

from tanks.models import (
    AdditionalServices,
    ServiceConsumedAndShippedDaily,
    Product,
    ProductProducedAndShippeDaily,
    Tanker,
    CargoLoading,
    Tank,
    TankInventory,
)
from .serializers import (
    AdditionalServicesSerializer,
    ServiceConsumedAndShippedDailySerializer,
    ServiceConsumedAndShippedDailyModelSerializer,
    ProductSerializer,
    ProductProducedAndShippedDailySerializer,
    TankerSerializer,
    CargoLoadingSerializer,
    TankSerializer,
    TankInventorySerializer,
    ProductProducedAndShippedDailyModelSerializer,
    ProductProducedAndShippedDailySerializer,
)


class AdditionalServicesViewSet(viewsets.ModelViewSet):
    queryset = AdditionalServices.objects.all()
    serializer_class = AdditionalServicesSerializer


class ServiceConsumedAndShippedDailyView(APIView):

    def get(self, request, *args, **kwargs):
        date = request.query_params.get("date", None)

        if date:
            queryset = ServiceConsumedAndShippedDaily.objects.filter(date=date)
        else:
            queryset = ServiceConsumedAndShippedDaily.objects.all()

        serializer = ServiceConsumedAndShippedDailyModelSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        services_data = request.data.get("services", [])
        date = request.data.get("date")

        if not date:
            return Response(
                {"error": "تاریخ مورد نیاز است."}, status=status.HTTP_400_BAD_REQUEST
            )

        serializer = ServiceConsumedAndShippedDailySerializer(
            data=services_data, many=True
        )

        if serializer.is_valid():
            for validated_data in serializer.validated_data:
                serializer.create_service_inventory(validated_data, date)
            return Response(
                {"status": "رکوردها با موفقیت ایجاد شدند."},
                status=status.HTTP_201_CREATED,
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        services_data = request.data.get("services", [])
        date = request.data.get("date")

        if not date:
            return Response(
                {"error": "تاریخ مورد نیاز است."}, status=status.HTTP_400_BAD_REQUEST
            )

        serializer = ServiceConsumedAndShippedDailySerializer(
            data=services_data, many=True
        )

        if serializer.is_valid():
            for validated_data in serializer.validated_data:
                serializer.create_service_inventory(validated_data, date)
            return Response(
                {"status": "رکوردها با موفقیت به‌روزرسانی شدند."},
                status=status.HTTP_200_OK,
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductProducedAndShippedDailyModelViewSet(viewsets.ModelViewSet):
    queryset = ProductProducedAndShippeDaily.objects.all()
    serializer_class = ProductProducedAndShippedDailySerializer


class ProductProducedAndShippedDailyViewSet(APIView):

    def get(self, request, *args, **kwargs):
        date = request.query_params.get("date", None)

        if date:
            queryset = ProductProducedAndShippeDaily.objects.filter(date=date)
        else:
            queryset = ProductProducedAndShippeDaily.objects.all()

        serializer = ProductProducedAndShippedDailyModelSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        product_data = request.data.get("product", [])
        date = request.data.get("date")

        if not date:
            return Response(
                {"error": "تاریخ مورد نیاز است."}, status=status.HTTP_400_BAD_REQUEST
            )

        serializer = ProductProducedAndShippedDailySerializer(
            data=product_data, many=True
        )

        if serializer.is_valid():
            for validated_data in serializer.validated_data:
                serializer.create_product_inventory(validated_data, date)
            return Response(
                {"status": "رکوردها با موفقیت ایجاد شدند."},
                status=status.HTTP_201_CREATED,
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        product_data = request.data.get("product", [])
        date = request.data.get("date")

        if not date:
            return Response(
                {"error": "تاریخ مورد نیاز است."}, status=status.HTTP_400_BAD_REQUEST
            )

        serializer = ProductProducedAndShippedDailySerializer(
            data=product_data, many=True
        )

        if serializer.is_valid():
            for validated_data in serializer.validated_data:
                serializer.create_product_inventory(validated_data, date)
            return Response(
                {"status": "رکوردها با موفقیت به‌روزرسانی شدند."},
                status=status.HTTP_200_OK,
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


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
