from django.urls import path, include
from . import views

urlpatterns = [
    path('list-books/', views.listBooks, name="list-books"), # Lists all the books in the library
    path('add-book/', views.addBooks, name="add-books"),    # Add new book to the library
    path('update-book/<str:bk>', views.updateBooks, name="update-books"),    # updates the book
    path('remove-book/<str:bk>', views.removeBooks, name="remove-books"), # remove book from library
]