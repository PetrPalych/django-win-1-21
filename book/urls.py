from django.urls import path
from . import views

urlpatterns = [
    path('', views.BookListView.as_view()),
    path('book_list/', views.BookDeleteListView.as_view()),
    path('book_detail/<int:pk>/', views.BookDetailView.as_view()),
    path('add-comment/', views.ReviewCreateView.as_view()),
    path('create_book/', views.BookCreateView.as_view()),
    path('book_list/<int:pk>/delete/', views.BookDeleteView.as_view()),
    path('book_list/<int:pk>/update/', views.BookUpdateView.as_view()),
]
