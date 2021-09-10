from django.conf.urls import url
from apps.user import views
from django.urls import path, include

urlpatterns = [
    path('register', views.UserRegisterAPIView.as_view()),
    path('login', views.UserLoginAPIView.as_view()),
    path('logout', views.UserLogoutAPIView.as_view()),
    path('center', views.UserCenterAPIView.as_view()),
]
