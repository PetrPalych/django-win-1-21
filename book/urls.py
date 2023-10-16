from django.urls import path
from .views import *

urlpatterns = [
    path('', view_book),
    path('<int:id>', detail_view)
]