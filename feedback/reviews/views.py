from django.http import HttpResponseRedirect
from django.shortcuts import render

from .forms import ReviewForm
from .models import Review


def review(request):
    if request.method == "POST":
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = Review(
                username=form.cleaned_data["username"],
                review_text=form.cleaned_data["review_text"],
                rating=form.cleaned_data["rating"])
            review.save()
            return HttpResponseRedirect("/thank-you")
    else:
        form = ReviewForm()

    return render(request, "reviews/review.html", {
        "form": form
    })


def thank_you(request):
    return render(request, "reviews/thank_you.html")
