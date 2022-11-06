from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from dbproject.models.user.user import user

class InfoView(APIView):
    permission_classes = ([IsAuthenticated])

    def get(self, request):
        user = request.user
        dbuser = user.objects.get(user=user)
        return Response({
            'result': "success",
            'user_id': user.user_id,
            'avatar': dbuser.avatar,
        })
