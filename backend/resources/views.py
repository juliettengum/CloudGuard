

# Create your views here.

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated

from .models import CloudResource
from .serializers import CloudResourceSerializer


class CloudResourceViewSet(viewsets.ModelViewSet):
    queryset = CloudResource.objects.all().order_by("-created_at")
    serializer_class = CloudResourceSerializer
    permission_classes = [IsAuthenticated]
