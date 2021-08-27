from django.conf.urls import url
from apps.user import views
from django.urls import path, include

urlpatterns = [
    path('center', views.UserView.as_view()),
]
