
import django_filters
from django_filters import DateFilter
from .models import *


class OrderFilter(django_filters.FilterSet):
    start_date = DateFilter(field_name='start_date', lookup_expr='gte')
    end_date = DateFilter(field_name='end_date', lookup_expr='lte')

    class Meta:
        model = Order
        fields = '__all__'
        exclude = ['customer', 'date_created']


class ProductFilter(django_filters.FilterSet):

    class Meta:
        model = Product
        fields = '__all__'
        exclude = ['name', 'description', 'tags', 'date_created', 'price']
