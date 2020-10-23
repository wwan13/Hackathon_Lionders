from django.forms import ModelForm
from django import forms
from .models import Delivery
from order.forms import OrderForm
from django.utils.translation import gettext_lazy as _


class DeliveryForm(forms.ModelForm):
    class Meta:
        model = Delivery
        fields = ['lionders_info', 'order_sheet', 'delivery_tips', 'state']
        labels = {
            'order_sheet': _('주문서'),
            'delivery_tips': _('배달 평'),
            #'grade_limit': _('배달원 제한'),
        }
        widgets = {
            'lionders_info': forms.HiddenInput(),
            'state': forms.HiddenInput(),
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