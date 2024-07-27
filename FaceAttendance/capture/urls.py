from django.urls import path
from .views import capture_image, success, capture_image_auto, list_persons

urlpatterns = [
    path('', capture_image, name='capture_image'),
    path('success/', success, name='success'),
    path('capture_auto/', capture_image_auto, name='capture_image_auto'),
    path('list_persons/', list_persons, name='list_persons'),
]
