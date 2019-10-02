from django.shortcuts import render

# Create your views here.
def index(request): # request는 인자의 이름
    return render(request, 'index.html')