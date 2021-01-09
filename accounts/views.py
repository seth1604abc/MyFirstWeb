from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from commodity.models import Order

def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.info(request, '帳號或是密碼錯誤')
    context = {}
    return render(request, 'login.html', context=context)

def logoutPage(request):
    if request.method == 'POST':
        logout(request)
        return redirect('/')


def signup(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, '註冊成功')
            return redirect('login')
    context = {'form': form}
    return render(request, 'signup.html', context=context)

@login_required(login_url='login')
def customers(request):
    user_id = request.user.id
    orders = Order.objects.filter(user_id=user_id)
    context = {'orders': orders}
    return render(request, 'customer.html', context=context)