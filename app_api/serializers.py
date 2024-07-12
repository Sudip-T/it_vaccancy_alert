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


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Company
        fields = '__all__'


class JobInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AdditionalInfo
        fields = ('header', 'content')


class JobListingSerializer(serializers.ModelSerializer):
    company = CompanySerializer()
    additional_info = serializers.SerializerMethodField()

    class Meta:
        model = models.JobListing
        fields = '__all__'

    def get_additional_info(self, obj):
        add_info = obj.add_info.all()
        return JobInfoSerializer(add_info, many=True).data


