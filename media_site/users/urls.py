from . import views
from django.urls import path
from rest_framework_simplejwt.views import (
    TokenRefreshView,TokenBlacklistView
)

app_name = 'users'

urlpatterns = [
    path('register/',views.RegisterAPIView.as_view(),name="register"),
    path('login/',views.LoginAPIView.as_view(),name="login"),
    path('logout/', TokenBlacklistView.as_view(), name='token_blacklist'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('<int:pk>/', views.RetrieveUpdateDeleteItem.as_view(),name='profile'),
]