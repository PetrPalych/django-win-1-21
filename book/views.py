from django.shortcuts import render

from .models import *

# Create your views here.


def view_book(request):
    queryset = Book.objects.all()
    return render(request, 'book_view.html', {'books': queryset})


def detail_view(request, id):
    queryset = Book.objects.get(id=id)
    return render(request, 'book_detail.html', {"book": queryset})
