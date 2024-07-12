from .views import *
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r'company', CompanyView)
router.register(r'it-industry', IndustryView)
# router.register(r'job-vaccancy', JobVaccancyView)
router.register(r'joblistings', JobListingView)


urlpatterns = router.urls