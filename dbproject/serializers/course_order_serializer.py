from rest_framework.serializers import ModelSerializer
from dbproject.models.course_order import CourseOrder


class CourseOrderSerializer(ModelSerializer):
    class Meta:
        model = CourseOrder
        fields = ["id", "coach", "course", "sys_user", "created_time"]
