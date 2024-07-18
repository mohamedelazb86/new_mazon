from rest_framework import serializers
from .models import Post

class PostListSerializers(serializers.ModelSerializer):
    category=serializers.StringRelatedField()
    class Meta:
        model=Post
        fields='__all__'

class Post_detailSerializers(serializers.ModelSerializer):
    category=serializers.StringRelatedField()
    class Meta:
        model=Post
        fields='__all__'

        
class PostAllSerializers(serializers.ModelSerializer):
    class Meta:
        model=Post
        fields='__all__'