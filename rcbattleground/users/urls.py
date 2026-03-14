
from django.urls import path

from .views import RegisterView, CustomTokenObtainPairView
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)

urlpatterns = [
  # http://127.0.0.1:8000/api/auth/register/
    path('register/', RegisterView.as_view(), name='register'),
    
    # http://127.0.0.1:8000/api/auth/login/
    path('login/', CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    
    # http://127.0.0.1:8000/api/auth/token/refresh/
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
  
]
