from django.urls import path
from .views import post_detail,post_list,create_post,update_post,delete_post

urlpatterns = [
    path('',post_list),
    path('<slug:slug>',post_detail),
    path('create_post/create',create_post),
    path('update/<slug:slug>',update_post),
    path('<slug:slug>/delete',delete_post)
]
