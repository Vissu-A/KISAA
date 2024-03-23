'''
user api routes/endpoints.
'''
from django.urls import path, re_path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from . import views

urlpatterns = [
    path('signup/', views.user_signup, name = "user_signup"),
    path('activate/?P<userid>/?P<token>/', views.activate_account, name = 'user_activate'),
    path('list/', views.get_user_list, name = "user_list"),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]