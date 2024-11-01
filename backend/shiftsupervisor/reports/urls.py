# reports/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('generate-report/', views.export_all_units_to_excel, name='write_section_data'),
]
