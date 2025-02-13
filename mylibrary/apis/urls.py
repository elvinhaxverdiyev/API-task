from django.urls import path
from .views import BookView, BookDetailView, BookSlugView

urlpatterns = [
    path('books/', BookView.as_view(), name="book-list"), 
    path('books/<int:pk>/', BookDetailView.as_view(), name="book-detail"), 
    path('book/<slug:slug>/', BookSlugView.as_view(), name="book-detail-slug"), 
]
