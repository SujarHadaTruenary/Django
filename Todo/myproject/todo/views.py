import json
from django.http import HttpResponse
from .models import todo
from .form import TodoForm
from django.shortcuts import render , redirect
from django.views.decorators.http import require_POST
import requests
from rest_framework import viewsets
from .serializers import TodoSerializer

# Create your views here.
# token = ""

token= "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjk2NTkyMjIyLCJpYXQiOjE2OTY1ODg2MjIsImp0aSI6ImRiMDQ3ZjdkMmQ1OTQzNjRhM2YxMzZkNjMyMDliNzBiIiwidXNlcl9pZCI6MX0.G84WhnBvGAflpaSxJd6Q8he6edNVoZpMK4srwUVsWQ4"

headers = {
    'Content-Type': 'application/json',
    'Authorization': f'Bearer {token}'
}

def index(request):
    r = requests.get('http://127.0.0.1:8000/todo/', headers=headers)

    json_data = r.content
    data = json.loads(json_data)
    # todolist = [{"name": item["name"], "done": item["done"]} for item in data]

    form = TodoForm()
    context = {'todo_list': data, 'form': form}

    return render(request, 'todo/index.html', context)

    # return HttpResponse('hello')

   # todo_list = Todo.objects.order_by('id')


@require_POST
def addTodo(request):
    data = {"name": request.POST['text']}
    data_json = json.dumps(data)

    r = requests.post('http://127.0.0.1:8000/todo/', data=data_json, headers=headers)
    return redirect('index')

def completeTodo(request,todo_id):
    url = f'http://127.0.0.1:8000/todo/{todo_id}/'
    r = requests.delete(url, headers=headers)
    return redirect('index')


def login(request):
    if request.method == 'POST':
        url = 'http://127.0.0.1:8000/api/token/'
        data = {
            'username': request.POST['userid'],
            'password': request.POST['password']
        }
        data_json = json.dumps(data)

        response = requests.post(url, data=data_json)
        response_data = response.json()
        access_token = response_data['access']
        token = access_token

        r = requests.get('http://127.0.0.1:8000/todo/', headers=headers)
        json_data = r.content

        data2 = json.loads(json_data)

        form = TodoForm()
        context = {'todo_list': data2, 'form': form}


        print(token)

        return render(request, 'todo/index.html', context)

    else:
        return render(request, 'todo/login.html')



def deletecompleted(request):
    Todo.objects.filter(complete__exact=True).delete()

    return redirect('index')

def deleteall(request):
    Todo.objects.all().delete()

    return redirect('index')
