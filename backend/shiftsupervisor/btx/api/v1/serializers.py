from rest_framework import serializers
from btx.models import U500,U600,U650,DailyDataBtx
from django.conf import settings




# class FixAbsolutePathSerializer(serializers.Field):
        
#     def to_representation(self, value):
#         text = value.replace(SEARCH_PATTERN, REPLACE_WITH)
#         return text



class U500Serializer(serializers.ModelSerializer):
    capacity_percent = serializers.FloatField(read_only=True)
    
    
    class Meta:
        model = U500
        fields = '__all__'

    def create(self, validated_data):
        # محاسبه‌ی capacity_percent 
        t_5001_feed_rate = validated_data.get('t_5001_feed_rate')
        validated_data['capacity_percent'] = (t_5001_feed_rate /126.88) * 100
        return super().create(validated_data)

    def update(self, instance, validated_data):
        # محاسبه‌ی capacity_percent 
        t_5001_feed_rate = validated_data.get('t_5001_feed_rate')
        validated_data['capacity_percent'] = (t_5001_feed_rate /126.88) * 100
        return super().update(instance, validated_data)




class U600Serializer(serializers.ModelSerializer):
    capacity_percent = serializers.FloatField(read_only=True)
    
    class Meta:
        model = U600
        fields = '__all__'

    def create(self, validated_data):
        # محاسبه‌ی capacity_percent 
        tk_6001_bt_from_sec_500 = validated_data.get('tk_6001_bt_from_sec_500')
        validated_data['capacity_percent'] = (tk_6001_bt_from_sec_500 /80.954) * 100
        return super().create(validated_data)

    def update(self, instance, validated_data):
        # محاسبه‌ی capacity_percent 
        tk_6001_bt_from_sec_500 = validated_data.get('tk_6001_bt_from_sec_500')
        validated_data['capacity_percent'] = (tk_6001_bt_from_sec_500 /80.954) * 100
        return super().update(instance, validated_data)


class U650Serializer(serializers.ModelSerializer):
    capacity_percent = serializers.FloatField(read_only=True)
    
    class Meta:
        model = U650
        fields = '__all__'

    def create(self, validated_data):
        # محاسبه‌ی capacity_percent 
        t_6501_feed_rate = validated_data.get('t_6501_feed_rate')
        validated_data['capacity_percent'] = (tk_6001_bt_from_sec_500 /76.691) * 100
        return super().create(validated_data)

    def update(self, instance, validated_data):
        # محاسبه‌ی capacity_percent 
        t_6501_feed_rate = validated_data.get('t_6501_feed_rate')
        validated_data['capacity_percent'] = (t_6501_feed_rate /76.691) * 100
        return super().update(instance, validated_data)






class DailyDataBtxSerializer(serializers.ModelSerializer):
    u500_data = U500Serializer(required=False, allow_null=True)
    u600_data = U600Serializer(required=False, allow_null=True)
    u650_data = U650Serializer(required=False, allow_null=True)
    user = serializers.CharField(source='user.first_name', read_only=True)

    class Meta:
        model = DailyDataBtx
        fields = '__all__'

        def validate(self, data):
            if not (data.get('u500_data') or data.get('u600_data') or data.get('u650_data')):
                raise serializers.ValidationError("حداقل یکی از داده‌ها (U500، U600 یا U650) باید وارد شود.")
            return data


    def create(self, validated_data):
        """ ایجاد DailyDataBtx به همراه داده‌های مرتبط با U500, U600 و U650 """
        date = validated_data.get('date')

        # جدا کردن داده‌های واحدها از validated_data
        u500_data = validated_data.pop('u500_data', None)
        u600_data = validated_data.pop('u600_data', None)
        u650_data = validated_data.pop('u650_data', None)

        if u500_data:
            u500_data['date'] = date
            u500_instance = U500.objects.create(**u500_data)
        else:
            u500_instance = None

        if u600_data:
            u600_data['date'] = date
            u600_instance = U600.objects.create(**u600_data)
        else:
            u600_instance = None

        if u650_data:
            u650_data['date'] = date
            u650_instance = U650.objects.create(**u650_data)
        else:
            u650_instance = None

        # ایجاد DailyDataBtx
        daily_data = DailyDataBtx.objects.create(
            u500_data=u500_instance,
            u600_data=u600_instance,
            u650_data=u650_instance,
            **validated_data
        )

        return daily_data
