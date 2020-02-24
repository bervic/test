# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView

from serializer import BlogSerializer

# Create your views here.


class Blog(APIView):

    def get(self, request):
        return Response({"data": "Data returnerd by get method"})
    
    def post(self, request):
        serializer = BlogSerializer(data=request.data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        return Response({"data": "Data returnerd by get method"})