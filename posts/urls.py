from django.urls import path
from .views import post_detail,post_list,create_post,update_post,delete_post
from .api import PostListApi,PostDetailApi,PostAllApi

urlpatterns = [
    path('',post_list),
    path('<slug:slug>',post_detail),
    path('create_post/create',create_post),
    path('update/<slug:slug>',update_post),
    path('<slug:slug>/delete',delete_post),

    #   api
    path('api/post/list',PostListApi.as_view()),
    path('api/post/<int:pk>',PostDetailApi.as_view()),
    path('api/postall',PostAllApi.as_view()),


]
