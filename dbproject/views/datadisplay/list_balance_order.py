from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from dbproject.models.balance_order import BalanceOrder
from dbproject.models.sysuser import SysUser
from dbproject.serializers.balance_order_serializer import BalanceOrderSerializer


class ListBalanceOrderView(APIView):
    def get(self, request):
        queryset = BalanceOrder.objects.all()[:5]
        serializer = BalanceOrderSerializer(queryset, many=True)
        data = []
        for x in serializer.data:
            order = x
            sys_user = SysUser.objects.get(id=order.get("sys_user"))
            order["sys_user_name"] = sys_user.name
            data.append(order)
        response = {'data': data, 'result': 'success', 'total': len(serializer.data)}
        return Response(data=response)

