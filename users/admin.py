from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from . import models

# Register your models here.
@admin.register(models.Consumer_Users)
class ConsumerUserAdmin(UserAdmin):
    """ Consumer User Admin """

    fieldsets = (
        (
            "Consumer Profile",
            {
                "fields": (
                    "usertype",
                    "name",
                    "address_num",
                    "address_road",
                    "address_detail",
                    "is_pro",
                    "have_order_sheet",
                )
            },
        ),
    )

    list_display = ("name","address_num","address_road","address_detail","is_pro")
    

@admin.register(models.Lionders_Users)
class LiondersUserAdmin(UserAdmin):
    """ Lionders User Admin """

    fieldsets = (
        (
            "Consumer Profile",
            {
                "fields": (
                    "usertype",
                    "name",
                    "address_num",
                    "address_road",
                    "address_detail",
                    "grade",
                )
            },
        ),
    )
    
    #filter_horizontal = ("rating",)
    list_display = ("name","address_num","address_road","address_detail","grade")

    