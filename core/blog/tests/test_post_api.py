from rest_framework.test import APIClient
from django.urls import reverse
from datetime import datetime
import pytest
from accounts.models import User 

@pytest.fixture()
def api_client():
     client = APIClient()
     return client

@pytest.fixture()
def common_user():
    user = User.objects.create_user(email='admin@admin.com', password='123456@Ms', is_verified=True)
    return user

@pytest.mark.django_db
class TestPostApi:

    def test_post_get_response_200_status(self, api_client):
        url = reverse('blog:api-v1:post-list')
        response = api_client.get(url)
        assert response.status_code == 200
    
    def test_create_post_unauthorized_response_401_status(self, api_client):
        url = reverse('blog:api-v1:post-list')
        data = {
            'title' : 'test title',
            'status':True,
            'content':'test content',
            'published_date': datetime.now()
        }
        response = api_client.post(url, data)
        assert response.status_code == 401

    def test_create_post_authenticated_response_201_status(self, api_client, common_user):
        url = reverse('blog:api-v1:post-list')
        data = {
            'title' : 'test title',
            'status':True,
            'content':'test content',
            'published_date': datetime.now()
        }
        user = common_user
        api_client.force_authenticate(user=user)
        response = api_client.post(url, data)
        assert response.status_code == 201

    def test_create_post_invalid_data_response_201_status(self, api_client, common_user):
        url = reverse('blog:api-v1:post-list')
        data = {
            'title' : 'test title',
            'status':True,
        }
        user = common_user
        api_client.force_authenticate(user=user)
        response = api_client.post(url, data)
        assert response.status_code == 400