'''
user api routes/endpoints.
'''
from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenBlacklistView
from . import views

urlpatterns = [
    path('signup/', views.UserCreate.as_view(), name="user_create"),
    path('activate/<uidb64>/<token>/', views.UserActivate.as_view(), name='user_activate'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('list/', views.UserList.as_view(), name="user_list"),
    path('logout/', views.UserLogout.as_view(), name="user_logout"),
]