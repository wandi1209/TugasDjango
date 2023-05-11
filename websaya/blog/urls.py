from django.urls import path

from .views import blog_index, BlogClass

urlpatterns = [
    path('', blog_index),
    path('bclass/', BlogClass.as_view()),
]