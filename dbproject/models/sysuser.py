from django.db import models
from django.contrib.auth.models import User


class SysUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    name = models.CharField(max_length=20, default="")
    avatar = models.URLField(max_length=256, blank=True)
    gender = models.CharField(max_length=10, default="男")
    age = models.IntegerField(default=0)
    height = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    weight = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    phone = models.CharField(max_length=20, default="")
    card_time = models.IntegerField(default=0)
    card_left_time = models.IntegerField(default=0)

    def __str__(self):
        return str(self.user)
