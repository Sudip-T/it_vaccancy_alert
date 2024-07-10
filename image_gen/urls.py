from django.urls import path
from . import views

urlpatterns = [
    path('', views.listings, name='listings'),
    path('gett/', views.gett, name='gett'),
    path('screenshot/', views.screenshot, name='screenshot'),
    path('create/', views.create_listing, name='create_listing'),
    path('job/<int:job_id>/', views.screenshotview, name='screenshotview'),
    path('job/take_screenshot/<int:job_id>/', views.take_screenshot, name='take_screenshot'),
    path('jobs/<int:job_listing_id>/', views.job_listing_details, name='job_listing_details'),
]
