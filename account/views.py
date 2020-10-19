from django.shortcuts import render,redirect
from account.forms import UserRejestrionsForms,UserUpdateForm,ProfileUpadteForms
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User 


# Create your views here.

def register(request):
    if request.method =='POST':
        form = UserRejestrionsForms(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request,f'Account create for {username}.')
            return redirect('login')
    else:
        form = UserRejestrionsForms()
    return render(request,'register.html',{'form':form})


@login_required
def profile(request):
    if request.method == 'POST':
        uuser = UserUpdateForm(request.POST, instance=request.user)
        uprofile = ProfileUpadteForms(request.POST, request.FILES, instance=request.user.profile)

        if uuser.is_valid() and uprofile.is_valid():
            uuser.save()
            uprofile.save()
            messages.success(request, f'Account has been updated.')
            return redirect('profile')
    else:
        uuser = UserUpdateForm(instance=request.user)
        uprofile = ProfileUpadteForms(instance=request.user.profile)

    return render(request, 'profile.html', {'uuser': uuser, 'uprofile': uprofile})


