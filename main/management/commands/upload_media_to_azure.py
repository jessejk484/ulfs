from django.core.management.base import BaseCommand
from azure.storage.blob import BlobServiceClient
from django.conf import settings
import os 

class Command(BaseCommand):
    help = 'Upload media files to Azure Blob Storage'

    def handle(self, *args, **options):
        container_name = 'static'
        AZURE_ACCOUNT_KEY = settings.AZURE_ACCOUNT_KEY  # or use settings.AZURE_ACCOUNT_KEY
        AZURE_ACCOUNT_NAME = settings.AZURE_ACCOUNT_NAME
        blob_service_client = BlobServiceClient(account_url=f"https://{AZURE_ACCOUNT_NAME}.blob.core.windows.net", credential=AZURE_ACCOUNT_KEY)
        container_client = blob_service_client.get_container_client(container_name)

        # Collect and upload media files to the Azure Blob Storage container
        media_root = settings.MEDIA_ROOT
        for root, dirs, files in os.walk(media_root):
            for file in files:
                media_file_path = os.path.join(root, file)
                blob_name = os.path.join("eastus2/", os.path.relpath(media_file_path, media_root).replace("\\", "/"))
                blob_client = container_client.get_blob_client(blob_name)

                with open(media_file_path, 'rb') as data:
                    blob_client.upload_blob(data)

        self.stdout.write(self.style.SUCCESS('Successfully uploaded media files to Azure Blob Storage.'))