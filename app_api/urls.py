from .views import *
from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r'company', CompanyView)
router.register(r'industry', IndustryView)
# router.register(r'job-vaccancy', JobVaccancyView)
router.register(r'joblistings', JobListingView)
router.register(r'specialities', SpecialitiesView)
router.register(r'skills', SkillsView)
router.register(r'job-content', AdditionalInfoView)


urlpatterns = router.urls