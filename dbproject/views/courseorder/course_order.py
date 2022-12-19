from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from dbproject.models.coach import Coach
from dbproject.models.course import Course
from dbproject.models.sysuser import SysUser
from dbproject.models.course_order import CourseOrder
from dbproject.serializers.coach_serializer import CoachSerializer
from dbproject.serializers.course_order_serializer import CourseOrderSerializer


class CourseOrderView(APIView):
    # permission_classes = ([IsAuthenticated])

    def get(self, request, p1):
        try:
            user_id = int(p1)
            user = SysUser.objects.get(user_id=user_id)
            queryset = CourseOrder.objects.filter(sys_user=user)
            serializer = CourseOrderSerializer(queryset, many=True)
            response = {'data': serializer.data, 'result': 'success'}
            return Response(data=response)
        except:
            response = {'result': 'error'}
            return Response(data=response, status=status.HTTP_400_BAD_REQUEST)

    def post(self, request, p1):
        # try:
        data = request.data
        course = Course.objects.get(id=data.get("course"))
        sys_user = SysUser.objects.get(user_id=data.get("sys_user"))
        coach = Coach.objects.get(id=data.get("coach"))

        if course.course_last > sys_user.card_left_time:
            response = {'result': 'error', 'message': "余额不足"}
            return Response(data=response)
        CourseOrder.objects.create(course=course, sys_user=sys_user, coach=coach)
        sys_user.card_left_time = sys_user.card_left_time - course.course_last
        sys_user.save()
        return Response({
            'result': "success",
        })

    # except:
    #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, p1):
        data = request.data
        course = Course.objects.get(id=data.get("course"))
        sys_user = SysUser.objects.get(user_id=data.get("sys_user"))
        if CourseOrder.objects.filter(sys_user=sys_user, course=course).exists():
            course_order = CourseOrder.objects.get(sys_user=sys_user, course=course)
            course_order.delete()
            sys_user.card_left_time = sys_user.card_left_time + course.course_last
            sys_user.save()
        return Response(status=status.HTTP_204_NO_CONTENT)
