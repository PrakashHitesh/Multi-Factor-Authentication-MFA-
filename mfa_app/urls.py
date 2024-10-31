from django.urls import path
from .views import signup, login_view, generate_mfa, verify_mfa, dashboard, logout_view

urlpatterns = [
    path('signup/', signup, name='signup'),
    path('login/', login_view, name='login'),
    path('generate_mfa/', generate_mfa, name='generate_mfa'),
    path('verify_mfa/', verify_mfa, name='verify_mfa'),
    path('dashboard/', dashboard, name='dashboard'),
    path('logout/', logout_view, name='logout'),
]
