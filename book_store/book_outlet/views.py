from django.shortcuts import get_object_or_404, render
from django.http import Http404

from .models import Book


def index(request):
    all_books = Book.objects.all()
    return render(request, "book_outlet/index.html", context={
        "all_books": all_books
    })


def book_detail(request, id):
    # try:
    #     book = Book.objects.get(pk=id)
    # except:
    #     raise Http404
    book = get_object_or_404(Book, pk=id)
    return render(request, "book_outlet/book-detail.html", context={
        "book": book
    })
