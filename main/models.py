from django.db import models
from django.contrib.auth.models import User

    
class FoundItem(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    item_name = models.CharField(max_length=100)
    description = models.TextField()
    date_found = models.DateField()
    location_found = models.CharField(max_length=100)
    contact_info = models.CharField(max_length=100)
    date_reported = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='found_item_images/', blank=True, null=True)
    admin_received = models.BooleanField(default=False)
    owner_collected = models.BooleanField(default=False)

    def __str__(self):
        return self.item_name
    
    def save(self, *args, **kwargs):
        is_new_item = self.pk is None
        super(FoundItem, self).save(*args, **kwargs)

        if is_new_item:
            FoundItemTimeline.objects.create(
                found_item = self,
                user= self.user,
                activity_type = 'reported'
            )
    
class FoundItemTimeline(models.Model):
    ACTIVITY_CHOICES = (
        ('reported', 'Item Reported'),
        ('denied', 'Item Denied to User'),
        ('claimed', 'Item Claimed'),
        ('verified', 'User Verified'),
        ('collected', 'Item Collected')
    )
    found_item = models.ForeignKey(FoundItem, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    activity_type = models.CharField(max_length=10, choices=ACTIVITY_CHOICES)
    timestamp = models.DateTimeField(auto_now_add=True)
    show_buttons = models.BooleanField(default=True)
    denied_to = models.CharField(max_length=100, null=True)

    def __str__(self):
        return f"{self.get_activity_type_display()} on {self.timestamp}"