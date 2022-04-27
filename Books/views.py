from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import BooksSerializer
from .models import Books

# Create your views here.
@api_view(['GET'])
def listBooks(request):
    books = Books.objects.all()
    serializer = BooksSerializer(books, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addBooks(request):
    serializer = BooksSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['PUT'])
def updateBooks(request, bk):
    book = Books.objects.get(id=bk)
    serializer = BooksSerializer(instance=book, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def removeBooks(request, bk):
    book = Books.objects.get(id=pk)
    book.delete()
    return Response(serializer.data)    