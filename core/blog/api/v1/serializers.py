from rest_framework import serializers
from ...models import Post, Category

class PostSerializers(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['id', 'title', 'status', 'content', 'author' , 'published_date']
    
    
class CategorySerializers(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ['id', 'name']