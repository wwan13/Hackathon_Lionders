from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, request
from .models import Delivery
from .forms import DeliveryForm, UpdateDeliveryForm
from users import models as usermodel
# Create your views here.


def delivery_list(request):
    deliveries = Delivery.objects.filter()
    context = {
        'deliveries': deliveries,
    }
    return render(request, 'delivery_list.html', context)


def delivery(request):
    if request.method == 'POST':
        form = DeliveryForm(request.POST)
        request.POST._mutable = True
        # request.POST['user'] = request.user
        if form.is_valid():
            new_item = form.save()
        return HttpResponseRedirect('../delivery/deliverylist')
    form = DeliveryForm()
    return render(request, 'delivery.html', {'form': form})


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




