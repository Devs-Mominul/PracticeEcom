from django.contrib import admin
from store.models import Category, Product, ProductImage


# Register your models here.
class ProductImageAdmin(admin.StackedInline):
    model = ProductImage
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageAdmin]
admin.site.register(Category)
admin.site.register(Product, ProductAdmin)
