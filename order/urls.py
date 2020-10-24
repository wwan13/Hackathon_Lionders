from django.urls import path
from . import views

urlpatterns = [
    # order(주문)
    path('order/',views.order,name='order'),
    path('order_final/<int:order_id>',views.make_order_final,name='order_final'),
    path('order/orderlist/',views.order_list,name='order-list'),
    path('order/<int:order_id>/',views.order_detail,name='order-detail'),
    path('order/<int:id>/delete/', views.order_delete,name='order-delete'),
    path('order/update/',views.order_update,name='order-update'),
    path('item/',views.item_create,name='item'),
    path('add_item/<int:order_id>/<int:item_id>',views.add_item,name='add_item'),
    path('remove_item/<int:order_id>/<int:item_id>',views.remove_item,name='remove_item'),
    path('delete_item/<int:item_id>',views.delete_item,name='delete_item'),
    path('estimate/',views.estimate_lionders,name='estimate_lionders'),
]