from django.forms import forms
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from . import models, forms


# Create your views here.


def view_book(request):
    book_value = models.Book.objects.all()
    return render(request, "book_view.html", {"book_key": book_value})


def detail_view(request, id):
    book_id = get_object_or_404(models.Book, id=id)
    return render(request, 'book_detail.html', {'book_key': book_id})


def create_review_for_book(request):
    method = request.method
    if method == 'POST':
        form = forms.ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()

            return HttpResponse("<a href='/'>Назад</a>")
    else:
        form = forms.ReviewForm()

    return render(request, 'create_review_for_book.html', {'form': form})


def create_view_book_post(request):
    method = request.method
    if method == "POST":
        form = forms.BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('Добавлен успешно!')
    else:
        form = forms.BookForm()
    return render(request, 'create_book.html', {'form': form})


def view_book_drop(request, id):
    lang_id = get_object_or_404(models.Book, id=id)
    lang_id.delete()
    return HttpResponse('Удален успешно!')


def view_book_delete(request):
    lang_value = models.Book.objects.all()
    return render(request, 'book_list.html', {'book_key': lang_value})

