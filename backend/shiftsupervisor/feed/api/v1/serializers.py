from rest_framework import serializers
from feed.models import (
    FeedInventory,
    Feed,
    Company,
    TankInventory,
    CompanyFuelAnalysis,
    TankOperation,
    GlobalFuelAnalysis,
)
from tanks.api.v1.utils import find_service_by_name


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = "__all__"


class TankInventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TankInventory
        fields = "__all__"


class CompanyFuelAnalysisSerializer(serializers.ModelSerializer):
    class Meta:
        model = CompanyFuelAnalysis
        fields = "__all__"


class TankOperationSerializer(serializers.ModelSerializer):
    class Meta:
        model = TankOperation
        fields = "__all__"


class GlobalFuelAnalysisSerializer(serializers.ModelSerializer):
    class Meta:
        model = GlobalFuelAnalysis
        fields = "__all__"


class FeedModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feed
        fields = "__all__"


class FeedInventorySerializer(serializers.Serializer):
    feed_name = serializers.CharField()
    quantity = serializers.FloatField()

    def validate_feed_name(self, data):
        # بررسی وجود فید با نام داده شده
        service_name = data.get("feed_name")

        # جستجوی سرویس و ذخیره آن برای استفاده در مراحل بعدی
        nameservice = find_service_by_name(service_name, "feed")
        if not nameservice:
            raise ValidationError("سرویس با این نام یافت نشد.")
        data["nameservice"] = nameservice
        return data

    def create_feed_inventory(self, validated_data, date):
        # پیدا کردن یا ایجاد رکوردهای FeedInventory با توجه به feed و quantity
        feed = Feed.objects.get(name=validated_data["nameservice"])
        return FeedInventory.objects.update_or_create(
            feed=feed, date=date, quantity=validated_data.get("quantity")
        )


class FeedInventoryModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = FeedInventory
        fields = "__all__"
