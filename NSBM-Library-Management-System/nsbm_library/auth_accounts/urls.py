# from rest_framework.routers import DefaultRouter
# from .views import *

# router=DefaultRouter()

# router.register('signup', signup)

# urlpatterns = router.urls

from django.urls import path
from .views  import *

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('signup/', signup.as_view(), name='signup'),
    
    path('signin/', TokenObtainPairView.as_view(), name='signin'),

    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
