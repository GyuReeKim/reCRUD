from django.shortcuts import render, redirect
from .models import Todo

# Create your views here.
def index(request): # request는 인자의 이름
    todos = Todo.objects.all()
    context = {
        'todos': todos,
    }
    return render(request, 'index.html', context) # render는 python에서 html을 읽을 수 있도록 한다.

def new(request):
    return render(request, 'new.html')

def create(request):
    title = request.GET.get('title')
    due_date = request.GET.get('duedate')

    todo = Todo()
    todo.title = title
    todo.due_date = due_date
    todo.save()

    return redirect('/todos/')

def delete(request, id):
    todo = Todo.objects.get(id=id)
    todo.delete()
    return redirect('/todos/')