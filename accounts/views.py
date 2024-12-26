from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from .models import OTP
from django.contrib import messages
from .utils import send_email, send_otp_mail
from .forms import CustomUserRegistrationForm
import random

def logoutPage(request):
    logout(request)
    return redirect('home')

def otpPage(request):
    resend = request.GET.get('resend')
    user_id = request.session.get('user_id')
    print(user_id)
    user = None
    if user_id:
        user = User.objects.get(id=user_id)
    if resend and user and request.method == 'GET':
        OTP.objects.filter(user=user).delete()
        otp_code = str(random.randint(100000, 999999))
        print(otp_code, user.id)
        otp = OTP(user=user, otp=otp_code)
        otp.save()
        send_otp_mail(user.email, otp_code, user)
        messages.success(request, 'OTP Sent Successfully!')

    if request.method == 'POST':
        otp = request.POST.get('otp')
        db_otp = OTP.objects.get(user=user)
        if otp is None:
            messages.error(request, 'Please enter the OTP!')
        elif int(otp) == db_otp.otp and not db_otp.is_expired():
            user.is_active = 1
            user.save()
            login(request, user)
            return redirect('home')
        elif db_otp.is_expired():
            messages.error(request, "OTP Expired, sent a new OTP")
            OTP.objects.filter(user=user).delete()
            otp_code = str(random.randint(100000, 999999))
            print(otp_code, user.id)
            otp = OTP(user=user, otp=otp_code)
            otp.save()
            send_otp_mail(user.email, otp_code, user)
            messages.success(request, 'OTP Sent Successfully!')
        else:
            messages.error(request, "Invalid OTP, Reenter Correct OTP!")
    context = {
        'title': 'OTP Confirmation'
    }
    return render(request, 'accounts/otp_form.html', context)

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)

            if str(user) == 'sa':
                return redirect('sa_home')
            return redirect('home')
        else:
            messages.error(request, 'Invalid Credentials')
    if request.user.is_authenticated:
        return redirect('home')
    context = {
        'title': 'Login',
    }
    return render(request, 'accounts/login.html',context)

def registerPage(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        if email.split("@")[1].strip() != 'my.unt.edu':
            messages.error(request, 'Only UNT Email Ids are allowed')
        else:
            form = CustomUserRegistrationForm(request.POST)
            if form.is_valid():
                print("Valid Form")
                user = form.save(commit=False)
                user.email = form.cleaned_data['email']
                user.is_active = False
                user.save()

                otp_code = str(random.randint(100000, 999999))
                otp = OTP(user=user, otp=otp_code)
                otp.save()

                send_otp_mail(email, otp_code, user)
                print(user.id)
                request.session['user_id'] = user.id
                return redirect('otp')
            else:
                errors = form.errors
                for field, error_list in errors.items():
                    for error in error_list:
                        messages.error(request, f"{field}: {error}")


    if request.user.is_authenticated:
        return redirect('home')
    context = {
        'title': 'Register',
    }
    return render(request, 'accounts/register.html',context)

# def logoutPage(request):
#     logout(request)
#     return redirect('home')

# def redirectPage(request):
#     code = request.GET.get('code', None)
#     if not code:
#         return render(request, 'dashboard/500.html')
#     flag, response = get_token_by_code(code)
#     if flag:
#         return render(request, 'dashboard/500.html')
#     try:
#         user_email = response['id_token_claims']['preferred_username']
#         user = User.objects.get(email__iexact=user_email)
#         if not user.first_name:
#             user.first_name = response['id_token_claims']['name']
#             user.save()
#         login(request, user)
#         return redirect('home')
#     except Exception as e:
#         print(e)
#         return render(request, 'accounts/login.html')