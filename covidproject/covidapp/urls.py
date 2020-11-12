from rest_framework import routers
from .api import RegisterViewset

router = routers.DefaultRouter()
router.register('api/covidapp/register', RegisterViewset, "register")

urlpatterns = router.urls