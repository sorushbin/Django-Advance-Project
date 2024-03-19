from rest_framework import serializers
from ...models import Post

class PostSerializers(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ['id', 'title', 'status', 'content', 'author' , 'published_date']
    
    
   