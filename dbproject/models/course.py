from django.db import models
from dbproject.models.coach import Coach


class Course(models.Model):
    course_name = models.CharField(max_length=20, default="")
    course_begin = models.DateTimeField()
    course_last = models.IntegerField()
    coach = models.ForeignKey(Coach, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.course_name)
