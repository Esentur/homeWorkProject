from django.contrib import admin

from apps.product.models import Product

# кастомизация административной панели
class CustomProduct(admin.ModelAdmin):
    list_display = ('id', 'name', 'description', 'price', 'vendor')
    list_filter = ['vendor']
    search_fields = ['name']

admin.site.register(Product, CustomProduct)
