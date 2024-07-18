from django.shortcuts import render
from .models import Product,Brand,Review,ProductImage
from django.views.generic import ListView,DetailView
from django.db.models.aggregates import Count

class Product_list(ListView):
    model=Product
    template_name='products/product_list.html'
    paginate_by=28

class Product_Detail(DetailView):
    model=Product
    template_name='products/product_detail.html'

    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context["reviews"] = Review.objects.filter(product=self.get_object())
        context["images"] = ProductImage.objects.filter(product=self.get_object())
        context["related"] = Product.objects.filter(brand=self.get_object().brand)
        return context
    
class Brand_List(ListView):
    model=Brand
    template_name='products/brand_list.html'
    paginate_by=25

    queryset=Brand.objects.all().annotate(product_count=Count('product_brand'))

# class Brand_Detail(DetailView):
#     model=Brand
#     template_name='products/brand_detail.html'

#     def get_context_data(self, **kwargs) :
#         context = super().get_context_data(**kwargs)
#         context["related"] = Product.objects.filter(brand=self.get_object())
#         return context


class Brand_Detail(ListView):
    model=Product
    template_name='products/brand_detail.html'
    paginate_by=5
    
    def get_queryset(self):
        brand=Brand.objects.get(slug=self.kwargs['slug'])
        queryset=super().get_queryset().filter(brand=brand)
        return queryset
    

    def get_context_data(self, **kwargs) :
        context = super().get_context_data(**kwargs)
        context["brand"] = brand=Brand.objects.filter(slug=self.kwargs['slug']).annotate(product_count=Count('product_brand'))[0]
        return context
    
    
    
    

   

   
    
    

    
    
