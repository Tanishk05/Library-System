Welcom to Library System 

In this Library, there are 3 tables :-

1) Students
2) Books
3) Inventory

1) Students 

In this we can register students using http://127.0.0.1:8000/students/register-student/

               update student using http://127.0.0.1:8000/students/update-student/<str:sk> -> replace this with student id

               withdraw student using http://127.0.0.1:8000/students/remove-student/<str:sk> -> (same as above)

               list all the students using http://127.0.0.1:8000/students/list-students/

2) Books 

In this we can list all the books using http://127.0.0.1:8000/books/list-books/

               add books in library using http://127.0.0.1:8000/books/add-book/
               
               update books using http://127.0.0.1:8000/books/update-book/<str:bk>

               remove books using http://127.0.0.1:8000/books/remove-book/<str:bk>

3) Inventory

In this we can list popular books using http://127.0.0.1:8000/inventory/list-popular-books/

               issue books using http://127.0.0.1:8000/inventory/issue-books/

               return books using http://127.0.0.1:8000/inventory/return-book/<str:bn> -> replace this with book name you want to return

               list issued books using http://127.0.0.1:8000/inventory/list-issued-books/

