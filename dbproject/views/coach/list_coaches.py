from rest_framework.views import APIView
from rest_framework.response import Response
from dbproject.models.coach import Coach
from dbproject.serializers.coach_serializer import CoachSerializer


class ListCoachesView(APIView):
    def get(self, request):
        queryset = Coach.objects.all()
        serializer = CoachSerializer(queryset, many=True)
        response = {'data': serializer.data, 'result': 'success', 'total': len(serializer.data)}
        return Response(data=response)
