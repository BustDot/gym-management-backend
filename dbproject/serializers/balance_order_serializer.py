from rest_framework.serializers import ModelSerializer
from dbproject.models.balance_order import BalanceOrder


class BalanceOrderSerializer(ModelSerializer):
    class Meta:
        model = BalanceOrder
        fields = ["id", "sys_user", "top_up_value", "created_time"]
