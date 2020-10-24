from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Item)

@admin.register(models.Order)
class OrderAdmin(admin.ModelAdmin):
    """ Order Admin """

    fieldsets = (
        (
            "Order Information",
            {
                "fields": (
                    "normal_user_info",
                    "total_price",
                    "destination_road",
                    "items",
                    "grade_limit",
                )
            },
        ),
    )
    
    filter_horizontal = ("items",)
    list_display = ("normal_user_info","total_price","destination_road","grade_limit")