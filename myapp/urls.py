from django.urls import path
from .views import index, detail, tags, create, edit, delete

urlpatterns = [
    path('', index, name='index'),
    path('car/<slug:slug>/', detail, name='detail'),
    path('tags/<slug:slug>/', tags, name='tags'),
    path('create/', create, name='create'),
    path('edit/<int:pk>/', edit, name='edit'),
    path('delete/<int:pk>/', delete, name='delete')

]
