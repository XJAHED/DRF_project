from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()


router.register('member', memberviewset)

urlpatterns = router.urls
