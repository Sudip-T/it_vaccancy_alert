from django.urls import path
from rest_framework.routers import SimpleRouter
from .views import IndustryView, JobVaccancyView

router = SimpleRouter()
router.register(r'it-industry', IndustryView)
router.register(r'job-vaccancy', JobVaccancyView)


urlpatterns = router.urls