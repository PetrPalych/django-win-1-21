from django.forms import forms
from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView, CreateView, DeleteView

from . import models, forms


# Create your views here.


class BookListView(ListView):
    model = models.Book
    queryset = models.Book.objects.all()
    context_object_name = "books"
    template_name = "book_view.html"


class BookDeleteListView(ListView):
    model = models.Book
    queryset = models.Book.objects.all()
    context_object_name = "book_key"
    template_name = "book_list.html"


class BookDetailView(DetailView):
    model = models.Book
    queryset = models.Book.objects.all()
    context_object_name = "book"
    template_name = "book_detail.html"


class BookCreateView(CreateView):
    model = models.Book
    form_class = forms.BookForm
    success_url = "/"
    template_name = "create_book.html"


class ReviewCreateView(CreateView):
    model = models.ReviewBook
    form_class = forms.ReviewForm
    success_url = "/"
    template_name = "create_review_for_book.html"


class BookDeleteView(DeleteView):
    model = models.Book
    success_url = "/"


class BookUpdateView(CreateView):
    model = models.Book
    form_class = forms.BookForm
    success_url = "/"
    template_name = "book_update.html"
