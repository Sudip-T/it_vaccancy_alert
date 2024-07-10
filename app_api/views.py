from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from image_gen import models
from .serializers import *
from rest_framework.response import Response
from rest_framework import status

# Create your views here.

class IndustryView(ModelViewSet):
    queryset = models.Industry.objects.all()
    serializer_class = IndustrySerializer

class JobVaccancyView(ModelViewSet):
    queryset = models.JobListing.objects.all()
    serializer_class = JobvaccancySerializer

    def list(self, request, *args, **kwargs):
        print(self.queryset.count())
        if self.queryset.count() == 0:
            return Response({"error": "No job listings available."}, status=status.HTTP_404_NOT_FOUND)
        
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)