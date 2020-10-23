from django.urls import path
from . import views

urlpatterns = [
    #delivery(배달)
    path('delivery/<int:order_id>',views.make_delivery,name='delivery'),
    path('delivery/deliverylist/',views.delivery_list,name='delivery-list'),
    path('delivery/<int:id>/delete/', views.delivery_delete,name='delivery-delete'),
    path('delivery/<int:id>/update/',views.delivery_update,name='delivery-update'),
]