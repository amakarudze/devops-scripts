from django.urls import path

from . import views

urlpatterns = [
    path('user-view', views.UserApiView.as_view()),
]
