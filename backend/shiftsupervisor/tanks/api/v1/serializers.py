from rest_framework import serializers
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


class AdditionalServicesSerializer(serializers.ModelSerializer):
    class Meta:
        model = AdditionalServices
        fields = "__all__"


class ServiceConsumedAndShippedDailyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceConsumedAndShippedDaily
        fields = "__all__"


class ServiceConsumedAndShippedDailySerializer(serializers.Serializer):
    service_name = serializers.CharField()
    shippedaily = serializers.FloatField()

    def validate(self, data):
        service_name = data.get("service_name")

        # جستجوی سرویس و ذخیره آن برای استفاده در مراحل بعدی
        nameservice = find_service_by_name(service_name, "service")
        if not nameservice:
            raise ValidationError("سرویس با این نام یافت نشد.")

        # ذخیره کردن شیء برای استفاده در view
        data["nameservice"] = nameservice
        return data

    def create_service_inventory(self, validated_data, date):
        # پیدا کردن یا ایجاد رکوردهای FeedInventory با توجه به feed و quantity
        nameservice = validated_data.get("nameservice")
        shippedaily_value = validated_data.get("shippedaily")
        # به‌روزرسانی رکورد موجود با استفاده از شیء از پیش جستجو شده

        additional_service = AdditionalServices.objects.get(name=nameservice)
        ServiceConsumedAndShippedDaily.objects.update_or_create(
            additionalServices=additional_service,
            date=date,
            defaults={"shippedaily": shippedaily_value},
        )


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = "__all__"


class ProductProducedAndShippedDailyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductProducedAndShippeDaily
        fields = "__all__"


class ProductProducedAndShippedDailySerializer(serializers.Serializer):
    product_name = serializers.CharField()
    produced = serializers.FloatField()
    shippedaily = serializers.FloatField()

    def validate(self, data):
        product_name = data.get("product_name")

        # جستجوی سرویس و ذخیره آن برای استفاده در مراحل بعدی
        nameservice = find_service_by_name(product_name, "product")
        if not nameservice:
            raise ValidationError("محصولی با این نام یافت نشد.")

        # ذخیره کردن شیء برای استفاده در view
        data["nameservice"] = nameservice
        return data

    def create_product_inventory(self, validated_data, date):
        nameservice = validated_data.get("nameservice")
        produced = validated_data.get("produced")
        shippedaily = validated_data.get("shippedaily")

        # ایجاد رکورد جدید با استفاده از شیء از پیش جستجو شده
        product = Product.objects.get(name=nameservice)

        ProductProducedAndShippeDaily.objects.update_or_create(
            product=product,
            produced=shippedaily_value,
            shippedaily=shippedaily,
            date=date,
        )


class TankerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tanker
        fields = "__all__"


class CargoLoadingSerializer(serializers.ModelSerializer):
    class Meta:
        model = CargoLoading
        fields = "__all__"


class TankSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tank
        fields = "__all__"


class TankInventorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TankInventory
        fields = "__all__"
