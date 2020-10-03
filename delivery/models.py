from django.db import models
from users import models as user_models
# from moneyfield import MoneyField
# Create your models here.


class Item(models.Model):
    store = models.CharField(max_length=100, blank=True)
    item_name = models.CharField(max_length=100, blank=True)
    price = models.PositiveIntegerField(blank=True, default=0)

    def __str__(self):
        return self.item_name

    def __unicode__(self):
        return self.item_name


class Order(models.Model):
    normal_user_info = models.ForeignKey(user_models.Users, on_delete=models.CASCADE, blank=True, null=True)
    ordered_time = models.DateTimeField(auto_now_add=True, blank=True)
    # updated_at = models.DateTimeField(auto_now=True)
    total_price = models.PositiveIntegerField(blank=True, default=0)
    destination = models.CharField(max_length=100, blank=True)
    items = models.ManyToManyField(Item, blank=True)



class Delivery(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=30, default="On Call", blank=True)
    lionders_info = models.ForeignKey(user_models.Users, on_delete=models.CASCADE, blank=True, null=True)
    order_sheet = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True)
    estimated_time = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    # updated_at = models.DateTimeField(auto_now=True)
    delivery_tips = models.IntegerField(null=True, default=0)
    grade_limit = models.CharField(max_length=30, default="초급자", blank=True)