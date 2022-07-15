from django.core.management.base import BaseCommand 
from api.models import Link
from datetime import timedelta
from django.utils import timezone

class Command(BaseCommand):

    '''In the description there was a task for automatic deletion of 
    url entries that were older than 30 days so i created this class and used a cron job
    to delete the entries every 30 minuts.'''

    help = 'Used to delete short urls that are older than 30 days'

    def handle(self, *args, **kwargs):
        days = 30
        urls = Link.objects.filter(created__lte=timezone.now() - timedelta(days=days))
        if not urls:
            self.stdout.write("There are no entries older than 30 days for now.")

        for url in urls:
            
            Link.objects.get(id=url.id)
            url.delete()

            self.stdout.write("deleted")