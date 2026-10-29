

# Create your models here.

from django.db import models


class CloudResource(models.Model):
    RESOURCE_TYPES = [
        ("EC2", "EC2 Instance"),
        ("S3", "S3 Bucket"),
        ("RDS", "RDS Database"),
        ("LAMBDA", "Lambda Function"),
        ("OTHER", "Other"),
    ]

    ENVIRONMENTS = [
        ("development", "Development"),
        ("staging", "Staging"),
        ("production", "Production"),
    ]

    STATUSES = [
        ("active", "Active"),
        ("inactive", "Inactive"),
        ("maintenance", "Maintenance"),
    ]

    name = models.CharField(max_length=150)
    resource_type = models.CharField(
        max_length=20,
        choices=RESOURCE_TYPES,
    )
    environment = models.CharField(
        max_length=20,
        choices=ENVIRONMENTS,
    )
    status = models.CharField(
        max_length=20,
        choices=STATUSES,
        default="active",
    )
    description = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.resource_type})"
