from rest_framework.views import APIView
from rest_framework.response import Response
from dbproject.models.sysuser import SysUser
from dbproject.serializers.sysuser_serializer import SysuserSerializer


class ListSysUsersView(APIView):
    def get(self, request):
        queryset = SysUser.objects.all()
        serializer = SysuserSerializer(queryset, many=True)
        response = {'data': serializer.data, 'result': 'success', 'total': len(serializer.data)}
        return Response(data=response)
