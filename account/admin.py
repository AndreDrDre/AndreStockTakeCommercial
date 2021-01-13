from django.contrib import admin
from .models import *  # This imports all the models

# Register your models here.
admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Tag)
admin.site.register(Order)
