from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.conf import settings
import pyotp, qrcode
from io import BytesIO
import base64
from .models import Profile
from .forms import CustomUserCreationForm, AuthenticationForm

# User Signup
def signup(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            Profile.objects.create(user=user)  # Create a Profile for MFA
            return redirect('login')
    else:
        form = CustomUserCreationForm()
    return render(request, 'mfa_app/signup.html', {'form': form})

# User Login
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('generate_mfa')
    else:
        form = AuthenticationForm()
    return render(request, 'mfa_app/login.html', {'form': form})

# Generate MFA
@login_required
def generate_mfa(request):
    profile = request.user.profile
    mfa_secret = pyotp.random_base32()
    profile.mfa_secret = mfa_secret
    profile.save()

    totp = pyotp.TOTP(mfa_secret)
    qr_code_url = totp.provisioning_uri(request.user.username, issuer_name="MFA_Demo")

    qr = qrcode.QRCode(version=1, box_size=10, border=5)
    qr.add_data(qr_code_url)
    qr.make(fit=True)
    img = qr.make_image(fill='black', back_color='white')

    buffer = BytesIO()
    img.save(buffer)
    qr_code_image = base64.b64encode(buffer.getvalue()).decode('utf-8')

    return render(request, 'mfa_app/generate_mfa.html', {'qr_code': qr_code_image})

# Verify MFA
@login_required
def verify_mfa(request):
    if request.method == 'POST':
        token = request.POST.get('token')
        profile = request.user.profile
        totp = pyotp.TOTP(profile.mfa_secret)
        if totp.verify(token):
            profile.mfa_enabled = True
            profile.save()
            return redirect('dashboard')
        else:
            return render(request, 'mfa_app/verify_mfa.html', {'error': 'Invalid token'})
    return render(request, 'mfa_app/verify_mfa.html')

# Dashboard
@login_required
def dashboard(request):
    return render(request, 'mfa_app/dashboard.html')

# Logout
def logout_view(request):
    logout(request)
    return redirect('login')
