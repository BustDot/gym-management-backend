from rest_framework.serializers import ModelSerializer
from dbproject.models.course import Course


class CourseSerializer(ModelSerializer):
    class Meta:
        model = Course
        fields = ["id", "course_name", "course_begin", "course_last", "coach"]
