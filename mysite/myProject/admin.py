from django.contrib import admin
from .models import Customer, Order, Status, ProductOrder, Product

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('f_name', 'l_name', 'email')

class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price')
    list_filter = ('name', 'price')

class ProductOrderInline(admin.TabularInline):
    model = ProductOrder
    extra = 0

class OrderAdmin(admin.ModelAdmin):
    inlines = [ProductOrderInline]

admin.site.register(Customer, CustomerAdmin)
admin.site.register(Order, OrderAdmin)
admin.site.register(Status)
admin.site.register(ProductOrder)
admin.site.register(Product, ProductAdmin)