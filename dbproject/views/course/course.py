from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from dbproject.models.coach import Coach
from dbproject.models.course import Course
from dbproject.serializers.coach_serializer import CoachSerializer


class CourseView(APIView):
    permission_classes = ([IsAuthenticated])

    def get(self, request, p1):
        try:
            user_id = int(p1)
            user = Coach.objects.get(user_id=user_id)
            serializer = CoachSerializer(user)
            response = {'data': serializer.data, 'result': 'success'}
            return Response(data=response)
        except:
            response = {'result': 'error'}
            return Response(data=response, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, p1):
        user_id = int(p1)
        user = Course.objects.get(id=user_id)
        user.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

