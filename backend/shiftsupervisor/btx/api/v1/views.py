from django.shortcuts import render
from btx.api.v1.serializers import U500Serializer,U600Serializer,U650Serializer,DailyDataBtxSerializer
from rest_framework.permissions import IsAuthenticated
from btx.models import U500,U600,U650,DailyDataBtx
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from btx.api.v1.paginations import DefaultPagination
from accounts.models import Profile
# Create your views here.

class U500ModelViewSet(viewsets.ModelViewSet):
    queryset = U500.objects.all().order_by('-date')
    serializer_class =  U500Serializer
    http_method_names = [ 'get']
    search_fields = ["title", "content"]
    pagination_class = DefaultPagination
    
   
class U600ModelViewSet(viewsets.ModelViewSet):
    queryset = U600.objects.all().order_by('-date')
    serializer_class =  U600Serializer
    http_method_names = [ 'get']
    search_fields = ["title", "content"]
    pagination_class = DefaultPagination
    
   
class U650ModelViewSet(viewsets.ModelViewSet):
    queryset = U650.objects.all().order_by('-date')
    serializer_class =  U650Serializer
    http_method_names = [ 'get']
    search_fields = ["title", "content"]
    pagination_class = DefaultPagination
    
   
    


class DailyDataBtxViewSet(viewsets.ModelViewSet):
    queryset = DailyDataBtx.objects.all()
    serializer_class = DailyDataBtxSerializer
    permission_classes = [IsAuthenticated]  # فرض بر این که فقط کاربران لاگین کرده بتوانند داده‌ها را مشاهده کنند
    pagination_class = DefaultPagination


    def perform_create(self, serializer):
        profile = Profile.objects.get(user=self.request.user) 
        serializer.save(user=profile)  
