from django.db import models
from users import models as user_models
# Create your models here.


class Order(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    normal_user_info = models.ForeignKey(user_models.Users, on_delete=models.CASCADE, blank=True, null=True)
    ordered_time = models.DateTimeField(auto_now_add=True, blank=True)
    # updated_at = models.DateTimeField(auto_now=True)
    total_price = models.IntegerField()
    destination = models.CharField(max_length=100, blank=True)

    def __str__(self):
        return self.title + ': ' + self.comment[:3]


class Delivery(models.Model):
    title = models.CharField(max_length=100, blank=True, null=True)
    state = models.CharField(max_length=30, default=1, blank=True)
    lionders_info = models.ForeignKey(user_models.Users, on_delete=models.CASCADE, blank=True, null=True)
    order_sheet = models.ForeignKey(Order, on_delete=models.CASCADE, blank=True, null=True)
    estimated_time = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    # updated_at = models.DateTimeField(auto_now=True)
    delivery_tips = models.IntegerField(null=True, default=0)
    grade_limit = models.CharField(max_length=30, default=1, blank=True)

    def __str__(self):
        return self.title + ': ' + self.comment[:3]
