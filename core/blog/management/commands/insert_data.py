from django.core.management.base import BaseCommand
from faker import Faker
import random.
from datetime import datetime
from accounts.models import User, Profile
from blog.models import Category, Post

category_list = [
    'it',
    'iot',
    'computer'
]


class Command(BaseCommand):
    help = 'Inserting dummy data'

    def __init__(self, *args, **kwargs) -> None:
        super(Command, self).__init__(*args, **kwargs)
        self.fake = Faker()

    def handle(self, *args, **kwargs):
        user = User.objects.create_user(
            email=self.fake.email(), password='123456@Ms')
        profile = Profile.objects.get(user=user)
        profile.first_name = self.fake.first_name()
        profile.last_name = self.fake.last_name()
        profile.description = self.fake.paragraph(nb_sentences=5)
        profile.save()

        for name in category_list:
            Category.objects.get_or_create(name=name)

        for _ in range(10):
            Post.objects.create(
                author=profile,
                title=self.fake.sentence(nb_words=5, variable_nb_words=False),
                content=self.fake.paragraph(nb_sentences=10), status=random.choice([True, False]),
                category=Category.objects.get(name=random.choice(category_list)),
                published_date=datetime.now()
            )
