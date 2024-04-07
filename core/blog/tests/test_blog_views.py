from django.test import TestCase, Client
from datetime import datetime
from django.urls import reverse
from accounts.models import User, Profile
from blog.models import Post, Category


class BlogViewTest(TestCase):

    def setUp(self):
        self.client = Client()
        self.user = User.objects.create(
            email = 'test@test.com', password = '845566535$Mdsf'
        )
        self.profile = Profile.objects.create(
            user = self.user,
            first_name = 'mahmoud',
            last_name = 'saifi',
            image = None,
            description = 'i am programmer',
            updated_date = datetime.now(),
        )
        self.cat_obj = Category.objects.create(name = 'test_cat')
        self.post = Post.objects.create(
            author = self.profile ,
            title = 'test',
            image  = None,
            content = 'the test content',
            status = True,
            category = self.cat_obj,
            published_date = datetime.now()           
        )

    def test_blog_index_url_response_successful(self):
        url = reverse('blog:cbv-index')
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, template_name='index.html')
        self.assertTrue(str(response.content).find('index'))

    def test_blog_post_detail_logged_in_response(self):
        url = reverse('blog:post-detail', kwargs={'pk':self.post.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 302)

    def test_blog_post_detail_anonymous_response(self):
        self.client.force_login(self.user)
        url = reverse('blog:post-detail', kwargs={'pk':self.post.id})
        response = self.client.get(url)
        self.assertEqual(response.status_code, 200)
