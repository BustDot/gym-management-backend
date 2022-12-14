from rest_framework.serializers import ModelSerializer
from dbproject.models.sysuser import SysUser


class SysuserSerializer(ModelSerializer):
    class Meta:
        model = SysUser
        fields = ["pk", "name", "avatar", "gender", "phone", "card_time", "card_left_time"]
