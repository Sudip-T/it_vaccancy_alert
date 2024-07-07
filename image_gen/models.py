from django.db import models

class JobListing(models.Model):
    position = models.CharField(max_length=100)
    company = models.CharField(max_length=100)
    experience = models.CharField(max_length=100)
    job_type = models.CharField(max_length=100)
    location = models.CharField(max_length=100)
    date_published = models.DateTimeField(blank=True, null=True)
    deadline = models.DateTimeField(blank=True, null=True)
    date_added = models.DateTimeField(auto_now_add=True)
    salary = models.CharField(max_length=100, default='Negotiable')
    no_of_vaccancy = models.CharField(max_length=10, default=1)
    career_level = models.CharField(max_length=100, default='Junior')
    vac_img = models.ImageField(upload_to='vaccancy', null=True, blank=True)
    apply_at = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.position
    


class JobDetails(models.Model):
    job_listing = models.OneToOneField(JobListing, on_delete=models.CASCADE, related_name='details')
    company_description = models.TextField()
    job_description = models.TextField()
    technical_skills = models.TextField()
    responsibilities = models.TextField()
    qualifications = models.TextField()
    additional_information = models.TextField()

    def __str__(self):
        return f"Details for {self.job_listing.position} at {self.job_listing.company}"
