from rest_framework.views import APIView
from rest_framework.response import Response
from django.contrib.auth.models import User
from dbproject.models.sysuser import SysUser
import requests

class UserView(APIView):
    def post(self, request):
        data = request.POST
        username = data.get("username", "").strip()
        password = data.get("password", "").strip()
        password_confirm = data.get("password_confirm", "").strip()
        if not username or not password:
            return Response({
                'result': "用户名和密码不能为空"
            })
        if password != password_confirm:
            return Response({
                'result': "两个密码不一致",
            })
        if User.objects.filter(username=username).exists():
            return Response({
                'result': "用户名已存在",
            })
        user = User(username=username)
        user.set_password(password)
        user.save()
        resp = requests.get("http://api.btstu.cn/sjtx/api.php?lx=a1")
        resp = resp.json()
        avatar_url = resp.get("imgurl")
        SysUser.objects.create(user=user, avatar=avatar_url)
        return Response({
            'result': "success",
        })
