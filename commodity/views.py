from django.shortcuts import render, redirect
from .models import Commodity, Order, Song
from django.contrib.auth.decorators import login_required

def commodity(request):
    goods = Commodity.objects.all()
    context = {'goods': goods}
    return render(request, 'commodity.html', context=context)

def detail(request, pk):
    merch = Commodity.objects.get(id=pk)
    songs = Song.objects.filter(album_id=pk)
    context = {'merch': merch, 'songs': songs}
    return render(request, 'detail.html', context=context)

@login_required(login_url='login')
def order(request, pk):
    confirm = Commodity.objects.get(id=pk)
    context = {'confirm': confirm}
    return render(request, 'order.html', context=context)

@login_required(login_url='login')
def information(request, pk):
    commodity = Commodity.objects.get(id=pk)
    orders = Order()
    if request.method == 'POST':
        if request.POST['name'] and request.POST['phone'] and request.POST['address'] and request.POST['pay']:
            orders.name = request.POST['name']
            orders.phone = request.POST['phone']
            orders.address = request.POST['address']
            orders.pay = request.POST['pay']
            orders.user = request.user
            orders.product = commodity
            orders.save()
            return redirect('/')
        else:
            return render(request, 'information.html')
    context = {'orders': orders}
    return render(request, 'information.html', context=context)


