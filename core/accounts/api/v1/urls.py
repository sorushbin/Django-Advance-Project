from django.urls import path
from . import views

app_name = 'accounts-api'

urlpatterns =[
    path('registration/', views.RegistrationApiView.as_view(), name='registration' )
]