from rest_framework.routers import DefaultRouter
from .views import *

router = DefaultRouter()

router.register('issuebook', IssueViewSet)

urlpatterns = router.urls