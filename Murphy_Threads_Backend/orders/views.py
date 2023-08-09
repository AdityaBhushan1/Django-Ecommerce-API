from django.shortcuts import render
from django.conf import settings
from utils.renderers import UserRenderer
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.exceptions import ValidationError
from .serializers import *
from rest_framework.permissions import IsAuthenticated
from .models import *

class OrderView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]

    def get(self,request):
        ...

    def post(self,request):
        ...

class OrdersListView(APIView):
    renderer_classes = [UserRenderer]
    permission_classes = [IsAuthenticated]
    def get(self,request):
        ...

