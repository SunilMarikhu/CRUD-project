from django.contrib import admin
from .models import Item
# Register your models here.
admin.site.site_header = "Online Store Pvt.Ltd"
admin.site.index_title = "Store Admin"
@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'name', 'description', 'image', 'price']