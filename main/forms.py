from django import forms
from .models import FoundItem

class FoundItemForm(forms.ModelForm):
    class Meta:
        model = FoundItem
        fields = ['item_name', 'description', 'date_found', 'location_found', 'contact_info', 'image']

    item_name = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control form-control-lg'}))
    date_found = forms.DateField(widget=forms.DateInput(attrs={'class': 'form-control form-control-lg'}))
    location_found = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
    contact_info = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control form-control-lg'}))
    image = forms.ImageField(widget=forms.ClearableFileInput(attrs={'class': 'custom-image-input'}))

