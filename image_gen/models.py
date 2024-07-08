from django.db import models
from django.core.validators import MaxValueValidator


class Industry(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name
    

class Company(models.Model):
    name = models.CharField(max_length=100)
    about = models.TextField(blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    website = models.URLField(blank=True, null=True)
    address = models.CharField(max_length=200, blank=True, null=True)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    established_date = models.DateField(blank=True, null=True)
    size = models.CharField(max_length=50, blank=True, null=True)
    logo = models.ImageField(upload_to='company_logos/', blank=True, null=True)
    industry = models.ForeignKey(Industry, on_delete=models.SET_NULL, null=True, blank=True)
    # specialties = models.CharField(max_length=200, blank=True, null=True)

    def __str__(self):
        return self.name
    


class JobListing(models.Model):
    company = models.ForeignKey(Company, on_delete=models.CASCADE)
    position = models.CharField(max_length=100)
    experience = models.PositiveIntegerField(validators=[MaxValueValidator(30)])
    Employement_type  = models.CharField(max_length=50, choices=[
        ('Full-Time', 'Full-Time'), 
        ('Part-Time', 'Part-Time'), 
        ('Remote', 'Remote'), 
        ('Internship', 'Internship')
    ])
    Seniority_level = models.CharField(max_length=50, choices=[
        ('Junior', 'Junior'), 
        ('Mid-Level', 'Mid-Level'), 
        ('Senior', 'Senior'), 
        ('Team Lead', 'Team Lead'),
        ('Project Manager', 'Project Manager')
    ])
    about_job = models.TextField()
    salary = models.CharField(max_length=100, default='Negotiable/Not Disclosed')
    deadline = models.DateTimeField(blank=True, null=True)
    date_published = models.DateTimeField(auto_now_add=True)
    application_link = models.URLField(blank=True, null=True)
    application_email = models.EmailField(blank=True, null=True)
    no_of_vaccancy = models.CharField(max_length=10, default=1)
    education_level = models.CharField(max_length=100, blank=True, null=True)

    vac_img = models.ImageField(upload_to='vaccancy', null=True, blank=True)

    qualifications = models.TextField()
    responsibilities = models.TextField(blank=True, null=True)
    technical_skills = models.TextField(blank=True, null=True)
    benefits = models.TextField(blank=True, null=True)
    additional_information = models.TextField(blank=True, null=True)

    # jobmetrics
    Job_views = models.PositiveIntegerField(default=0)
    application_count = models.PositiveIntegerField(default=0)
    


    def __str__(self):
        return f"{self.position} at {self.company.name}"


# class JobListing(models.Model):
#     position = models.CharField(max_length=100)
#     company = models.CharField(max_length=100)
#     experience = models.CharField(max_length=100)
#     job_type = models.CharField(max_length=100)
#     location = models.CharField(max_length=100)
#     date_published = models.DateTimeField(blank=True, null=True)
#     deadline = models.DateTimeField(blank=True, null=True)
#     date_added = models.DateTimeField(auto_now_add=True)
#     salary = models.CharField(max_length=100, default='Negotiable')
#     no_of_vaccancy = models.CharField(max_length=10, default=1)
#     career_level = models.CharField(max_length=100, default='Junior')
#     vac_img = models.ImageField(upload_to='vaccancy', null=True, blank=True)
#     company_logo = models.ImageField(upload_to='company_logo', null=True, blank=True)
#     apply_at = models.CharField(max_length=500, null=True, blank=True)

#     def __str__(self):
#         return self.position
    


# class JobDetails(models.Model):
#     job_listing = models.OneToOneField(JobListing, on_delete=models.CASCADE, related_name='details')
#     company_description = models.TextField()
#     job_description = models.TextField()
#     technical_skills = models.TextField()
#     responsibilities = models.TextField()
#     qualifications = models.TextField()
#     additional_information = models.TextField()

#     def __str__(self):
#         return f"Details for {self.job_listing.position} at {self.job_listing.company}"
