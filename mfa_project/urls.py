from django.contrib import admin
from django.urls import path, include
from django.shortcuts import redirect

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', lambda request: redirect('login')),  # Redirect root URL to login page
    path('signup/', include('mfa_app.urls')),
    path('login/', include('mfa_app.urls')),
    path('generate_mfa/', include('mfa_app.urls')),
    path('verify_mfa/', include('mfa_app.urls')),
    path('dashboard/', include('mfa_app.urls')),
    path('logout/', include('mfa_app.urls')),
]
