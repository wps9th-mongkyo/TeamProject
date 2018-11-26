import logging

from django.contrib.auth import get_user_model
from django.core.management import BaseCommand
from django.utils.crypto import get_random_string

User = get_user_model()
logger = logging.getLogger(__name__)

class Command(BaseCommand):
    def handle(self, *args, **options):
        username = f'dummy_{get_random_string(length=10)}'
        User.objects.create_user(username=username)
        print(f'User {username} created')