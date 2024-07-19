from .serializers import *
from image_gen.models import *
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet


class IndustryView(ModelViewSet):
    queryset = Industry.objects.all()
    serializer_class = IndustrySerializer


class SpecialitiesView(ModelViewSet):
    queryset = Specialty.objects.all()
    serializer_class = SpecialitiesSerializer


class SkillsView(ModelViewSet):
    queryset = Skill.objects.all()
    serializer_class = SkillsSerializer


class AdditionalInfoView(ModelViewSet):
    queryset = AdditionalInfo.objects.all()
    serializer_class = AdditionalInfoSerializer


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
    # serializer_class = CompanySerializer

 

    # def perform_create(self, serializer):
    #     # Override perform_create to handle specialties association
    #     specialties_data = self.request.data.get('specialities','')
    #     instance = serializer.save()
    #     print(specialties_data.split(','))
    #     # for specialty in specialties_data.split(','):
    #         # instance.specialties.add(specialty_id)

    # def perform_update(self, serializer):
    #     # Override perform_update to handle specialties association
    #     specialties_data = self.request.data.get('specialties', [])
    #     instance = serializer.save()
    #     instance.specialties.clear()
    #     for specialty_id in specialties_data:
    #         instance.specialties.add(specialty_id)


class JobListingView(ModelViewSet):
    queryset = JobListing.objects.all()
    serializer_class = JobListingSerializer
    filterset_fields = ['company']

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.Job_views +=1
        instance.save()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)