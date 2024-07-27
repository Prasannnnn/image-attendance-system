from django.urls import path
from .views import capture_image, success

urlpatterns = [
    path('', capture_image, name='capture_image'),
    path('success/', success, name='success'),
]
