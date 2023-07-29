from django.contrib import admin
from .models import (
    Category,
    Product,
    ProductDescription,
    ProductImage
)

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'discount', 'category')
    ordering = ['id']


class ProductImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'image')
    ordering = ['id']


class ProductDescriptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'description')
    ordering = ['id']


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage, ProductImageAdmin)
admin.site.register(ProductDescription, ProductDescriptionAdmin)