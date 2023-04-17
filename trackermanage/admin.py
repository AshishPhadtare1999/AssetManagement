from django.contrib import admin
from .models import *
# Register your models here.

class AssetTypeAdmin(admin.ModelAdmin):
    list_display=['assetid','assettype','description','created_at','updated_at']

class AssetManageAdmin(admin.ModelAdmin):
    list_display=['assetname','assetcode','assettype','assetimage','is_active','created_at','updated_at']


admin.site.register(AssetType,AssetTypeAdmin)
admin.site.register(ManageAsset,AssetManageAdmin)




