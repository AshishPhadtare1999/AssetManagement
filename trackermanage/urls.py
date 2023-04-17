from django.urls import path
from trackermanage import views
from AssetTracker import settings
from django.conf.urls.static import static

urlpatterns = [
    path('',views.indexPage, name='homePage' ),
    path('crudasset/',views.readData,name='index'),
    path('addasset/', views.addData, name = 'add-book'),
    path('updateasset/<int:assetid>', views.updateAsset),
    path('deleteasset/<int:assetid>', views.deleteAsset)
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)