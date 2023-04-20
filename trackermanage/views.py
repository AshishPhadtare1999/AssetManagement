from django.shortcuts import render, redirect
from django.http import HttpResponse,FileResponse,JsonResponse
from .models import *
from .forms import *
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.db.models import Count
import pandas as pd
import tempfile
from django.core.serializers import serialize
from .task import *
import json

# Create your views here.
@login_required
def chartPage(request):
    data=AssetType.objects.all().values('assettype').annotate(total=Count('assettype'))
    active_data=ManageAsset.objects.all().values('is_active').annotate(total=Count('is_active'))
    print(active_data)
    labels =['on', 'of']
    values = [0, 0]
    for obj in active_data:
        if obj["is_active"]:
          values[0] = obj["total"]
        else:
            values[1] = obj["total"]  
    print(f'{labels=}, {values=}')
    return render(request, 'index.html',{'data':data, "titles": labels, 'values':values})

# Asset Types Crud operations...
@login_required
def addData(request):
    if request.method=='POST':
        asset_form=AssetTypeForm(request.POST)
        if asset_form.is_valid():
            asset_form.save()
            asset_form=AssetTypeForm()
    else:
        asset_form=AssetTypeForm()
    data=AssetType.objects.all().order_by('-created_at')
    page = request.GET.get('page', 1)
    paginator = Paginator(data, 4)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    
    return render(request,'assettype.html',{'form':asset_form,'data':posts})

@login_required
def deleteData(request,id):
    data=AssetType.objects.get(pk=id)
    data.delete()
    return redirect('/adddata')

@login_required
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

@login_required
def manageAdd(request):
    if request.method=='POST':
        name=request.POST['assetname']
        types=int(request.POST['assettype'])
        obj=AssetType.objects.get(pk=types)
        image=request.FILES['myimage']
        active=True if request.POST.get('is_active')=='on' else False
        manage_form=ManageAsset.objects.create(assetname=name,assettype=obj,assetimage=image,is_active=active)
        return redirect('/manageadd')
    data=ManageAsset.objects.all().order_by('-created_at')
    page = request.GET.get('page', 1)
    paginator = Paginator(data, 4)
    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)
    asset_list=AssetType.objects.all()
    
    # Download response none normal get request...

    download = request.GET.get("download")
    if download:
        print("your request has been in queue...")
        if download == "1":
            sleepy.delay(10)
            return HttpResponse("")
        elif download=="2":
            import os
            return JsonResponse({"is_file_ready":os.path.exists("assetManage.csv")})
        else: 
            import os
            if os.path.exists("assetManage.csv"):
                return FileResponse(open("assetManage.csv", 'rb'))
            raise Exception("Not Found")
    # if request.GET.get("download"):
    #     print("your request has been in que")
    #     sleepy.delay(10)
    #     with tempfile.TemporaryDirectory() as tmpdirname:
    #         df=pd.DataFrame(data)
    #         file_loc = f"{tmpdirname}/assetManage.csv"
    #         print("tmpdirname>>.....", tmpdirname)
    #         df.to_csv(file_loc,index=False)
    #         return FileResponse(open(file_loc, 'rb'))

    return render(request,'manageasset.html',{'data':posts,'asset_list':asset_list})

@login_required
def delete_manage(request,id):
    data=ManageAsset.objects.get(pk=id)
    data.delete()
    return redirect('/manageadd')

@login_required
def update_manage(request,id):
    if request.method=='POST':
        obj=ManageAsset.objects.get(pk=id)
        name=request.POST['assetname']
        types=int(request.POST['assettype'])
        assetObj=AssetType.objects.get(pk=types)
        image=request.FILES['assetimage']
        active=True if request.POST.get('is_active')=='on' else False
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
        