from django.db import models
from dbproject.models.coach import Coach
from dbproject.models.sysuser import SysUser
from dbproject.models.course import Course


class CourseOrder(models.Model):
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    coach = models.ForeignKey(Coach, on_delete=models.CASCADE)
    sys_user = models.ForeignKey(SysUser, on_delete=models.CASCADE)
    created_time = models.TimeField(auto_now_add=True)

    def __str__(self):
        return str(self.course)
