from django_filters import rest_framework as filters
from btx.models import U500


# class UnitFilters(filters.FilterSet):
#     class Meta:
#         model = U500
#         fields = {
#             "temp__name": ["exact", "in"],
#             "temp": ["exact"],
#             "temp": ["exact"],
#         }