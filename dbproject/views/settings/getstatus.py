from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth import authenticate, login


class GetstatusView(APIView):
    def get(self, request):
        user = request.SysUser
        if user.is_authenticated:
            return Response({
                'result': "login",
                'username': user.username
            })
        return Response({
            'result': "logout"
        })
