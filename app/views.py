from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response

from django.db.models import Q
from app.permissions import IsOwnerOrReadOnly

from app.serializers import BandSerializer, AlbumSerializer
from app.models import Band, Album

class BandListCreateAPIView(APIView):
    def get:
        pass
    def post:
        pass

class BandRetrieveUpdateDestroyAPIView(APIView):
    def get:
        pass
    def put:
        pass
    def delete:
        pass

class AlbumListCreateAPIView(APIView):
    def get:
        pass
    def post:
        pass

class AlbumRetrieveUpdateDestroyAPIView(APIView):
    def get:
        pass
    def put:
        pass
    def delete:
        pass
