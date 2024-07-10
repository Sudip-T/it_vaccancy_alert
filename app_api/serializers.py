from rest_framework import serializers
from image_gen import models


class IndustrySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Industry
        fields = '__all__'


class JobvaccancySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.JobListing
        fields = '__all__'