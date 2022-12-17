from rest_framework.serializers import ModelSerializer
from dbproject.models.sysuser import SysUser


class SysuserSerializer(ModelSerializer):
    class Meta:
        model = SysUser
        fields = ["id", "name", "avatar", "gender", "age", "phone", "course"]
