from django.urls import path
from .views import Product_list,Product_Detail,Brand_Detail,Brand_List

urlpatterns = [
    path('brands',Brand_List.as_view()),
    path('brands/<slug:slug>',Brand_Detail.as_view()),

    
    path('',Product_list.as_view()),
    path('<slug:slug>',Product_Detail.as_view()),
]
