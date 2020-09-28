from app.models import Todo
from django.db.migrations import serializer

from rest_framework.decorators import api_view
from rest_framework.response import Response
from app.serializers import TodoSerializer
from rest_framework  import  status


@api_view(['GET','POST'])
def todo_list(request):
    if request.method == 'GET':
        todo = Todo.objects.all()
        serializer  = TodoSerializer(todo,many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = TodoSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)



