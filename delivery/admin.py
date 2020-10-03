from django.contrib import admin
from .models import Delivery, Order, Item

# Register your models here.

admin.site.register(Delivery)
admin.site.register(Order)
admin.site.register(Item)