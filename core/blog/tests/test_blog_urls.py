from django.test import TestCase
from django.urls import reverse, resolve
from ..views import BlogView, PostListView, PostDetailView


class UrlTest(TestCase):
    def test_blog_index_url_resolve(self):
        url = reverse('blog:cbv-index')
        self.assertEqual(resolve(url).func.view_class, BlogView )

    def test_blog_list_url_resolve(self):
        url = reverse('blog:home-blog')
        self.assertEqual(resolve(url).func.view_class, PostListView )

    def test_blog_detail_url_resolve(self):
        url = reverse('blog:post-detail', kwargs={'pk':1})
        self.assertEqual(resolve(url).func.view_class, PostDetailView )