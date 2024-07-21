from  django.urls import path
from . import views

urlpatterns = [
  path('register/', views.registration, name='register'),
  path('', views.home, name='home'),
  path('login/', views.user_login, name='login'),
  path('change-password/', views.change_password, name='change_password'),
  path('update-profile/', views.update_profile, name='update_profile'),
  path('delete-account/', views.delete_account, name='delete_account'),
]