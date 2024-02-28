from rest_framework import serializers
from api.models import Workers


class WorkerSerializer(serializers.ModelSerializer):
    class Meta:
        model=Workers
        fields="__all__"
        read_only_fields=["id"]