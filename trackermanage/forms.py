from django import forms
from .models import *

class AssetTypeForm(forms.ModelForm):
    class Meta:
        model=AssetType
        fields='__all__'


class ManageAssestForm(forms.ModelForm):
        class Meta:
            model=ManageAsset
            fields='__all__'
