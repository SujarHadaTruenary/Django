from django.shortcuts import render , HttpResponse
from django.views import View

from django.views.generic import (
CreateView,
DetailView,
ListView,
UpdateView,
ListView,
DeleteView
)



from .models import TodoItem
# Create your views here.
# request parameters helps us to access the query parameter and it also helps us to access the body of different requests

def home(request): 
    return render(request,"home.html")

# def todos(request):
#     items = TodoItem.objects.all()
#     return render(request,"todos.html", {"todos":items})


class todos(ListView):
     template_name = 'todos.html'
     queryset = TodoItem.objects.all()


   