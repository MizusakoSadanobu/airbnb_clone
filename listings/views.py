from django.shortcuts import render
from .models import Listing

def listing_list(request):
    listings = Listing.objects.all()
    return render(request, 'listings/listing_list.html', {'listings': listings})
