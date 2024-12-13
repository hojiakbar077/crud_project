# crud/urls.py
from django.urls import path
from . import views

app_name = 'crud'  # Namespace ni qo'shing

urlpatterns = [
    path('create/', views.create_book, name='create_book'),  # 'create_book' deb nomlangan URL
    path('update/<int:id>/', views.update_book, name='update_book'),
    path('delete/<int:id>/', views.delete_book, name='delete_book'),
    path('', views.book_list, name='book_list'),
]
