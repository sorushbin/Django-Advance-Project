from django.urls import path
from . import views

app_name = 'api-v1'


urlpatterns = [
    # path('post/', views.post_list, name='post-list'),
    # path('post/<int:pk>', views.post_details, name='post-details'),
    # path('post/', views.PostList.as_view(), name='post-list'),
    # path('post/<int:pk>', views.PostDetail.as_view(), name='post-detail'),
    path('post/', views.PostViewSet.as_view({'get':'list', 'post':'create'}), name='post-list'),
    path('post/<int:pk>/', views.PostViewSet.as_view({'get':'retrieve', 'put':'update', 'patch':'partial_update', 'delete':'destroy'}), name='post-detail')
   
]