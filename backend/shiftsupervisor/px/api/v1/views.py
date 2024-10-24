from django.shortcuts import render
from px.api.v1.serializers import U400Serializer,U700Serializer,U800Serializer,U950Serializer,U970Serializer,DailyDataPXSerializer
from rest_framework.permissions import IsAuthenticated
from px.models import U400,U700,U800,U950,U970,DailyDataPX
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from px.api.v1.paginations import DefaultPagination
from accounts.models import Profile
# Create your views here.

class U400ModelViewSet(viewsets.ModelViewSet):
    queryset = U400.objects.all().order_by('-date')
    serializer_class =  U400Serializer
    http_method_names = [ 'get']
    pagination_class = DefaultPagination
    
   
class U700ModelViewSet(viewsets.ModelViewSet):
    queryset = U700.objects.all().order_by('-date')
    serializer_class =  U700Serializer
    http_method_names = [ 'get']
    pagination_class = DefaultPagination
    
   
class U800ModelViewSet(viewsets.ModelViewSet):
    queryset = U800.objects.all().order_by('-date')
    serializer_class =  U800Serializer
    http_method_names = [ 'get']
    pagination_class = DefaultPagination
    
   
   
class U950ModelViewSet(viewsets.ModelViewSet):
    queryset = U950.objects.all().order_by('-date')
    serializer_class =  U950Serializer
    http_method_names = [ 'get']
    pagination_class = DefaultPagination
    
   
class U970ModelViewSet(viewsets.ModelViewSet):
    queryset = U970.objects.all().order_by('-date')
    serializer_class =  U970Serializer
    http_method_names = [ 'get']
    pagination_class = DefaultPagination
    
   
    


class DailyDataPxViewSet(viewsets.ModelViewSet):
    queryset = DailyDataPX.objects.all()
    serializer_class = DailyDataPXSerializer
    permission_classes = [IsAuthenticated]  # فرض بر این که فقط کاربران لاگین کرده بتوانند داده‌ها را مشاهده کنند
    pagination_class = DefaultPagination


    def perform_create(self, serializer):
        profile = Profile.objects.get(user=self.request.user) 
        serializer.save(user=profile)  
