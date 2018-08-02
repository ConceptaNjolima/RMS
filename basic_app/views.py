from django.shortcuts import render, redirect
from basic_app.forms import UserProfileInfoForm, Userform
from django.urls import reverse
from django.http import HttpResponseRedirect, HttpResponse
from basic_app.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages


# make the index view
def index(request):
    return render(request, 'index.html')


def tenantView(request):
    return render(request, 'tenant view.html')


@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('home'))


@login_required
def special(request):
    return HttpResponse("You are logged In")


# make the registration view
def register(request):
    registered = False
    if request.method == 'POST':
        user_form = Userform(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            # then here you can harsh
            user.set_password(user.password)
            # then can save again
            user.save()

            profile = profile_form.save(commit=False)
            # then set the one to one relationship between user form and user info form
            profile.user = user
            registered = True

    # if there was nothing submitted, render the form as blank to be refilled
    else:
        user_form = Userform()
        profile_form = UserProfileInfoForm()

    return render(request, 'register.html',
                  {'user_form': user_form, 'profile_form': profile_form, 'registered': registered}
                  )


def user_login(request):
    if request.method == 'POST':
        user_name = request.POST.get('username')
        password = request.POST.get('password')
        # after grabbing the fields we need to autheticate
        user = authenticate(username=user_name, password=password)
        if user:
            if user.is_active:
                login(request, user)

                return HttpResponseRedirect(reverse('basic_app:tenantView'))

            else:
                return HttpResponse("your account is not active")
        else:
            return HttpResponse('Invalid log in details')
    else:
        return render(request, 'login.html', {'login': login})


def manager_login(request):
    if request.method == 'POST':
        user_name = request.POST.get('username')
        password = request.POST.get('password')
        # after grabbing the fields we need to autheticate
        user = authenticate(username=user_name, password=password)
        if user:
            if user.is_staff:
                login(request, user)

                return HttpResponseRedirect(reverse('basic_app:welcomeManager'))

            else:

                return HttpResponse("YOU ARE NOT A REGISTERED USER")
        else:
            return HttpResponse('Invalid log in details')
    else:
        return render(request, 'login.html', {'login': login})


def welcomeManager(request):
    return render(request, 'welcomeManager.html')


def manager(request, ):
    user_list = User.objects.all()
    return render(request, 'manager.html', {'user_list': user_list})


# def delete_tenant(request, pk):
#     tenant_list = User.objects.get(username=pk)
#     tenant_list.delete()
#     messages.success(request, 'item removed')
#     return redirect('manager.html')
