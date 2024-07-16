from image_gen import models
from rest_framework import serializers


class IndustrySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Industry
        fields = '__all__'


class SpecialitiesSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Specialty
        fields = ('name',)

class JobvaccancySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.JobListing
        fields = '__all__'


class CompanySerializer(serializers.ModelSerializer):
    logo = serializers.ImageField(required=False)
    specialties = serializers.ListField(write_only=True)
    # specialties = SpecialitiesSerializer(write_only=True)

    class Meta:
        model = models.Company
        fields = '__all__'

    def create(self, validated_data):
        specialties_data = validated_data.pop('specialties', []) 
        company = models.Company.objects.create(**validated_data)
        
        for specialty_data in specialties_data:
            specialty, _ = models.Specialty.objects.get_or_create(name=specialty_data)
            company.specialties.add(specialty)
        
        return company


class InfoTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.JobInfoTitle
        fields = '__all__'


class JobInfoSerializer(serializers.ModelSerializer):
    title = serializers.CharField(source='title.title')
    class Meta:
        model = models.AdditionalInfo
        fields = ('id','title', 'content')


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
        fields = '__all__'

class JobInfoTitleSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.JobInfoTitle
        # fields = ('title',)
        fields = '__all__'


class AdditionalInfoSerializer(serializers.ModelSerializer):
    titles = JobInfoTitleSerializer(source='title', read_only=True)
    # title = JobInfoTitleSerializer()
    class Meta:
        model = models.AdditionalInfo
        fields = '__all__'
        extra_kwargs = {
            'title': {'write_only': True}
        }


class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Skill
        fields = '__all__'


class JobListingSerializer(serializers.ModelSerializer):
    company_info = CompanySerializer(source='company', read_only=True)
    additional_info = serializers.SerializerMethodField(read_only=True)
    # qualifications = serializers.SerializerMethodField()
    # responsbilities = serializers.SerializerMethodField()
    # skills = serializers.SerializerMethodField()
    skills_data = SkillsSerializer(source='skills', many=True, read_only=True)
    # about_job = serializers.SerializerMethodField()

    class Meta:
        model = models.JobListing
        fields = '__all__'
        extra_kwargs = {
            'skills': {'write_only': True},
            'company': {'write_only': True}
        }

    # def get_about_job(self, obj):
    #     job_info = obj.about_job.all()
    #     return AboutJobSerializer(job_info, many=True).data
    
    def get_additional_info(self, obj):
        add_info = obj.add_info.all()
        return JobInfoSerializer(add_info, many=True).data
    
    # def get_skills(self, obj):
    #     skills = obj.skills.values_list('content', flat=True)
    #     return list(skills)
    

