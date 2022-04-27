from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Inventory
from .serializer import InventorySerializer
from Books.models import Books
from Students.models import Students
from django.http import HttpResponseBadRequest
import requests
# Create your views here.
@api_view(['POST'])
def IssueBook(request):
    books = Books.objects.all()
    students = Students.objects.all()
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    id1 = ''
    id2 = ''
    for x in books:
        if x.book_name == request.GET.get('book_name_to_be_issued'): 
            a += 1
            id1 = x.id
            c = x.no_of_time_issued   
            d = x.book_available
    for y in students:
        if y.student_name == request.GET.get('student_name'):
            b += 1
            e = y.no_of_books_issued
            id2 = y.id
        
    if a > 0 and b > 0 and d>0 and e < 3:
        myobj1= {"no_of_time_issued" : c+1, "book_available" : 0}
        myobj2= {"no_of_books_issued" : e+1}
        requests.put("http://127.0.0.1:8000/books/update-book/"+str(id1), data=myobj1)
        requests.put("http://127.0.0.1:8000/students/update-student/" + str(id2), data=myobj2)
        serializer = InventorySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
        return Response(serializer.data)

    elif d == 0:
        return HttpResponseBadRequest("The requested book has been taken by somebody else")

    elif e >= 3:
        return HttpResponseBadRequest("You have already taken 3 books, first return them then take another")

    elif a>0 and b<=0:
        return HttpResponseBadRequest("The student is not registered")
    
    elif a<=0 and b>0:
        return HttpResponseBadRequest("The requested book is not available in the library")
    
    else:
        return HttpResponseBadRequest("Enter correct value")

@api_view(['DELETE'])
def returnBooks(request, bn):
    inventory = Inventory.objects.all()
    students = Students.objects.all()
    id1 = ''
    id2 = ''
    n = 0
    student_name = ''
    for i in inventory:
        if i.book_name_to_be_issued == bn:
            id1 = i.id
            student_name = i.student_name

    for s in students:
        if s.student_name == student_name:
            id2 = s.id
            n = s.no_of_books_issued

    myobj = {"no_of_books_issued" : n-1}
    requests.put("http://127.0.0.1:8000/students/update-student/" + str(id2), data=myobj)

    inventory = Inventory.objects.get(id=id1)
    inventory.delete()
    return Response(serializer.data)

@api_view(['GET'])
def listIssuedBook(request):
    inventory = Inventory.objects.all()
    serializer = InventorySerializer(inventory, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def popularBooks(request):
    books = Books.objects.order_by("no_of_time_issued")
    serializer = InventorySerializer(books, many=True)
    return Response(serializer.data)