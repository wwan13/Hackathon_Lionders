from django.urls import path
from . import views

urlpatterns = [
    path('order/',views.order,name='order'),
    path('order/orderlist/',views.order_list,name='order-list'),
    path('order/<int:id>/delete/', views.order_delete,name='order-delete'),
    path('order/update/',views.order_update,name='order-update'),
]