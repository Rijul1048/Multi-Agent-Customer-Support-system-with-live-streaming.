from django.contrib import admin
from .models import Product, Order, RefundRequest


class OrderAdmin(admin.ModelAdmin):
    list_display = ['user', 'product_name', 'status', 'amount', 'created_at' , 'tracking_number' ] 

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','price','category','in_stock']

class RefundRequestAdmin(admin.ModelAdmin):
    list_display = ['order','user','status','created_at']        

admin.site.register(Product, ProductAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(RefundRequest, RefundRequestAdmin)
