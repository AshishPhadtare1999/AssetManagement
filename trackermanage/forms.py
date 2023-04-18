from django import forms
from .models import *

class AssetTypeForm(forms.ModelForm):
    class Meta:
        model=AssetType
        fields='__all__'
        widgets={
             'assettype':forms.TextInput(attrs={'class':'form-control'}),
             'description':forms.Textarea(attrs={'class':'form-control'})
        }


class ManageAssestForm(forms.ModelForm):
        class Meta:
            model=ManageAsset
            fields='__all__'
            widgets={
             'assetname':forms.TextInput(attrs={'class':'form-control'}),
             'assetcode':forms.TextInput(attrs={'class':'form-control'}),
             'assettype':forms.Select(attrs={'class':'form-control'}),
             'assetimage':forms.FileInput(attrs={'class':'form-control'}),
            
            }
