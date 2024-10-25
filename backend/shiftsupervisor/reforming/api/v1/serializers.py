from rest_framework import serializers
from reforming.models import (
    Unit100,
    Unit200,
    Unit250,
    Unit300,
    Unit350,
    DailyDataReforming,
)
from django.conf import settings


# class FixAbsolutePathSerializer(serializers.Field):

#     def to_representation(self, value):
#         text = value.replace(SEARCH_PATTERN, REPLACE_WITH)
#         return text


class U100Serializer(serializers.ModelSerializer):
    capacity_percent = serializers.FloatField(read_only=True)

    class Meta:
        model = Unit100
        fields = "__all__"

    def create(self, validated_data):
        # محاسبه‌ی capacity_percent
        feed_rate_t_hr = validated_data.get("feed_rate_t_hr")
        validated_data["capacity_percent"] = (feed_rate_t_hr / 34.1) * 100
        return super().create(validated_data)

    def update(self, instance, validated_data):
        # محاسبه‌ی capacity_percent
        feed_rate_t_hr = validated_data.get("feed_rate_t_hr")
        validated_data["capacity_percent"] = (feed_rate_t_hr / 34.1) * 100
        return super().update(instance, validated_data)


class UnitHelpTextSerializer(serializers.Serializer):
    help_texts = serializers.SerializerMethodField(read_only=True)

    def get_help_texts(self, obj):
        help_texts = {}
        for field in obj._meta.get_fields():
            if hasattr(field, "help_text") and field.help_text:
                help_texts[field.name] = field.help_text
        return help_texts


class U200Serializer(serializers.ModelSerializer):
    capacity_percent = serializers.FloatField(read_only=True)

    class Meta:
        model = Unit200
        fields = "__all__"

    def create(self, validated_data):
        # محاسبه‌ی capacity_percent
        t2001_t_hr = validated_data.get("t2001_t_hr")
        validated_data["capacity_percent"] = (t2001_t_hr / 568.182) * 100
        return super().create(validated_data)

    def update(self, instance, validated_data):
        # محاسبه‌ی capacity_percent
        t2001_t_hr = validated_data.get("t2001_t_hr")
        validated_data["capacity_percent"] = (t2001_t_hr / 568.182) * 100
        return super().update(instance, validated_data)


class U250Serializer(serializers.ModelSerializer):
    capacity_percent = serializers.FloatField(read_only=True)

    class Meta:
        model = Unit250
        fields = "__all__"

    def create(self, validated_data):
        # محاسبه‌ی capacity_percent
        feed_rate = validated_data.get("feed_rate")
        validated_data["capacity_percent"] = (feed_rate / 234.822) * 100
        return super().create(validated_data)

    def update(self, instance, validated_data):
        # محاسبه‌ی capacity_percent
        feed_rate = validated_data.get("feed_rate")
        validated_data["capacity_percent"] = (feed_rate / 234.822) * 100
        return super().update(instance, validated_data)


class U300Serializer(serializers.ModelSerializer):
    capacity_percent = serializers.FloatField(read_only=True)

    class Meta:
        model = Unit300
        fields = "__all__"

    def create(self, validated_data):
        # محاسبه‌ی capacity_percent
        feed_rate = validated_data.get("feed_rate")
        validated_data["capacity_percent"] = (feed_rate / 233.64) * 100
        return super().create(validated_data)

    def update(self, instance, validated_data):
        # محاسبه‌ی capacity_percent
        feed_rate = validated_data.get("feed_rate")
        validated_data["capacity_percent"] = (feed_rate / 233.64) * 100
        return super().update(instance, validated_data)


class U350Serializer(serializers.ModelSerializer):

    class Meta:
        model = Unit350
        exclude = ["capacity_percent"]


class DailyDataReformingSerializer(serializers.ModelSerializer):
    u100_data = U100Serializer(required=False, allow_null=True)
    u200_data = U200Serializer(required=False, allow_null=True)
    u250_data = U250Serializer(required=False, allow_null=True)
    u300_data = U300Serializer(required=False, allow_null=True)
    u350_data = U350Serializer(required=False, allow_null=True)

    user = serializers.CharField(source="user.first_name", read_only=True)

    class Meta:
        model = DailyDataReforming
        fields = "__all__"

        def validate(self, data):
            if not (
                data.get("u100_data")
                or data.get("u200_data")
                or data.get("u250_data")
                or data.get("u300_data")
                or data.get("u350_data")
            ):
                raise serializers.ValidationError(
                    "حداقل یکی از داده‌ها (Unit100,Unit200,Unit250,Unit300,Unit350) باید وارد شود."
                )
            return data

    def create(self, validated_data):
        date = validated_data.get("date")

        # جدا کردن داده‌های هر واحد
        u100_data = validated_data.pop("u100_data", None)
        u200_data = validated_data.pop("u200_data", None)
        u250_data = validated_data.pop("u250_data", None)
        u300_data = validated_data.pop("u300_data", None)
        u350_data = validated_data.pop("u350_data", None)

        # ذخیره‌سازی داده‌های واحدها با استفاده از سریالایزرها
        u100_instance = None
        u200_instance = None
        u250_instance = None
        u300_instance = None
        u350_instance = None

        if u100_data:
            u100_data["date"] = date
            u100_serializer = U100Serializer(data=u100_data)
            if u100_serializer.is_valid(raise_exception=True):
                u100_instance = u100_serializer.save()

        if u200_data:
            u200_data["date"] = date
            u200_serializer = U200Serializer(data=u200_data)
            if u200_serializer.is_valid(raise_exception=True):
                u200_instance = u200_serializer.save()

        if u250_data:
            u250_data["date"] = date
            u250_serializer = U250Serializer(data=u250_data)
            if u250_serializer.is_valid(raise_exception=True):
                u250_instance = u250_serializer.save()

        if u300_data:
            u300_data["date"] = date
            u300_serializer = U300Serializer(data=u300_data)
            if u300_serializer.is_valid(raise_exception=True):
                u300_instance = u300_serializer.save()

        if u350_data:
            u350_data["date"] = date
            u350_serializer = U350Serializer(data=u350_data)
            if u350_serializer.is_valid(raise_exception=True):
                u350_instance = u350_serializer.save()

        # ایجاد DailyDataReforming
        daily_data = DailyDataReforming.objects.create(
            u100_data=u100_instance,
            u200_data=u200_instance,
            u250_data=u250_instance,
            u300_data=u300_instance,
            u350_data=u350_instance,
            **validated_data
        )

        return daily_data
