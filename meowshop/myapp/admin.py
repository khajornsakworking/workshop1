from django.contrib import admin
from .models import Category, Product, CommentProduct, ProductImage

class CoommentProductStackInline(admin.StackedInline):
    model = CommentProduct

class CoommentProductTabularInline(admin.TabularInline):
    model = CommentProduct
    extra = 0

class ImageProductTabularInline(admin.TabularInline):
    model = ProductImage
    extra = 0

class ProductAdmin(admin.ModelAdmin):
    list_display = ['p_name', 'showimg_product', 'p_description', 'p_price', 'p_recommend', 'p_status']
    list_filter = ['p_status', 'p_category']
    search_fields = ['p_code', 'p_name']
    prepopulated_fields = {'p_slug': ['p_name']}
    #fieldsets = (
    #   (None, {'fields': ['p_code', 'p_slug', 'p_name', 'p_description', 'p_price', 'p_recommend', 'p_status']}),
    #   ('Category', {'fields': ['p_category'], 'classes':['collapse']}),
    #)
    inlines = [ CoommentProductTabularInline, ImageProductTabularInline ]

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['c_name', 'showimg_category', 'c_description', 'c_status']
    search_fields = ['c_name']
    list_filter = ['c_status']



admin.site.register(Category, CategoryAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(ProductImage)
