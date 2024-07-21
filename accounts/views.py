from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import AuthenticationForm
from .forms import UserRegistrationForm
from .models import UserProfile

from .forms import UserRegistrationForm

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts:login')  # 登録後にログインページへリダイレクト
    else:
        form = UserRegistrationForm()
    return render(request, 'accounts/register.html', {'form': form})

def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            try:
                user_profile = user.userprofile
            except UserProfile.DoesNotExist:
                user_profile = UserProfile.objects.create(user=user)

            if user_profile.is_owner:
                return redirect('accounts:owner_profile')  # オーナープロフィールページにリダイレクト
            else:
                return redirect('accounts:guest_profile')  # ゲストプロフィールページにリダイレクト
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

@login_required
def guest_profile(request):
    if request.user.userprofile.is_owner:
        return HttpResponseForbidden("You do not have permission to access this page.")
    return render(request, 'accounts/guest_profile.html')

@login_required
def owner_profile(request):
    if not request.user.userprofile.is_owner:
        return HttpResponseForbidden("You do not have permission to access this page.")
    return render(request, 'accounts/owner_profile.html')