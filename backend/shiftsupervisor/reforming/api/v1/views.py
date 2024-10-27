from django.shortcuts import render
from reforming.api.v1.serializers import (
    U100Serializer,
    U200Serializer,
    U250Serializer,
    U300Serializer,
    U350Serializer,
    DailyDataReformingSerializer,
)
from rest_framework.permissions import IsAuthenticated
from reforming.models import (
    Unit100,
    Unit200,
    Unit250,
    Unit300,
    Unit350,
    DailyDataReforming,
)
from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from reforming.api.v1.paginations import DefaultPagination
from accounts.models import Profile
from rest_framework.decorators import action

from shared.views import HelpTextViewSet


class U100HelpTextViewSet(HelpTextViewSet):
    model = Unit100


class U200HelpTextViewSet(HelpTextViewSet):
    model = Unit200


class U250HelpTextViewSet(HelpTextViewSet):
    model = Unit250


class U300HelpTextViewSet(HelpTextViewSet):
    model = Unit300


class U350HelpTextViewSet(HelpTextViewSet):
    model = Unit350


class U100ModelViewSet(viewsets.ModelViewSet):
    queryset = Unit100.objects.all().order_by("-date")
    serializer_class = U100Serializer
    http_method_names = ["get"]
    pagination_class = DefaultPagination


class U200ModelViewSet(viewsets.ModelViewSet):
    queryset = Unit200.objects.all().order_by("-date")
    serializer_class = U200Serializer
    http_method_names = ["get"]
    pagination_class = DefaultPagination


class U250ModelViewSet(viewsets.ModelViewSet):
    queryset = Unit250.objects.all().order_by("-date")
    serializer_class = U250Serializer
    http_method_names = ["get"]
    pagination_class = DefaultPagination


class U300ModelViewSet(viewsets.ModelViewSet):
    queryset = Unit300.objects.all().order_by("-date")
    serializer_class = U300Serializer
    http_method_names = ["get"]
    pagination_class = DefaultPagination


class U350ModelViewSet(viewsets.ModelViewSet):
    queryset = Unit350.objects.all().order_by("-date")
    serializer_class = U350Serializer
    http_method_names = ["get"]
    pagination_class = DefaultPagination


class DailyDataReformingViewSet(viewsets.ModelViewSet):
    queryset = DailyDataReforming.objects.all()
    serializer_class = DailyDataReformingSerializer
    permission_classes = [
        IsAuthenticated
    ]  # فرض بر این که فقط کاربران لاگین کرده بتوانند داده‌ها را مشاهده کنند
    pagination_class = DefaultPagination

    def perform_create(self, serializer):
        profile = Profile.objects.get(user=self.request.user)
        serializer.save(user=profile)
