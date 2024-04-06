from django.test import TestCase
from datetime import datetime
from ..models import Post, Category
from accounts.models import User, Profile

class PostModelTest(TestCase):

    def test_post_create_validated_data(self):
        cat_obj = Category.objects.create(name = 'test')
        user = User.objects.create(
            email = 'test@test.com', password = '845566535$Mdsf'
        )
        profile = Profile.objects.create(
            user = user,
            first_name = 'mahmoud',
            last_name = 'saifi',
            image = None,
            description = 'i am programmer',
            updated_date = datetime.now(),
        )

        post = Post.objects.create(
            author = profile ,
            title = 'test',
            image  = None,
            content = 'the test content',
            status = True,
            category = cat_obj,
            published_date = datetime.now()           
        )
        self.assertEqual(post.title, 'test')