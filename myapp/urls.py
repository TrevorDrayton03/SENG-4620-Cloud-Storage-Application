from django.urls import path, include
from django.contrib import admin

from . import views

urlpatterns = [
    path('', views.home, name='home'),	
    path('logout', views.logout_view, name="logout_view"),
    path('register/', views.register_view, name="register_view"),	
    path('profile/', views.profile_view, name="profile_view"),
    path('upload/', views.upload_view, name="upload_view"),
    path('download/<username>/<filename>/', views.download_view, name="download_view"),
    path('delete/<username>/<filename>/', views.delete_view, name="delete_view"),
    path('process/', views.process, name="process"),
    # path(r'^password/change/$', auth_views.password_change, name='auth_password_change'),
    # path(r'^password/change/done/$', auth_views.password_change_done,  name='auth_password_change_done'),
]