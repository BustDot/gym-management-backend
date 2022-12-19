from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from dbproject.models.coach import Coach
from dbproject.models.course import Course
from dbproject.models.sysuser import SysUser
from dbproject.models.course_order import CourseOrder
from dbproject.serializers.course_serializer import CourseSerializer
from dbproject.serializers.course_order_serializer import CourseOrderSerializer


class ListUserOrderView(APIView):
    # permission_classes = ([IsAuthenticated])

    def get(self, request, p1):
        try:
            user_id = int(p1)
            user = SysUser.objects.get(user_id=user_id)
            courses = Course.objects.all()
            data = []
            for course in courses:
                serializer = CourseSerializer(course)
                temp = serializer.data
                if CourseOrder.objects.filter(sys_user=user, course=course).exists():
                    temp["is_selected"] = True
                else:
                    temp["is_selected"] = False
                data.append(temp)
            response = {'data': data, 'result': 'success'}
            return Response(data=response)
        except:
            response = {'result': 'error'}
            return Response(data=response, status=status.HTTP_400_BAD_REQUEST)