from django.urls import path
from . import views

urlpatterns = [
    path('', views.view_book),
    path('book_detail/<int:id>/', views.detail_view),
    path('add-comment/', views.create_review_for_book),
    path('create_book/', views.create_view_book_post),
    path('book_list/<int:id>/delete/', views.view_book_drop),
    path('book_list/', views.view_book_delete),
]
