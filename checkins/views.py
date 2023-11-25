from checkins.models import Checkin
from checkins.serializers import CheckinSerializer
from checkins.permissions import CheckinPermissionChecker
from rest_framework.permissions import IsAuthenticated
from rest_framework.generics import ListCreateAPIView
from rest_framework_simplejwt.authentication import JWTAuthentication


class CheckinView(ListCreateAPIView):
    authentication_classes = [JWTAuthentication]
    permission_classes = [IsAuthenticated, CheckinPermissionChecker]
    
    serializer_class = CheckinSerializer

    def get_queryset(self):
        user_id = self.request.query_params.get('user_id', None)

        if user_id:
            return Checkin.objects.filter(employee_id=user_id)
        else:
            return Checkin.objects.all()
