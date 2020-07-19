from django.urls import path,include
from .api import RegisterAPI

urlpatterns=[
    path('api/contact', RegisterAPI.as_view())
]