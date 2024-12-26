from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .models import FoundItem, FoundItemTimeline
from django.core.paginator import Paginator
from django.contrib import messages
from .decorators import admin_required
from .forms import FoundItemForm


from django.shortcuts import render

def custom_404_page(request, exception):
    return render(request, 'main/404.html', status=404)


@admin_required
def usersPage(request):
    users_list = User.objects.filter(is_superuser=False, is_staff=False)
    paginator = Paginator(users_list, 20)
    page = request.GET.get('page')
    users = paginator.get_page(page)
    for user in users:
        user.reported_items_count = FoundItem.objects.filter(user=user).count()
        user.claimed_items_count = FoundItemTimeline.objects.filter(user=user, activity_type = 'claimed').count()

    context = {
        'title': 'Users Management',
        'users': users
    }

    return render(request, 'main/users.html', context)




@admin_required
def claimsPage(request):
    context = {
        'title': 'Claims'
    }
    claims_all = FoundItemTimeline.objects.filter(activity_type='claimed').order_by('-timestamp')
    paginator = Paginator(claims_all, 15)
    page = request.GET.get('page')
    context['claims'] = paginator.get_page(page)
    return render(request, 'main/claims.html', context)

@login_required
def createFoundItem(request):
    if request.method == 'POST':
        form = FoundItemForm(request.POST, request.FILES)
        form.instance.user = request.user
        if form.is_valid():
            found_item = form.save(commit=False)
            found_item.user = request.user
            found_item.save()
            return redirect(reverse('found_items_details', args=[found_item.id]))
        else:
            errors = form.errors
            for field, error_list in errors.items():
                for error in error_list:
                    messages.error(request, f"{field}: {error}")
    else:
        form = FoundItemForm()
        
    return render(request, 'main/create_found_item.html', {'url': 'create_found_item', 'form': form, 'title': 'Create A Found Item'})

@admin_required
def claimDeny(request, id):
    found_item_timeline = get_object_or_404(FoundItemTimeline, pk=id)
    found_item_timeline.show_buttons = False
    found_item_timeline.save()
    FoundItemTimeline.objects.create(
        found_item=found_item_timeline.found_item,
        user=found_item_timeline.user,
        activity_type='denied'
    )
    return redirect(reverse('found_items_details', args=[found_item_timeline.found_item_id]))

@admin_required
def receiveItem(request, item_id):
    found_item = get_object_or_404(FoundItem, pk=item_id)
    found_item.admin_received = True
    found_item.save()
    FoundItemTimeline.objects.create(
        found_item=found_item,
        user=request.user,
        activity_type='collected'
    )
    return redirect(reverse('found_items_details', args=[item_id]))



@admin_required
def claimApprove(request, id):
    found_item_timeline = get_object_or_404(FoundItemTimeline, pk=id)
    found_item = get_object_or_404(FoundItem, pk=found_item_timeline.found_item_id)
    found_item.owner_collected = True
    found_item.save()
    FoundItemTimeline.objects.create(
        found_item=found_item,
        user=found_item_timeline.user,
        activity_type='verified'
    )
    return redirect(reverse('found_items_details', args=[found_item_timeline.found_item_id]))


@login_required
def claimItemPage(request, item_id):
    found_item = get_object_or_404(FoundItem, pk=item_id)
    if request.user == found_item.user:
        messages.error(request, "You cannot claim an Item you reported")
        return redirect(reverse('found_items_details', args=[item_id]))
    
    if FoundItemTimeline.objects.filter(found_item=found_item, user=request.user, activity_type='claimed').exists():
        messages.error(request, "You have already claimed this item.")
        return redirect(reverse('found_items_details', args=[item_id]))

    # Create a timeline record for claiming the item
    FoundItemTimeline.objects.create(
        found_item=found_item,
        user=request.user,
        activity_type='claimed'
    )

    messages.success(request, "Your claim request submitted")
    return redirect(reverse('found_items_details', args=[item_id]))



    

@login_required
def homePage(request):
    user = request.user
    found_items_list = FoundItem.objects.all().order_by('-date_reported')
    paginator = Paginator(found_items_list, 10)
    found_items = paginator.get_page(1)
    context = {
        'user': user,
        'title': 'Home',
        'found_items': found_items,
        'url': 'home'
    }
    if request.user.is_superuser:
        context['total_items_count'] = FoundItem.objects.count()
        context["items_inbound_count"] = FoundItem.objects.filter(admin_received=False).count()
        context["total_claims_count"] = FoundItem.objects.filter(owner_collected=True).count()
        context["claims_count"] = FoundItemTimeline.objects.filter(activity_type='claimed').count()

        context['claims'] = FoundItemTimeline.objects.filter(activity_type='claimed').order_by('-timestamp')[:10]
        return render(request, 'main/admin_home.html', context)
    else:
        return render(request, 'main/home.html', context)


@login_required
def foundItemsPage(request):
    user = request.user
    found_items_list = FoundItem.objects.all().order_by('-date_reported')
    paginator = Paginator(found_items_list, 15)
    page = request.GET.get('page')
    found_items = paginator.get_page(page)

    if request.method == 'POST':
        try:
            item_id = request.POST.get('item_id')
            fis = FoundItem.objects.filter(pk=int(item_id))
            if len(fis) == 1:
                return redirect(reverse('found_items_details', args=[fis[0].id]))
            else:
                messages.error(request, 'Invalid Item ID')
        except:
            messages.error(request, 'Invalid Item ID')

    context = {
        'user': user,
        'title': 'Found Items',
        'found_items': found_items,
        'url': 'found_items'
    }
    return render(request, 'main/found_items.html', context)


@login_required
def foundItemsDetail(request, item_id):
    found_item = get_object_or_404(FoundItem, pk=item_id)
    timeline_entries = found_item.founditemtimeline_set.all()


    context = {
        'title': found_item.item_name,
        'item': found_item,
        'timelines': timeline_entries
    }

    return render(request, 'main/found_item_details.html', context)