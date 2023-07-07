from django.urls import path, re_path
from . import views

urlpatterns = [
    path('', views.helloview),
    path('add-book/', views.addbookview),
    path('add-book/add', views.addbook),
    path('edit-book/', views.editbookview),
    path('edit-book/edit', views.editbook),
    path('delete-book/', views.deletebookview),
]
