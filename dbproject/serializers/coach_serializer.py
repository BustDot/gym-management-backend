from rest_framework.serializers import ModelSerializer
from dbproject.models.coach import Coach


class CoachSerializer(ModelSerializer):
    class Meta:
        model = Coach
        fields = ["id", "name", "avatar", "gender", "age", "phone"]
