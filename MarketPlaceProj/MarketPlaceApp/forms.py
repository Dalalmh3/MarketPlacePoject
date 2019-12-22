from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout,Submit
from django.core.validators import RegexValidator
from .models import Product
from django import forms

class ProductForm(forms.ModelForm):

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)


    class Meta:
        model = Product
        fields = ('pName', 'description','img_url')

        # self.helper.layout = Layout(
        #     'pName','description','img_url',
        #     Submit('submit','send', css_class='btn-success')
        # )




    