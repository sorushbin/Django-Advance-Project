from rest_framework.permissions import (
    IsAuthenticatedOrReadOnly,
)
from rest_framework.generics import (
    # GenericAPIView,
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
)
from rest_framework import viewsets, filters
from django_filters.rest_framework import DjangoFilterBackend
from .paginations import PostPagination
from .permissions import IsOwnerOrReadOnly
from .serializers import PostSerializers, CategorySerializers
from ...models import Post, Category

# from rest_framework.response import Response
# from django.shortcuts import get_object_or_404
# from rest_framework.views import APIView
# from rest_framework.decorators import action

# example for Function Base View
"""
from rest_framework.decorators import api_view, permission_classes
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
    '''if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors)'''


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
    '''
    try:
        post = Post.objects.get(id=pk)
        serializer = PostSerializers(post)
        return Response(serializer.data)
    except Post.DoesNotExist:
        return Response('dose not exist.', status=status.HTTP_404_NOT_FOUND)
   '''
"""

# example for APIViw in Class Base View
'''
class PostList(APIView):
    """getting a list of posts and creating a new post"""
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializers

    def get(self, request):
        """retrieving a list of all posts"""
        posts = Post.objects.filter(status=True)
        serializer = self.serializer_class(posts, many=True) # serializer = PostSerializers(posts, many=True)
        return Response(serializer.data)
    def post(self, request):
        """creating a new post with provided data"""
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

class PostDetail(APIView):
    """ getting detail of post and editing plus removing it """
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializers

    def get(self, request, pk):
        """ getting detail of post """
        post = get_object_or_404(Post, id=pk, status=True)
        serializer = self.serializer_class(post) # serializer = PostSerializers(post)
        return Response(serializer.data)
    def put(self, request, pk):
        """ editing the post """
        post = get_object_or_404(Post, id=pk, status=True)
        serializer = self.serializer_class(post, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    def delete(self, request, pk):
        """ deleting the post """
        post = get_object_or_404(Post, id=pk, status=True)
        post.delete()
        return Response("{'details': post deleted successfully}", status=status.HTTP_204_NO_CONTENT)
    '''


# example for GenericApiView in Class Base View
class PostList(ListCreateAPIView):
    """getting a list of posts and creating a new post"""

    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializers
    queryset = Post.objects.filter(status=True)


'''class PostList(GenericAPIView, mixins.ListModelMixin, mixins.CreateModelMixin):
    """getting a list of posts and creating a new post"""
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializers
    queryset = Post.objects.filter(status=True)

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)'''


class PostDetail(RetrieveUpdateDestroyAPIView):
    """getting detail of post and editing plus removing it"""

    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializers
    queryset = Post.objects.filter(status=True)


"""class PostDetail(GenericAPIView, mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializers
    queryset = Post.objects.filter(status=True)

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)
    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)"""


# example for ViewSet in Class Base View
"""
class PostViewSet(viewsets.ViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = PostSerializers
    queryset = Post.objects.filter(status=True)

    def list(self, request):
        serializer = self.serializer_class(self.queryset, many=True)
        return Response(serializer.data)
    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    def retrieve(self, request, pk=None):
        post_object = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(post_object)
        return Response(serializer.data)
    def update(self, request, pk=None):
        post_object = get_object_or_404(self.queryset, pk=pk)
        serializer = self.serializer_class(post_object, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    def destroy(self, request, pk=None):
        post_object = get_object_or_404(self.queryset, pk=pk)
        post_object.delete()
        return Response({'detail':'this post deleted successfully.'}, status=status.HTTP_204_NO_CONTENT)
    def partial_update(self, request, pk=None):
        pass
"""


# example for ModelViewSet in Class Base View
class PostModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]
    serializer_class = PostSerializers
    queryset = Post.objects.filter(status=True)
    pagination_class = PostPagination
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter,
    ]
    filterset_fields = {
        "category": ["exact", "in"],
        "author": ["exact", "in"],
        "status": ["exact"],
    }
    search_fields = ["title", "content"]
    ordering_fields = ["published_date"]


class CategoryModelViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAuthenticatedOrReadOnly]
    serializer_class = CategorySerializers
    queryset = Category.objects.all()
