# from django import forms
# from .models import JobListing

# class JobListingForm(forms.ModelForm):
#     class Meta:
#         model = JobListing
#         fields = ['position', 'company', 'job_type', 'location', 'experience']



# forms.py

from django import forms
from .models import JobListing, JobDetails

class JobForm(forms.ModelForm):
    class Meta:
        model = JobListing
        fields = ['position', 'company', 'experience', 'job_type', 'location', 'deadline']

    company_description = forms.CharField(widget=forms.Textarea)
    job_description = forms.CharField(widget=forms.Textarea)
    technical_skills = forms.CharField(widget=forms.Textarea)
    responsibilities = forms.CharField(widget=forms.Textarea)
    qualifications = forms.CharField(widget=forms.Textarea)
    additional_information = forms.CharField(widget=forms.Textarea)

    def save(self, commit=True):
        job_listing = super().save(commit=False)
        if commit:
            job_listing.save()

        job_details = JobDetails(
            job_listing=job_listing,
            company_description=self.cleaned_data['company_description'],
            job_description=self.cleaned_data['job_description'],
            technical_skills=self.cleaned_data['technical_skills'],
            responsibilities=self.cleaned_data['responsibilities'],
            qualifications=self.cleaned_data['qualifications'],
            additional_information=self.cleaned_data['additional_information']
        )
        job_details.save()

        return job_listing, job_details
