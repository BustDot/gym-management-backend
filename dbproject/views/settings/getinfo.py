from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from dbproject.models.sysuser import SysUser


class InfoView(APIView):
    permission_classes = ([IsAuthenticated])

    def get(self, request):
        try:
            user_id = int(request.GET.get('user_id', 1))
            sys_user = SysUser.objects.get(user_id=user_id)
            return Response({
                'result': "success",
                'id': sys_user.user.id,
                'username': sys_user.user.username,
                'avatar': sys_user.avatar,
            })
        except:
            return Response({
                'result': "输入参数错误"
            })
