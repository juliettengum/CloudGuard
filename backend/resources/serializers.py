

from rest_framework import serializers
from .models import CloudResource


class CloudResourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = CloudResource
        fields = [
            "id",
            "name",
            "resource_type",
            "environment",
            "status",
            "description",
            "created_at",
            "updated_at",
        ]
        read_only_fields = [
            "id",
            "created_at",
            "updated_at",
        ]
