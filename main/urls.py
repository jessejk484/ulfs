from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name='home'),
    path('found-items/', views.foundItemsPage, name = 'found_items'),
    path('found-items/details/<int:item_id>', views.foundItemsDetail, name='found_items_details'),
    path('claim_item/<int:item_id>', views.claimItemPage, name='claim_item'),
    path('claim_approve/<int:id>', views.claimApprove, name='claim_approve'),
    path('claim_deny/<int:id>', views.claimDeny, name='claim_deny'),
    path('receive_item/<int:item_id>', views.receiveItem, name='receive_item'),
    path('create_found_item/', views.createFoundItem, name= 'create_found_item'),
    path('claims/', views.claimsPage, name='claims'),
    path('users/', views.usersPage, name='users')
]