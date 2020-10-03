from django.forms import ModelForm
from django import forms
from .models import Delivery, Order, Item
from django.utils.translation import gettext_lazy as _



class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['store', 'item_name', 'price']
        labels = {
            'store': _('가게명'),
            'item_name': _('상품'),
            'price': _('가격'),
        }
        widgets = {

        }
        help_texts = {

        }


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['normal_user_info', 'total_price', 'destination', 'items']
        labels = {
            'total_price': _('총 금액'),
            'destination': _('주소')
        }
        widgets = {
            'normal_user_info': forms.HiddenInput(),
            # 'items': forms.HiddenInput()
        }
        help_texts = {

        }

class UpdateOrderForm(OrderForm):
    class Meta:
        model = Order
        exclude = ['user']

    def __init__(self, *args, **kwargs):
        self.request = kwargs.pop('request', None)
        super(OrderForm, self).__init__(*args, **kwargs)

    def save(self, commit=True):
        instance = super(OrderForm, self).save(commit=False)

        if commit:
            instance.save()
        return instance


class DeliveryForm(forms.ModelForm):
    class Meta:
        model = Delivery
        fields = ['lionders_info', 'order_sheet', 'delivery_tips', 'grade_limit']
        labels = {
            'order_sheet': _('주문서'),
            'delivery_tips': _('배달 평'),
            'grade_limit': _('배달원 제한'),
        }
        widgets = {
            'lionders_info': forms.HiddenInput(),
            # 'items': forms.HiddenInput()
        }
        help_texts = {

        }


class UpdateDeliveryForm(OrderForm):
    class Meta:
        model = Delivery
        exclude = ['lionders_info']

    # def __init__(self, *args, **kwargs):
    #     self.request = kwargs.pop('request', None)
    #     super(DeliveryForm, self).__init__(*args, **kwargs)

    # def save(self, commit=True):
    #     instance = super(DeliveryForm, self).save(commit=False)
    #
    #     if commit:
    #         instance.save()
    #     return instance