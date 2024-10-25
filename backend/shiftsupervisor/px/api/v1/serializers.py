from rest_framework import serializers
from px.models import U400,U700,U800,U950,U970,DailyDataPX
from django.conf import settings




# class FixAbsolutePathSerializer(serializers.Field):
        
#     def to_representation(self, value):
#         text = value.replace(SEARCH_PATTERN, REPLACE_WITH)
#         return text



class U400Serializer(serializers.ModelSerializer):
    capacity_percent = serializers.FloatField(read_only=True)
    
    
    class Meta:
        model = U400
        fields = '__all__'

    def create(self, validated_data):
        # محاسبه‌ی capacity_percent 
        t_4001_feed_rate = validated_data.get('t_4001_feed_rate')
        validated_data['capacity_percent'] = (t_4001_feed_rate /238.26) * 100
        return super().create(validated_data)

    def update(self, instance, validated_data):
        # محاسبه‌ی capacity_percent 
        t_4001_feed_rate = validated_data.get('t_4001_feed_rate')
        validated_data['capacity_percent'] = (t_4001_feed_rate /238.26) * 100
        return super().update(instance, validated_data)




class U700Serializer(serializers.ModelSerializer):
    capacity_percent = serializers.FloatField(read_only=True)
    
    class Meta:
        model = U700
        fields = '__all__'

    def create(self, validated_data):
        # محاسبه‌ی capacity_percent 
        feed_t_7001_a_b = validated_data.get('feed_t_7001_a_b')
        validated_data['capacity_percent'] = (feed_t_7001_a_b /426.57) * 100
        return super().create(validated_data)

    def update(self, instance, validated_data):
        # محاسبه‌ی capacity_percent 
        feed_t_7001_a_b = validated_data.get('feed_t_7001_a_b')
        validated_data['capacity_percent'] = (feed_t_7001_a_b /426.57) * 100
        return super().update(instance, validated_data)


class U800Serializer(serializers.ModelSerializer):
    capacity_percent = serializers.FloatField(read_only=True)
    
    class Meta:
        model = U800
        fields = '__all__'

    def create(self, validated_data):
        # محاسبه‌ی capacity_percent 
        t_8001_aro_rec = validated_data.get('t_8001_aro_rec')
        validated_data['capacity_percent'] = (t_8001_aro_rec /335.762) * 100
        return super().create(validated_data)

    def update(self, instance, validated_data):
        # محاسبه‌ی capacity_percent 
        t_8001_aro_rec = validated_data.get('t_8001_aro_rec')
        validated_data['capacity_percent'] = (t_8001_aro_rec /335.762) * 100
        return super().update(instance, validated_data)



class U950Serializer(serializers.ModelSerializer):
    capacity_percent = serializers.FloatField(read_only=True)
    
    class Meta:
        model = U950
        fields = '__all__'

    def create(self, validated_data):
        # محاسبه‌ی capacity_percent 
        feed_rate = validated_data.get('feed_rate')
        validated_data['capacity_percent'] = (feed_rate /113) * 100
        return super().create(validated_data)

    def update(self, instance, validated_data):
        # محاسبه‌ی capacity_percent 
        feed_rate = validated_data.get('feed_rate')
        validated_data['capacity_percent'] = (feed_rate /113) * 100
        return super().update(instance, validated_data)



class U970Serializer(serializers.ModelSerializer):
    capacity_percent = serializers.FloatField(read_only=True)
    
    class Meta:
        model = U970
        fields = '__all__'

    def create(self, validated_data):
        # محاسبه‌ی capacity_percent 
        feed_rate = validated_data.get('feed_rate')
        validated_data['capacity_percent'] = (feed_rate /150) * 100
        return super().create(validated_data)

    def update(self, instance, validated_data):
        # محاسبه‌ی capacity_percent 
        feed_rate = validated_data.get('feed_rate')
        validated_data['capacity_percent'] = (feed_rate /150) * 100
        return super().update(instance, validated_data)







class DailyDataPXSerializer(serializers.ModelSerializer):
    u400_data = U400Serializer(required=False, allow_null=True)
    u700_data = U700Serializer(required=False, allow_null=True)
    u800_data = U800Serializer(required=False, allow_null=True)
    u950_data = U950Serializer(required=False, allow_null=True)
    u970_data = U970Serializer(required=False, allow_null=True)

    user = serializers.CharField(source='user.first_name', read_only=True)

    class Meta:
        model = DailyDataPX
        fields = '__all__'

        def validate(self, data):
            if not (data.get('u400_data') or data.get('u700_data') or data.get('u800_data') or data.get('u950_data') or data.get('u970_data')) :
                raise serializers.ValidationError("حداقل یکی از داده‌ها (U400، U700 , U800,U900,U970) باید وارد شود.")
            return data


    def create(self, validated_data):
        date = validated_data.get('date')

        # جدا کردن داده‌های واحدها از validated_data
        u400_data = validated_data.pop('u400_data', None)
        u700_data = validated_data.pop('u700_data', None)
        u800_data = validated_data.pop('u800_data', None)
        u950_data = validated_data.pop('u950_data', None)
        u970_data = validated_data.pop('u970_data', None)

        u400_instance = None
        u700_instance = None
        u800_instance = None
        u950_instance = None
        u970_instance = None

        # ایجاد داده برای U400
        if u400_data:
            u400_data['date'] = date
            u400_serializer = U400Serializer(data=u400_data)
            if u400_serializer.is_valid(raise_exception=True):
                u400_instance = u400_serializer.save()

        # ایجاد داده برای U700
        if u700_data:
            u700_data['date'] = date
            u700_serializer = U700Serializer(data=u700_data)
            if u700_serializer.is_valid(raise_exception=True):
                u700_instance = u700_serializer.save()

        # ایجاد داده برای U800
        if u800_data:
            u800_data['date'] = date
            u800_serializer = U800Serializer(data=u800_data)
            if u800_serializer.is_valid(raise_exception=True):
                u800_instance = u800_serializer.save()

        # ایجاد داده برای U950
        if u950_data:
            u950_data['date'] = date
            u950_serializer = U950Serializer(data=u950_data)
            if u950_serializer.is_valid(raise_exception=True):
                u950_instance = u950_serializer.save()

        # ایجاد داده برای U970
        if u970_data:
            u970_data['date'] = date
            u970_serializer = U970Serializer(data=u970_data)
            if u970_serializer.is_valid(raise_exception=True):
                u970_instance = u970_serializer.save()

        # ایجاد DailyDataPX
        daily_data = DailyDataPX.objects.create(
            u400_data=u400_instance,
            u700_data=u700_instance,
            u800_data=u800_instance,
            u950_data=u950_instance,
            u970_data=u970_instance,
            **validated_data
        )

        return daily_data

