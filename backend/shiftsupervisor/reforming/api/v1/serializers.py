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
        """ایجاد DailyDataBtx به همراه داده‌های مرتبط با U500, U600 و U650"""
        date = validated_data.get("date")

        u100_data = validated_data.pop("u100_data", None)
        u200_data = validated_data.pop("u200_data", None)
        u250_data = validated_data.pop("u250_data", None)
        u300_data = validated_data.pop("u300_data", None)
        u350_data = validated_data.pop("u350_data", None)

        if u100_data:
            u100_data["date"] = date
            u100_instance = Unit100.objects.create(**u100_data)
        else:
            u100_instance = None

        if u200_data:
            u200_data["date"] = date
            u200_instance = Unit200.objects.create(**u200_data)
        else:
            u200_instance = None

        if u250_data:
            u250_data["date"] = date
            u250_instance = Unit250.objects.create(**u250_data)
        else:
            u250_instance = None

        if u300_data:
            u300_data["date"] = date
            u300_instance = Unit300.objects.create(**u300_data)
        else:
            u300_instance = None

        if u350_data:
            u350_data["date"] = date
            u350_instance = Unit350.objects.create(**u350_data)
        else:
            u350_instance = None

        # ایجاد DailyDataBtx
        daily_data = DailyDataReforming.objects.create(
            u100_data=u100_instance,
            u200_data=u200_instance,
            u250_data=u250_instance,
            u300_data=u300_instance,
            u350_data=u350_instance,
            **validated_data
        )

        return daily_data
