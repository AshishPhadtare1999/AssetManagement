from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import *
from .forms import *
# Create your views here.

def indexPage(request):
    return render(request,'index.html')

def readData(request):
    data=AssetType.objects.all()
    return render(request,'crudasset.html',{'data':data})

def addData(request):
    form=AssetTypeForm()
    if request.method=='POST':
        form=AssetTypeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('crudasset.html')
    else:
        return render('crudasset.html',{'form':form})
    
def updateAsset(request,asset_id):
    asset_id=int(asset_id)
    try:
        asset=AssetType.objects.get(id=asset_id)
    except AssetType.DoesNotExist:
        return redirect('crudasset.html')
    form=AssetTypeForm(request.POST)
    if form.is_valid():
        form.save()
    return render('crudasset.html')

def deleteAsset(request,id):
    asset_id=int(asset_id)
    try:
        asset=AssetType.objects.get(id=asset_id)
    except AssetType.DoesNotExist:
        return redirect('crudasset.html')
    asset.delete()
    return redirect('crudasset.html')

    
    


