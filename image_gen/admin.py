from django.contrib import admin
from .models import *


admin.site.register(Industry)
admin.site.register(Qualifications)
admin.site.register(Responsbilities)
admin.site.register(AboutJob)
admin.site.register(Skill)
admin.site.register(JobInfoTitle)
admin.site.register(Hashtag)

@admin.register(AdditionalInfo)
class AdditionalInfoAdmin(admin.ModelAdmin):
    list_display = ('title','job_position')

    def job_position(self, obj):
        return f'{obj.job.position} - {obj.job.company.name}'
    job_position.short_description = 'Job Position'

@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ('name', 'industry', 'size', 'established_date')
    search_fields = ('name', 'industry')
    list_filter = ('industry', 'size')

@admin.register(JobListing)
class JobListingAdmin(admin.ModelAdmin):
    list_display = ('position', 'company', 'Employement_type', 'date_published', 'deadline')
    search_fields = ('position', 'company__name')
    list_filter = ('Employement_type', 'date_published', 'deadline', 'company__industry')
