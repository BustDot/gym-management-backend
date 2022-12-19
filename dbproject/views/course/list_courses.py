from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from dbproject.models.course import Course
from dbproject.serializers.course_serializer import CourseSerializer
from dbproject.models.coach import Coach


class ListCoursesView(APIView):
    def get(self, request):
        queryset = Course.objects.all()
        serializer = CourseSerializer(queryset, many=True)
        data = []
        for x in serializer.data:
            course = x
            coach = Coach.objects.get(id=course.get("coach"))
            course["coach_name"] = coach.name
            data.append(course)
        response = {'data': data, 'result': 'success', 'total': len(serializer.data)}
        return Response(data=response)

    def post(self, request):
        try:
            data = request.data
            coach = Coach.objects.get(name=data.get("coach_name"))
            data["coach"] = coach.id
            data.pop("coach_name")
            serializer = CourseSerializer(data=data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
        except:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
