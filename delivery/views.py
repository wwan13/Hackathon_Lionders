from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, request
from .models import Item, Order, Delivery
from .forms import OrderForm, UpdateOrderForm, ItemForm
from django.shortcuts import render, get_object_or_404, redirect
# Create your views here.

def order_list(request):
    # if not request.user.is_authenticated:
    #     return HttpResponseRedirect('/signin/')
    # orders = Order.objects.filter(user_id=request.user.pk).order_by('created_at')
    orders = Order.objects.filter()
    context = {
        'orders': orders,
    }
    return render(request, 'order_list.html', context)


def order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        request.POST._mutable = True
        # request.POST['user'] = request.user
        if form.is_valid():
            new_item = form.save()
        return HttpResponseRedirect('../order/orderlist')
    form = OrderForm(request.FILES)
    return render(request, 'order.html', {'form': form})


def order_delete(request, id):
    item = get_object_or_404(Order, pk=id)
    if request.method == 'POST':
        item.delete()
        return redirect('order-list')  # 리스트 화면으로 이동합니다.
    return render(request, 'order_delete.html', {'item': item})


def order_update(request):
    if request.method == 'POST' and 'id' in request.POST:
        item = get_object_or_404(Order, pk=request.POST.get('id'))
        form = UpdateOrderForm(request.POST, instance=item)
        if form.is_valid():
            item = form.save()

    elif 'id' in request.GET:
        item = get_object_or_404(Order, pk=request.GET.get('id'))
        form = OrderForm(instance=item)
        return render(request, 'order_update.html', {'form': form})
    return HttpResponseRedirect("../orderlist")


def delivery_list(request):
    deliveries = Delivery.objects.filter()
    context = {
        'deliveries': deliveries,
    }
    return render(request, 'delivery_list.html', context)

def delivery(request):
    if request.method == 'POST':
        delivery_form = DeliveryForm(request.POST)
        request.POST._mutable = True
        # request.POST['user'] = request.user
        if delivery_form.is_valid():
            delivery_form.save()
        return redirect('delivery_list')
    form = DeliveryForm()
    return render(request, 'delivery.html', {'delivery_form': form})

def delivery_update(request):
    pass

def delivery_delete(request):
    pass