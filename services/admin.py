from django.contrib import admin
from .models import (
    Category,
    Product,
    ProductDescription,
    ProductImages
)

# Register your models here.
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name',)


class ProductAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'price', 'discount', 'category')


class ProductImagesAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'image')


class ProductDescriptionAdmin(admin.ModelAdmin):
    list_display = ('id', 'product', 'description')


admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImages, ProductImagesAdmin)
admin.site.register(ProductDescription, ProductDescriptionAdmin)