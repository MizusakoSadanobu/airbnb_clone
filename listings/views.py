from django.shortcuts import render
from .models import Listing

from django.shortcuts import render, redirect
from .forms import ListingForm


def listing_list(request):
    listings = Listing.objects.all()
    return render(request, 'listings/listing_list.html', {'listings': listings})

def add_listing(request):
    if request.method == 'POST':
        form = ListingForm(request.POST)
        if form.is_valid():
            form.save()  # フォームの内容を保存
            return redirect('listing_list')  # リストページにリダイレクト
    else:
        form = ListingForm()  # 空のフォームを作成

    return render(request, 'listings/add_listing.html', {'form': form})

from django.contrib.auth import login, authenticate
from .forms import UserRegistrationForm

def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            new_user = form.save(commit=False)
            new_user.set_password(form.cleaned_data['password'])
            new_user.save()
            login(request, new_user)
            return redirect('dashboard')
    else:
        form = UserRegistrationForm()
    return render(request, 'listings/register.html', {'form': form})

from django.contrib.auth.decorators import login_required

@login_required
def profile(request):
    return render(request, 'listings/profile.html')