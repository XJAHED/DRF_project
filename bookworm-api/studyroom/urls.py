from .views import *
from rest_framework.routers import DefaultRouter

router=DefaultRouter()

router.register('room', room)
router.register('studyroom', study_room)

urlpatterns = router.urls
