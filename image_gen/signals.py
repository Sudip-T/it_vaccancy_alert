from .models import JobListing
from .utility import TakeScreenshot
from django.dispatch import receiver
from django.db.models.signals import post_save


# @receiver(post_save, sender=JobListing)
# def take_screenshot(sender, instance, created, **kwargs):
#     if created:
#         try:
#             TakeScreenshot().take_screenshot(instance.id)
#         except Exception as e:
#             print(f"Error taking screenshot: {e}")