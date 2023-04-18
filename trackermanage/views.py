from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import *


# Create your views here.

def chartPage(request):
    return render(request, 'index.html')

# Asset Types Crud operations...
def addData(request):
    if request.method=='POST':
        asset_form=AssetTypeForm(request.POST)
        if asset_form.is_valid():
            asset_form.save()
            asset_form=AssetTypeForm()
    else:
        asset_form=AssetTypeForm()
    data=AssetType.objects.all()
    return render(request,'assettype.html',{'form':asset_form,'data':data})

def deleteData(request,id):
    data=AssetType.objects.get(pk=id)
    data.delete()
    return redirect('/adddata')

def updateData(request,id):
    if request.method=='POST':
        obj=AssetType.objects.get(pk=id)
        asset_form=AssetTypeForm(request.POST,instance=obj)
        if asset_form.is_valid():
            asset_form.save()
            return redirect('/adddata')
    else:
        obj=AssetType.objects.get(pk=id)
        asset_form=AssetTypeForm(instance=obj)
    return render(request,'Update.html',{'form':asset_form})


# Manage Assets crud operations..

def manageAdd(request):
    if request.method=='POST':
        name=request.POST['assetname']
        types=int(request.POST['assettype'])
        obj=AssetType.objects.get(pk=types)
        image=request.FILES['myimage']
        active=True if request.POST['is_active']=='on' else False
        manage_form=ManageAsset.objects.create(assetname=name,assettype=obj,assetimage=image,is_active=active)
        return redirect('/manageadd')
    data=ManageAsset.objects.all()
    return render(request,'manageasset.html',{'data':data})

def delete_manage(request,id):
    data=ManageAsset.objects.get(pk=id)
    data.delete()
    return redirect('/manageadd')

def update_manage(request,id):
    if request.method=='POST':
        obj=ManageAsset.objects.get(pk=id)
        name=request.POST['assetname']
        types=int(request.POST['assettype'])
        assetObj=AssetType.objects.get(pk=types)
        image=request.FILES['assetimage']
        print(types)
        print('--------')
        print(obj)

        active=True if request.POST['is_active']=='on' else False
        obj.assetname=name
        obj.assettype=assetObj
        obj.assetimage=image
        obj.is_active=active
        obj.save()
        return redirect('/manageadd')
    else:
        obj=ManageAsset.objects.get(pk=id)
        manage_form=ManageAssestForm(instance=obj)
        return render(request,'manageUpdate.html',{"form":manage_form})
        