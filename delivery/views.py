from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, request, response
from .models import Delivery
from .forms import DeliveryForm, UpdateDeliveryForm
from users import models as usermodel
from order import models as ordermodel
# Create your views here.


# def delivery_list(request):
#     if not request.user.is_authenticated:
#         return HttpResponseRedirect('/signin/')
#     if request.user.usertype == 'lionders':
#         deliveries = Delivery.objects.filter(order_sheet__destination = request.user.address, lionders_info_id=request.user.pk)
#         context = {
#             'deliveries': deliveries,
#         }
#         return render(request, 'delivery_list.html', context)
#     else :
#         deliveries = Delivery.objects.filter(lionders_info_id=request.user.pk)
#         context = {
#             'deliveries': deliveries,
#         }
#         return render(request, 'delivery_list.html', context)


def delivery_list(request):
    orders = ordermodel.Order.objects.filter(is_complete=False)
    return render(request,'delivery_list.html',{'orders':orders})


def make_delivery(request, order_id):
    current_user = get_object_or_404(usermodel.Lionders_Users,pk = request.user.id)
    order = get_object_or_404(ordermodel.Order,pk = order_id)
    
    if current_user.grade == "초급자":
        delivery_tip = 1500
    elif current_user.grade == "중급자":
        delivery_tip = 2000
    elif current_user.grade == "고급자":
        delivery_tip = 2500
    else:
        delivery_tip = 0

    delivery = Delivery(
        state = "배달중",
        lionders_info = current_user,
        order_sheet = order,
        delivery_tips = delivery_tip,
    )
    delivery.save()

    order.is_complete = True
    order.save()

    return render(request,"delivery.html",{'delivery':delivery})


# def delivery(request):
#     if request.method == 'POST':
#         form = DeliveryForm(request.POST)
#         request.POST._mutable = True
#         request.POST['lionders_info'] = request.user
#         if form.is_valid():
#             new_item = form.save()
#         return HttpResponseRedirect('../delivery/deliverylist')
#     form = DeliveryForm()
#     return render(request, 'delivery.html', {'form': form})


def delivery_update(request, id):
    item = get_object_or_404(Delivery, pk=id)
    if request.method == 'POST':
        item.state = "배달 완료"
        item.save()
        return redirect('delivery-list')
    return render(request, 'delivery_update.html', {'item': item})


def delivery_delete(request, id):
    item = get_object_or_404(Delivery, pk=id)
    if request.method == 'POST':
        item.delete()
        return redirect('delivery-list')  # 리스트 화면으로 이동합니다.
    return render(request, 'delivery_delete.html', {'item': item})




