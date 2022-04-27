from django.urls import path, include
from . import views

urlpatterns = [
    path('issue-books/', views.IssueBook, name="issue-books"), # issue book from the library
    path('list-issued-books/', views.listIssuedBook, name="list-issued-books"), # Lists all the issued books in the library
    path('return-book/<str:bn>', views.returnBooks, name="return-books"), # return book to library
    path('list-popular-books/', views.popularBooks, name="list-popular-books") # return popular books
]