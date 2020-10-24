from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, request, response
from .models import Delivery
from .forms import DeliveryForm, UpdateDeliveryForm
from users import models as usermodel
from order import models as ordermodel
# Create your views here.


def delivery_list(request):
    orders = ordermodel.Order.objects.filter(doing_delivery=False, can_delivery=True)
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
    order.doing_delivery = True
    order.save()

    return render(request,"delivery.html",{'delivery':delivery})


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
