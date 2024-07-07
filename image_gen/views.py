from .models import JobListing, JobDetails
from .forms import JobForm
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .utility import TakeScreenshot


def create_listing(request):
    if request.method == 'POST':
        form = JobForm(request.POST)
        if form.is_valid():
            job_listing, job_details = form.save()
            return redirect('listings')
    else:
        form = JobForm()
    
    return render(request, 'create_vaccancy.html', {'form': form})


def listings(request):
    jobs = JobListing.objects.all()
    return render(request, 'dashboard.html', {'jobs': jobs})


def screenshotview(request, job_id):
    job = get_object_or_404(JobListing, pk=job_id)
    return render(request, 'take_screenshot.html', {'job': job})


def take_screenshot(request, job_id):
    response = TakeScreenshot().take_screenshot(job_id)
    return HttpResponse(response)


def job_listing_details(request, job_listing_id):
    job_listing = get_object_or_404(JobListing, pk=job_listing_id)
    job_details = job_listing.details
    qualifications = job_details.qualifications.split('\n')
    responsibilities = job_details.responsibilities.split('\n')
    additional_info = job_details.additional_information.split('\n')

    context = {
        'job_listing': job_details.job_listing,
        'job_details': job_details,
        'qualifications_list': qualifications,
        'responsibilities': responsibilities,
        'additional_info': additional_info,
    }
    return render(request, 'job_detail.html', context)


def screenshot(request):
    return HttpResponse('hello')