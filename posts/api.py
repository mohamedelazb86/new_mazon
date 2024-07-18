from rest_framework import generics
from .serializers import PostListSerializers,Post_detailSerializers,PostAllSerializers
from .models import Post


class PostListApi(generics.ListAPIView):
    queryset=Post.objects.all()
    serializer_class=PostListSerializers


class PostDetailApi(generics.RetrieveAPIView):
    queryset=Post.objects.all()
    serializer_class=Post_detailSerializers

class PostAllApi(generics.RetrieveUpdateDestroyAPIView):
    queryset=Post.objects.all()
    serializer_class=PostAllSerializers
