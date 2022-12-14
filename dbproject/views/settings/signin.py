from django.contrib.auth import authenticate, login
from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from dbproject.models.sysuser import SysUser


class SigninView(APIView):
    def post(self, request):
        data = request.POST
        username = data.get("username", "")
        password = data.get('password')
        user = authenticate(username=username, password=password)
        if not user:
            return Response({
                'result': "用户名或密码不正确"
            })
        login(request, user)
        return Response({
            'result': "success"
        })
