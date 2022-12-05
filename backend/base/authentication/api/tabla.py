from rest_framework.permissions import BasePermission, IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
from authentication.models.tabla import Tabla
from rest_framework import serializers
from rest_framework import status, viewsets


class TablaModelSerializer(serializers.ModelSerializer):

    class Meta:
        model = Tabla
        fields = '__all__'


class TablaViewSet(viewsets.ModelViewSet):
    queryset = Tabla.objects.all()
    serializer_class = TablaModelSerializer
    filterset_fields = ['id']
