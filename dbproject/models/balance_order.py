from django.db import models
from dbproject.models.coach import Coach
from dbproject.models.sysuser import SysUser
from dbproject.models.course import Course


class BalanceOrder(models.Model):
    sys_user = models.ForeignKey(SysUser, on_delete=models.CASCADE)
    top_up_value = models.IntegerField(default=0)
    created_time = models.DateTimeField(auto_now_add=True)

