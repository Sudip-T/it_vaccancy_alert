from django.contrib import admin
from .models import JobListing, Company, Industry


admin.site.register(Industry)

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
