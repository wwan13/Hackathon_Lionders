from django.forms import ModelForm
from django import forms
from .models import Order, Item
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
        fields = ['normal_user_info', 'total_price', 'destination_road', 'items']
        labels = {
            'total_price': _('총 금액'),
            'destination_road': _('주소')
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