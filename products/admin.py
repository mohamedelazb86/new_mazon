from django.contrib import admin
from django_summernote.admin import SummernoteModelAdmin

from .models import Product,Brand,Review,ProductImage


class Product_Imge(admin.TabularInline):
    model=ProductImage


class ProductAdmin(SummernoteModelAdmin):
    list_display=['name','sku','flag']
    search_fields=['name','subtitle','descriptions']
    list_filter=['brand']

    summernote_fields = ('subtitle','descriptions')
    inlines=[Product_Imge]



admin.site.register(Product,ProductAdmin)
admin.site.register(Brand)
admin.site.register(Review)
#admin.site.register(ProductImage)
