from django.core.management.base import BaseCommand
from listings.models import Listing
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Deletes all data from the listings and user models'

    def handle(self, *args, **kwargs):
        Listing.objects.all().delete()
        User.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Successfully deleted all listings and users'))
