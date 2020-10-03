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

    usertype = models.CharField(max_length = 8,choices=USERTYPE_CHOICES)
    name = models.CharField(max_length = 50)
    address = models.CharField(max_length = 100)
    phone = models.CharField(max_length = 15)

    class meta:
        abstract = True

class Consumer_Users(Users):
    """ Consumer User Moder """

    is_pro = models.BooleanField(default=False)

    class Meta:
        verbose_name = "Consumer User"

class Lionders_Users(Users):
    """ Lionders User Model """

    GRADE_CHOICES = (
        ('Beginner', "초급자"),
        ('Intermediate', "중급자"),
        ('Advanced', "고급자"),
    )

    grade = models.CharField(max_length = 10, choices=GRADE_CHOICES)
    #rating = models.ManyToManyField(Consumer_Users)

    class Meta:
        verbose_name = "Lionders User"