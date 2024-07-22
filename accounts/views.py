from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.contrib.auth import authenticate, login, logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import Group
from .forms import UserRegistrationForm
from .models import UserProfile

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            
            # ユーザータイプの設定
            user_profile = UserProfile(user=new_user)
            user_profile.user_type = form.cleaned_data['role']
            user_profile.save()

            # グループの設定
            if form.cleaned_data['role'] == 'owner':
                group = Group.objects.get(name='Owner')
            else:
                group = Group.objects.get(name='Guest')
            new_user.groups.add(group)
            new_user.save()

            login(request, new_user)
            return redirect('listing_list')
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
                print(f"UserProfile Exists {user_profile.user_type}")
            except UserProfile.DoesNotExist:
                print("UserProfile Does Not Exist")
                user_profile = UserProfile.objects.create(user=user)

            if user_profile.user_type=="owner":
                return redirect('accounts:owner_profile')  # オーナープロフィールページにリダイレクト
            else:
                return redirect('accounts:guest_profile')  # ゲストプロフィールページにリダイレクト
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})

@login_required
def guest_profile(request):
    if request.user.userprofile.user_type!="guest":
        return HttpResponseForbidden("You do not have permission to access this page.")
    return render(request, 'accounts/guest_profile.html')

@login_required
def owner_profile(request):
    if request.user.userprofile.user_type!="owner":
        return HttpResponseForbidden("You do not have permission to access this page.")
    return render(request, 'accounts/owner_profile.html')

def logout_view(request):
    auth_logout(request)
    return redirect('listing_list')