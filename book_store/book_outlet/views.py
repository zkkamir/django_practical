from django.shortcuts import get_object_or_404, render
from django.http import Http404
from django.db.models import Avg

from .models import Book


def index(request):
    all_books = Book.objects.all().order_by("-rating")
    tnob = all_books.count()
    average_rating = all_books.aggregate(Avg("rating"))

    return render(request, "book_outlet/index.html", context={
        "all_books": all_books,
        "total_number_of_books": tnob,
        "average_rating": average_rating
    })


def book_detail(request, slug):
    # try:
    #     book = Book.objects.get(pk=id)
    # except:
    #     raise Http404
    book = get_object_or_404(Book, slug=slug)
    return render(request, "book_outlet/book-detail.html", context={
        "book": book,
    })
