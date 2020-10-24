from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.
class Users(AbstractUser):
    """ Base User Model """
    
    USERTYPE_CONSUMER = "consumer"
    USERTYPE_LIONDERS = "lionders"

    USERTYPE_CHOICES = (
        (USERTYPE_CONSUMER, "consumer"),
        (USERTYPE_LIONDERS, "lionders"),
    )
    image = models.ImageField(blank=True, null=True, upload_to="blog/%Y/%m/%d")
    usertype = models.CharField(max_length = 8,choices=USERTYPE_CHOICES)
    name = models.CharField(max_length = 50)
    address_num = models.CharField(max_length = 30)
    address_road = models.CharField(max_length = 100)
    address_detail = models.CharField(max_length = 100)
    phone = models.CharField(max_length = 15)

    class meta:
        abstract = True

class Consumer_Users(Users):
    """ Consumer User Moder """

    is_pro = models.BooleanField(default=False)
    have_order_sheet = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Consumer User"

class Lionders_Users(Users):
    """ Lionders User Model """

    GRADE_CHOICES = (
        ('초급자', "초급자"),
        ('중급자', "중급자"),
        ('고급자', "고급자"),
    )
   
    grade = models.CharField(max_length = 12, choices=GRADE_CHOICES, default = "초급자")
    rating = models.FloatField(default=0.0)
    rating_count = models.PositiveIntegerField(default=0)

    class Meta:
        verbose_name = "Lionders User"