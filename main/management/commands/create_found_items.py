from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
import random
import string
import os
from main.models import FoundItem

class Command(BaseCommand):
    help = 'Create random users with specified attributes'

    def handle(self, *args, **kwargs):
        folder_path = './found_items'
        for folder_name in os.listdir(folder_path):
            folder = os.path.join(folder_path, folder_name)
            if os.path.isdir(folder):
                description_file = os.path.join(folder, 'description.txt')
                image_file = os.path.join(folder, 'image.jpg')

                if os.path.exists(description_file) and os.path.exists(image_file):
                    with open(description_file, 'r') as f:
                        description = f.read()

                    user = User.objects.order_by('?').first()

                    found_item = FoundItem(
                        user=user,
                        item_name = f'Random Item {random.randint(1, 100)}',
                        description = description,
                        date_found = f'2023-{random.randint(1, 12)}-{random.randint(1, 28)}',
                        location_found = f'Location {random.randint(1, 20)}',
                        contact_info = f'Contact {random.randint(1, 10)}'
                    )

                    with open(image_file, 'rb') as img_file:
                        found_item.image.save('image_2.jpg', img_file, save=True)

                    found_item.save()

                    self.stdout.write(self.style.SUCCESS(f'Successfully created FoundItem from {folder_name}'))



