from django.test import TestCase
from datetime import datetime
from ..models import Post, Category
from accounts.models import User, Profile

class PostModelTest(TestCase):

    def setUp(self):
        self.cat_obj = Category.objects.create(name = 'test')
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

    def test_post_create_validated_data(self):
        post = Post.objects.create(
            author = self.profile ,
            title = 'test',
            image  = None,
            content = 'the test content',
            status = True,
            category = self.cat_obj,
            published_date = datetime.now()           
        )
        self.assertTrue(Post.objects.filter(pk = post.id).exists())
        self.assertEqual(post.title, 'test')