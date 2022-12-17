from django.db import models


class Coach(models.Model):
    name = models.CharField(max_length=20, default="")
    avatar = models.URLField(max_length=256, blank=True)
    gender = models.CharField(max_length=10, default="男")
    age = models.IntegerField(default=0)
    phone = models.CharField(max_length=20, default="")
    course = models.CharField(max_length=50, default="")

    def __str__(self):
        return str(self.name)
