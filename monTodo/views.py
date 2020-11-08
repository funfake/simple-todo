from django.shortcuts import render
from monTodo.models import Todo
# Create your views here.

def get_todos(request):
    todos = Todo.objects.all().order_by("-fait_le")
    return render(request, 'monTodo/list.html', context={'todos':todos})