from django.urls import path
from .views import UserGetCreate
urlpatterns = [
    path('users/',UserGetCreate.as_view())
]
