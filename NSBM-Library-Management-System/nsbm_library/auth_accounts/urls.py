from django.urls import path
from .views  import *

from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('signup/', signup.as_view(), name='signup'),
    
    path('signin/', EmailTokenView.as_view(), name='signin'),

    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
