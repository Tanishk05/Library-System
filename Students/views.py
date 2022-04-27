from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializer import StudentsSerializer
from .models import Students

# Create your views here.
@api_view(['GET'])
def listStudents(request):
    students = Students.objects.all()
    serializer = StudentsSerializer(students, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def registerStudent(request):
    serializer = StudentsSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

api_view(['PUT'])
def updateStudent(request, sk):
    student = Students.objects.get(id=pk)
    serializer = StudentsSerializer(instance=student, data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)

@api_view(['DELETE'])
def removeStudent(removeStudent, sk):
    student = Students.objects.get(id=pk)
    student.delete()
    return Response(serializer.data)    