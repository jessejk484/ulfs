from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
import random
import string

class Command(BaseCommand):
    help = 'Create random users with specified attributes'

    def handle(self, *args, **kwargs):
        for _ in range(100):  # Create 100 random users
            first_name = ''.join(random.choices(string.ascii_uppercase, k=5))
            last_name = ''.join(random.choices(string.ascii_uppercase, k=5))
            username = ''.join(random.choices(string.ascii_lowercase, k=5))
            email = f'{username}@my.unt.edu'
            password = ''.join(random.choices(string.ascii_letters + string.digits, k=10))

            User.objects.create_user(username=username, email=email, password=password, first_name=first_name, last_name=last_name)
            self.stdout.write(self.style.SUCCESS(f'Successfully created user: {username}'))
