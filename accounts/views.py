from django.shortcuts import render
from django.http.request import HttpRequest
from django.contrib.auth import authenticate, login, logout
from django.http.response import HttpResponse, HttpResponseRedirect
from django.contrib.auth.models import Group

from rest_framework import status

from accounts.models import CustomUser



def user_login(request: HttpRequest):
    method = request.method
    if method == 'POST':
        data = request.POST
        email, password = data.get('email', ''), data.get('password', '')
        user = authenticate(request, email=email, password=password)
        if user is None:
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)
        login(request, user)
        return HttpResponse(status=status.HTTP_200_OK)
    else:
        return render(request, 'accounts/registration/login.html')


def user_logout(request: HttpRequest):
    logout(request)
    request.session.clear()
    response = HttpResponseRedirect('/logout/done/')
    response.delete_cookie("csrftoken", path="/", samesite='none')
    response.delete_cookie("sessionid", path="/", samesite='none')
    return response


def user_logout_done(request: HttpRequest):
    return render(request, 'accounts/registration/logout_done.html')


def user_register(request: HttpRequest):
    method = request.method
    if method == 'POST':
        data = request.POST
        email, password = data.get('email', ''), data.get('password', '')
        try:
            user_group = Group.objects.get(name='user')
        except Group.DoesNotExist:
            print('User group does not exist')
            return HttpResponse(status=status.HTTP_404_NOT_FOUND)

        try:
            CustomUser.objects.get(email=email)
            return HttpResponse(status=status.HTTP_400_BAD_REQUEST)
        except CustomUser.DoesNotExist:
            user = CustomUser.objects.create_user(email=email, password=password)
            user.groups.add(user_group)
            return HttpResponse(status=status.HTTP_201_CREATED)
    else:
        return render(request, 'accounts/registration/register.html')


def user_register_done(request: HttpRequest):
    return render(request, 'accounts/registration/register_done.html')