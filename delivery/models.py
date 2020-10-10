from django.db import models
from users import models as user_models
from order.models import Order, Item
# from moneyfield import MoneyField
# Create your models here.


class Delivery(models.Model):
    state = models.CharField(max_length=30, default="배달 대기 중", blank=True)
    lionders_info = models.ForeignKey(user_models.Users, on_delete=models.CASCADE, blank=True, null=True)
    order_sheet = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True)
    estimated_time = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    # updated_at = models.DateTimeField(auto_now=True)
    delivery_tips = models.IntegerField(null=True, default=0)
    grade_limit = models.CharField(max_length=30, default="초급자", blank=True)