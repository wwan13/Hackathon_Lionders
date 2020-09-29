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
                    "adress",
                    "is_pro",
                )
            },
        ),
    )

    list_display = ("name","adress","is_pro")
    

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
                    "adress",
                    "grade",
                )
            },
        ),
    )
    
    #filter_horizontal = ("rating",)
    list_display = ("name","adress","grade")

    