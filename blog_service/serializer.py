from rest_framework import serializers, status

from models import Blog



class BlogSerializer(serializers.Serializer):
    title = serializers.CharField(required=True)
    slug = serializers.SlugField(required=True)
    content = serializers.CharField(required=False)
    author = serializers.CharField(required=False)