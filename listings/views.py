from django.shortcuts import render, redirect
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from .models import Listing
from .forms import ListingForm
# from .decorators import owner_required

@login_required
# @owner_required
def add_listing(request):
    if request.user.userprofile.user_type != "owner":
        return HttpResponseForbidden("You do not have permission to access this page.")
    
    if request.method == 'POST':
        form = ListingForm(request.POST)
        if form.is_valid():
            listing = form.save(commit=False)
            listing.owner = request.user
            listing.save()
            return redirect('listing_list')
    else:
        form = ListingForm()
    return render(request, 'listings/add_listing.html', {'form': form})

def listing_list(request):
    listings = Listing.objects.all()
    is_owner = request.user.userprofile.user_type == "owner" if request.user.is_authenticated else False
    return render(request, 'listings/listing_list.html', {'listings': listings, 'is_owner': is_owner})