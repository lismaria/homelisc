from dataclasses import fields
from django import forms
import Vendor.models as Vendor

class ItemCreationForm(forms.ModelForm):
    class Meta:
        model = Vendor.Item
        fields = ['item_name', 'item_descr', 'item_price', 'item_category']
        widgets = {
            'item_name' : forms.TextInput(attrs={'placeholder':'Item Name'}), 
            'item_descr' : forms.Textarea(attrs={'placeholder':'Item Description'}), 
            'item_price' : forms.NumberInput(attrs={'placeholder':'Item Price'}), 
            'item_category' : forms.TextInput(attrs={'placeholder':'Category (eg. Wall Painting, Brownies,..)'})
        }

# class ItemImageUploadForm(ItemCreationForm):
#     # item_img = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}),required=False)
#     class Meta(ItemCreationForm.Meta):
#         fields = ItemCreationForm.Meta.fields + ['item_img',]
#         widgets = {
#             'item_img': forms.ClearableFileInput(attrs={'multiple': True})
#         }
#         # required= {
#         #     'item_img': False
#         # }

class ItemImageUploadForm(forms.ModelForm):
    # item_img = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}),required=False)
    class Meta:
        model = Vendor.ItemImage
        fields = ('item_img',)
        widgets = {
            'item_img': forms.ClearableFileInput(attrs={'type':'file' ,'id':'add-itemimg','style':'display:none', 'accept':'image/*'})
        }
        # required= {
        #     'item_img': False
        # }

class ItemImageEditForm(forms.ModelForm):
    # item_img = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True}),required=False)
    class Meta:
        model = Vendor.ItemImage
        fields = ('item_img',)
        widgets = {
            'item_img': forms.ClearableFileInput(attrs={'type':'file' ,'id':'edit-itemimg','style':'display:none', 'accept':'image/*'})
        }

class ShopCreationForm(forms.ModelForm):
    class Meta:
        model = Vendor.Shop
        fields = ['shop_name', 'shop_tags', 'shop_descr', 'shop_contact', 'shop_state', 'shop_city', 'shop_location', 'shop_logo']
        labels = {
            'shop_name': '',
            'shop_tags': '', 
            'shop_descr': '',
            'shop_contact': '',
            'shop_state': '',
            'shop_city': '',
            'shop_location': '',
            'shop_logo': '',
        }
        widgets = {
            'shop_name': forms.TextInput(attrs={'placeholder':'Shop Name'}),
            'shop_tags': forms.TextInput(attrs={'placeholder':'Tags (eg. Chocolates,Crafts,..)'}),
            'shop_descr': forms.Textarea(attrs={'placeholder':'Shop Description'}),
            'shop_contact': forms.TextInput(attrs={'placeholder':'Shop Contact Number'}),
            'shop_state': forms.Select(attrs={'id':'select-state'}),
            'shop_city': forms.Select(attrs={'id':'select-city'}),
            'shop_location': forms.TextInput(attrs={'placeholder':'Add Location',"style":"width:60%;height:100%"}),
            'shop_logo': forms.FileInput(attrs={"id":"add_logo", "style":"display:none;", "onchange":"document.getElementById('logo_pic').src = window.URL.createObjectURL(this.files[0])", "accept":"image/*"}),
        }

