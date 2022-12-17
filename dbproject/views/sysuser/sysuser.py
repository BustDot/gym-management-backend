from django.http import QueryDict
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.response import Response
from dbproject.models.sysuser import SysUser
from dbproject.serializers.sysuser_serializer import SysuserSerializer


class SysUserView(APIView):
    permission_classes = ([IsAuthenticated])

    def get(self, request, p1):
        try:
            user_id = int(p1)
            user = SysUser.objects.get(user_id=user_id)
            serializer = SysuserSerializer(user)
            response = {'data': serializer.data, 'result': 'success'}
            return Response(data=response)
        except:
            response = {'result': 'error'}
            return Response(data=response, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, p1):
        try:
            data = request.data
            user_id = int(p1)
            user = SysUser.objects.get(user_id=user_id)
            top_up_value = data.get("top_up_value", 0)
            top_up_value = int(top_up_value)
            user.card_time = user.card_time + top_up_value
            user.card_left_time = user.card_left_time + top_up_value
            user.save()
            serializer = SysuserSerializer(user)
            response = {'data': serializer.data, 'result': 'success'}
            return Response(data=response)
        except:
            response = {'result': 'error'}
            return Response(data=response, status=status.HTTP_400_BAD_REQUEST)
