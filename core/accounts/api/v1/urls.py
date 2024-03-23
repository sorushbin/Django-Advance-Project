from django.urls import path
from . import views
# from rest_framework.authtoken.views import ObtainAuthToken



app_name = 'accounts-api'

urlpatterns =[
    path('registration/', views.RegistrationApiView.as_view(), name='registration'),
    path('token/login/', views.CustomAuthToken.as_view(), name='token-login'),
    path('token/logout/', views.CustomDiscardAuthToken.as_view(), name='token-logout'),
]