from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from image_gen.models import Industry, JobListing, Company
from .serializers import IndustrySerializer, JobvaccancySerializer, CompanySerializer, JobListingSerializer
from rest_framework.response import Response
from rest_framework import status

class IndustryView(ModelViewSet):
    queryset = Industry.objects.all()
    serializer_class = IndustrySerializer

# class JobVaccancyView(ModelViewSet):
#     queryset = JobListing.objects.all()
#     serializer_class = JobvaccancySerializer

#     def list(self, request, *args, **kwargs):
#         if self.queryset.count() == 0:
#             return Response({"error": "No job listings available."}, status=status.HTTP_404_NOT_FOUND)
        
#         queryset = self.filter_queryset(self.get_queryset())
#         serializer = self.get_serializer(queryset, many=True)
#         return Response(serializer.data)

class CompanyView(ModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer

class JobListingView(ModelViewSet):
    queryset = JobListing.objects.all()
    serializer_class = JobListingSerializer
