from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib import messages

from django.contrib.auth import login, authenticate
from django.contrib.auth.models import User

from .forms import RegistrationForm
from .models import Profile
# Create your views here.


def register(request):
    if request.method == 'POST':
        user_form = RegistrationForm(request.POST)
        if user_form.is_valid():
            new_user = User.objects.create(username=user_form.cleaned_data['username'],
                                           email=user_form.cleaned_data['email'])
            # Set the chosen password
            new_user.set_password(user_form.cleaned_data['password1'])
            # Save the User object
            new_user.save()
            # Create the user profile
            profile = Profile.objects.create(user=new_user,mobile=user_form.cleaned_data['mobile'])
            profile.save()
            return redirect('login.html')
    else:
        user_form = RegistrationForm()
    return render(request, 'register.html', {'user_form': user_form})


