from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, request
from .models import Item, Order
from delivery.models import Delivery
from users.models import Lionders_Users
from .forms import OrderForm, UpdateOrderForm, ItemForm
from users import models as usermodel
import datetime

# Create your views here.

# 사용자가 설정한 기간을 받아 주문 목록을 출력
def order_list(request):
    # if not request.user.is_authenticated:
    #     return HttpResponseRedirect('/signin/')
    # orders = Order.objects.filter(user_id=request.user.pk).order_by('created_at')
    period = request.POST.get('period', 0)
    period = int(period)
    current_date = datetime.date.today()
    if period == 0:
        orders = Order.objects.filter(normal_user_info=request.user).order_by('ordered_time')
    else:
        past_date = current_date - datetime.timedelta(days = period)
        current_date = current_date + datetime.timedelta(1)
        orders = Order.objects.filter(normal_user_info=request.user).order_by('ordered_time').filter(ordered_time__range=[past_date, current_date])
    context = {
        'orders': orders,
    }
    return render(request, 'order_list.html', context)

def order_detail(request, order_id):
    order = get_object_or_404(Order, pk=order_id)
    delivery = order.delivery_set.all()[0]
    return render(request, 'order_detail.html', {'order':order, 'delivery':delivery})

# item을 담아서 order_sheet를 만드는 함수
def order(request):
    if request.user.is_authenticated:
        if request.user.is_superuser:
            return redirect('login')
        elif request.user.usertype=="lionders":
            return redirect('login')
        else:
            all_items = Item.objects.all()
            total_price=0
            current_user = get_object_or_404(usermodel.Consumer_Users,pk = request.user.id)
            if current_user.have_order_sheet == False:
                new_order = Order(normal_user_info=current_user,total_price=0)
                new_order.save()
                current_user.have_order_sheet = True
                current_user.save()
                ordered_items = new_order.items.all()
                for item in ordered_items:
                    total_price += item.price
                ex_items = list(set(all_items) - set(ordered_items))
                stores = get_store(ex_items)
                item_list = slice_by_store(stores,ex_items)
                new_order.total_price = total_price
                new_order.save()
                return render(request,'order.html',{'all_items':all_items,'order':new_order,'ordered_items':ordered_items,'ex_items':ex_items,'total_price':total_price,'item_list':item_list})
            else:
                my_order = current_user.order_set.all().order_by('-ordered_time')
                order = my_order[0]
                ordered_items = my_order[0].items.all()
                for item in ordered_items:
                    total_price += item.price
                ex_items = list(set(all_items) - set(ordered_items))
                stores = get_store(ex_items)
                item_list = slice_by_store(stores,ex_items)
                order.total_price = total_price
                order.save()
                return render(request,'order.html',{'all_items':all_items,'order':order,'ordered_items':ordered_items,'ex_items':ex_items,'total_price':total_price,'item_list':item_list})
    else:
        return redirect('login')

def get_store(items):
    stores = []
    for item in items:
        if str(item.store) not in stores:
            stores.append(str(item.store))
    return stores


def slice_by_store(stores,items):
    list = []
    item_list = []
    for store in stores:
        for item in items:
            if str(store) == str(item.store):
                list.append(item)
        item_list.append(list)
    return item_list



def add_item(request,order_id,item_id):
    order = get_object_or_404(Order,pk=order_id)
    order.items.add(item_id)
    return redirect('order')


def remove_item(request,order_id,item_id):
    order = get_object_or_404(Order,pk=order_id)
    order.items.remove(item_id)
    return redirect('order')


def delete_item(requestm, item_id):
    item = get_object_or_404(Item,pk=item_id)
    item.delete()
    return redirect('create_objs')


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

def item_create(request):
    if request.method == 'POST':
        form = ItemForm(request.POST)
        request.POST._mutable = True
        # request.POST['user'] = request.user
        if form.is_valid():
            new_item = form.save()
        return HttpResponseRedirect('../order/orderlist')
    form = ItemForm()
    return render(request, 'item_create.html', {'form': form})

def make_order_final(request, order_id):
    order = get_object_or_404(Order,pk = order_id)
    items = order.items.all()
    current_user = get_object_or_404(usermodel.Consumer_Users,pk = request.user.id)
    if request.method == 'POST':
        order.destination_road = request.POST['destination_road']
        order.destination_derail = request.POST['destination_road']
        order.grade_limit = request.POST['lionders']
        order.can_delivery = True
        order.save()
        current_user.have_order_sheet = False
        current_user.save()
        return redirect('on_going')
    return render(request, 'order_final.html', {'items':items,'order':order,'user':current_user})


''' estimate lionders '''
def estimate_lionders(request, order_id, lionders_id):
    lionders = get_object_or_404(Lionders_Users, pk=lionders_id)
    order = get_object_or_404(Order, pk=order_id)
    if request.method == 'POST':
        point = request.POST.get('estimate', 0.0)
        point = float(point)
        rating_count = lionders.rating_count
        rating = lionders.rating

        rating_count = rating_count + 1
        rating = (rating + point) / rating_count

        lionders.rating_count = rating_count
        lionders.rating = rating
        lionders.save()
        delivery = order.delivery_set.all()[0]
        delivery.is_estimated = True
        delivery.save()
        return render(request, "estimate_complete.html")
    return render(request, "estimate_popup.html", {'lionders':lionders, 'order':order})