from django.contrib import admin
from .models import Product,Transaction
# Register your models here.
class ProductAdmin(admin.ModelAdmin):
    list_display = ['ProductName','price']
class TransactionAdmin(admin.ModelAdmin):
    list_display = ['UserName','quatily']
admin.site.register(Product,ProductAdmin)
admin.site.register(Transaction,TransactionAdmin)
