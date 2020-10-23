from django.contrib import admin
from . import models

# Register your models here.

admin.site.register(models.Community)
admin.site.register(models.Comment)