import datetime

from django.db.models import Sum
from rest_framework.views import APIView
from rest_framework.response import Response

from dbproject.models.balance_order import BalanceOrder
from dbproject.models.sysuser import SysUser
from dbproject.models.coach import Coach
from dbproject.models.course import Course
from dbproject.models.course_order import CourseOrder


class DataDisplayView(APIView):
    def get(self, request):
        sys_user_count = SysUser.objects.all().count()
        coach_count = Coach.objects.all().count()
        course_count = Course.objects.all().count()
        course_order_count = CourseOrder.objects.all().count()

        course_order_x = []
        course_order_y = []
        today = datetime.date.today()
        start = today - datetime.timedelta(6)
        end = today - datetime.timedelta(5)
        for i in range(7):
            course_order_x.append(start.day)
            course_order_y.append(CourseOrder.objects.filter(created_time__range=(start, end)).count())
            start = start + datetime.timedelta(1)
            end = end + datetime.timedelta(1)

        balance_order_y = []
        today = datetime.date.today()
        start = today - datetime.timedelta(6)
        end = today - datetime.timedelta(5)
        for i in range(7):
            total = BalanceOrder.objects.filter(created_time__range=(start, end)).aggregate(nums=Sum('top_up_value'))
            balance_order_y.append(0 if total.get("nums") is None else total.get("nums"))
            start = start + datetime.timedelta(1)
            end = end + datetime.timedelta(1)

        response = {
            "sys_user_count": sys_user_count,
            "coach_count": coach_count,
            "course_count": course_count,
            "course_order_count": course_order_count,
            "course_order_x": course_order_x,
            "course_order_y": course_order_y,
            "balance_order_y": balance_order_y,
            "balance_today": balance_order_y[6],
            "balance_yes": balance_order_y[5]
        }
        return Response(data=response)
