from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render


def index_view(request: WSGIRequest):
    # print(request.GET.get("id"))
    # print(f'Id: {request.GET["id"]}')
    # print(f'Id: {request.GET.get("id", 10)}')
    # print(f'Name: {request.GET.get("name", "John")}')
    # print(f"Method: {request.method}")
    # print(f"Get id - {request.GET.get('id')} - {type(request.GET.get('id'))}")
    first = int(request.GET.get('first', 0))
    second = int(request.GET.get('second', 0))
    return render(request, 'index.html', context={
        'result': first + second,
        'first': first,
        'second': second
    })