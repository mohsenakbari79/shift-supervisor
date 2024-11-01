from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from feed.models import (
    FeedInventory,
    Company,
    TankInventory,
    CompanyFuelAnalysis,
    TankOperation,
    GlobalFuelAnalysis,
)
from .serializers import (
    FeedInventorySerializer,
    FeedInventoryModelSerializer,
    CompanySerializer,
    TankInventorySerializer,
    CompanyFuelAnalysisSerializer,
    TankOperationSerializer,
    GlobalFuelAnalysisSerializer,
)


class CompanyViewSet(viewsets.ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer


class TankInventoryViewSet(viewsets.ModelViewSet):
    queryset = TankInventory.objects.all()
    serializer_class = TankInventorySerializer


class CompanyFuelAnalysisViewSet(viewsets.ModelViewSet):
    queryset = CompanyFuelAnalysis.objects.all()
    serializer_class = CompanyFuelAnalysisSerializer


class TankOperationViewSet(viewsets.ModelViewSet):
    queryset = TankOperation.objects.all()
    serializer_class = TankOperationSerializer


class GlobalFuelAnalysisViewSet(viewsets.ModelViewSet):
    queryset = GlobalFuelAnalysis.objects.all()
    serializer_class = GlobalFuelAnalysisSerializer


class FeedInventoryView(APIView):

    def get(self, request, *args, **kwargs):
        date = request.query_params.get("date")
        if date:
            queryset = FeedInventory.objects.filter(date=date)
        else:
            queryset = FeedInventory.objects.all()
        serializer = FeedInventoryModelSerializer(feed_inventory, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
        date = request.data.get("date")
        feeds_data = request.data.get("feeds", [])

        if not date:
            return Response(
                {"error": "تاریخ مورد نیاز است."}, status=status.HTTP_400_BAD_REQUEST
            )

        serializer = FeedInventorySerializer(data=feeds_data, many=True)
        if serializer.is_valid():
            for validated_data in serializer.validated_data:
                serializer.create_feed_inventory(validated_data, date)
            return Response(
                {"status": "رکوردها با موفقیت ایجاد شدند."},
                status=status.HTTP_201_CREATED,
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, *args, **kwargs):
        date = request.data.get("date")
        feeds_data = request.data.get("feeds", [])

        if not date:
            return Response(
                {"error": "تاریخ مورد نیاز است."}, status=status.HTTP_400_BAD_REQUEST
            )

        serializer = FeedInventorySerializer(data=feeds_data, many=True)
        if serializer.is_valid():
            for validated_data in serializer.validated_data:
                serializer.create_feed_inventory(validated_data, date)
            return Response(
                {"status": "رکوردها با موفقیت به‌روزرسانی شدند."},
                status=status.HTTP_200_OK,
            )

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
