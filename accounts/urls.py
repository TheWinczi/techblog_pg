from django.urls import path
from accounts import views

urlpatterns = [
    path('login/', views.user_login, name='login'),
    path('logout/', views.user_logout, name='logout'),
    path('logout/done/', views.user_logout_done, name='logout_done'),
    path('register/', views.user_register, name='register'),
    path('register/done/', views.user_register_done, name='register_done'),
]
