from functools import wraps
from django.contrib import messages
from django.shortcuts import redirect

def admin_required(view_func):
    @wraps(view_func)
    def _wrapped_view(request, *args, **kwargs):
        if not request.user.is_staff: 
            messages.error(request, "Restricted Route!")
            return redirect('home')  # Redirect to the login page or another page
        return view_func(request, *args, **kwargs)
    return _wrapped_view
