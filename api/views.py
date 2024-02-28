from django.shortcuts import render
from rest_framework import viewsets
from api.serializers import WorkerSerializer
from rest_framework.response import Response

from api.models import Workers

class workerModelViewsetView(viewsets.ModelViewSet):
    serializer_class=WorkerSerializer
    model=Workers
    queryset=Workers.objects.all()

