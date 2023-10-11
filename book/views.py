from django.shortcuts import render

from .models import *

# Create your views here.


def view_book(request):
    queryset = Book.objects.all()
    return render(request, 'book_view.html', {'books': queryset})
