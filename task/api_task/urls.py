from django.urls import path
from .views import operation

urlpatterns = [
    path('', view=operation, name='post')
]