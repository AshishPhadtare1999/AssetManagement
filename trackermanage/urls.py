from django.urls import path
from trackermanage import views
from AssetTracker import settings
from django.conf.urls.static import static

urlpatterns = [
                  path('', views.chartPage, name='charts'),
                  path('adddata/',views.addData,name="Add"),
                  path('deletedata/<int:id>',views.deleteData,name='DeleteData'),
                  path('updatedata/<int:id>',views.updateData,name='updateData'),
                  
                  path('manageadd/',views.manageAdd,name='manageadd'),
                  path('delete/<int:id>',views.delete_manage,name="manageDelete"),
                  path('update/<int:id>',views.update_manage,name='manageUpdate'),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
