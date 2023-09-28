
from django.contrib import admin
from django.urls import path
from storeapp import views
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.item_name, name="item_name"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('<int:id>/', views.delete_item, name="delete_item"),
    path('edit/<int:id>/', views.edit_item, name="edit_item"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)