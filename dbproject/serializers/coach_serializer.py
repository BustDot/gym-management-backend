from rest_framework.serializers import ModelSerializer
from dbproject.models.sysuser import SysUser


class CoachSerializer(ModelSerializer):
    class Meta:
        model = SysUser
        fields = ["pk", "user_id", "name", "avatar", "gender", "age", "phone", "card_time", "card_left_time"]
