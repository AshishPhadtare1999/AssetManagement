from django.db import models
import uuid

# Create your models here.

class AssetType(models.Model):
    assetid=models.AutoField(primary_key=True)
    assettype=models.CharField('Asset Type',max_length=50,blank=False,null=False,unique=True)
    description=models.CharField('Description',max_length=500,null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.assettype

def get_asset_code():
    return str(uuid.uuid4().int)[:16]

class ManageAsset(models.Model):
    assetname=models.CharField('Asset Name',max_length=50,blank=False,null=False)
    assetcode=models.CharField(default = get_asset_code,editable=False,max_length=20)
    assettype=models.ForeignKey(AssetType,null=True,blank=False,on_delete=models.SET_NULL)
    assetimage=models.ImageField('Image',upload_to='images/',default=None)
    is_active=models.BooleanField('Active',default=True)
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.assetname




