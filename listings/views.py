from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Listing
from .forms import ListingForm

@login_required
def add_listing(request):
    if request.method == 'POST':
        form = ListingForm(request.POST)
        if form.is_valid():
            listing = form.save(commit=False)
            listing.owner = request.user
            try:
                listing.save()
            except Exception as e:
                print(f"Error: {e}")  # エラーの詳細をコンソールに出力
            return redirect('listing_list')
    else:
        form = ListingForm()
    return render(request, 'listings/add_listing.html', {'form': form})

@login_required
def listing_list(request):
    listings = Listing.objects.all()
    return render(request, 'listings/listing_list.html', {'listings': listings})