from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated
from rest_framework.response import Response
from .serializers import PostSerializers
from ...models import Post
from rest_framework import status
from django.shortcuts import get_object_or_404


@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def post_list(request):
    if request.method == 'GET':
        posts = Post.objects.filter(status=True)
        serializer = PostSerializers(posts, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = PostSerializers(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    # another way
    """
    if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)
    """


@api_view(['GET', 'PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def post_details(request, pk):
    post = get_object_or_404(Post, id=pk, status=True)
    if request.method == 'GET':
        serializer = PostSerializers(post)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = PostSerializers(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    elif request.method == 'DELETE':
        post.delete()
        return Response("{'details': post deleted successfully}", status=status.HTTP_204_NO_CONTENT)

    # another way for 404 page0
    """
    try:
        post = Post.objects.get(id=pk)
        serializer = PostSerializers(post)
        return Response(serializer.data)
    except Post.DoesNotExist:
        return Response('dose not exist.', status=status.HTTP_404_NOT_FOUND)
    """
