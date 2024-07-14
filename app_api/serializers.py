from image_gen import models
from rest_framework import serializers


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

class InfoTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.JobInfoTitle
        fields = '__all__'


class JobInfoSerializer(serializers.ModelSerializer):
    title = serializers.CharField(source='title.title')
    class Meta:
        model = models.AdditionalInfo
        fields = ('title', 'content')


class QualificationSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AdditionalInfo
        fields = ('content', )


class ResponsibilitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AdditionalInfo
        fields = ('content', )


class AboutJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.AboutJob
        fields = ('content', )

class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Skill
        fields = ('content', )


class JobListingSerializer(serializers.ModelSerializer):
    company = CompanySerializer()
    additional_info = serializers.SerializerMethodField()
    # qualifications = serializers.SerializerMethodField()
    # responsbilities = serializers.SerializerMethodField()
    # skills = serializers.SerializerMethodField()
    # about_job = serializers.SerializerMethodField()

    class Meta:
        model = models.JobListing
        fields = '__all__'

    # def get_about_job(self, obj):
    #     job_info = obj.about_job.all()
    #     return AboutJobSerializer(job_info, many=True).data
    
    def get_additional_info(self, obj):
        add_info = obj.add_info.all()
        return JobInfoSerializer(add_info, many=True).data
    
    # def get_skills(self, obj):
    #     skills = obj.skills.values_list('content', flat=True)
    #     return list(skills)
    
    # def get_responsbilities(self, obj):
    #     skills = obj.responsbilities.values_list('content', flat=True)
    #     return list(skills)
    
    # def get_qualifications(self, obj):
    #     skills = obj.qualifications.values_list('content', flat=True)
    #     return list(skills)

