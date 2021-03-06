from django.shortcuts import render
from django.http import Http404, HttpResponseNotFound, HttpResponseRedirect, response
from django.urls import reverse


monthly_challenges = {
    "january": "challenge for jan",
    "february": "challenge for feb",
    "march": "challenge for mar",
    "april": "challenge for apr",
    "may": "challenge for may",
    "june": "challenge for jun",
    "july": "challenge for jul",
    "august": "challenge for aug",
    "september": "challenge for sep",
    "october": "challenge for oct",
    "november": "challenge for nov",
    "december": None
}


def index(request):
    list_items = ""
    months = list(monthly_challenges.keys())

    return render(request, "challenges/index.html", {
        "months": months
    })

    # for month in months:
    #     capitalized_month = month.capitalize()
    #     month_path = reverse("month-challenge", args=[month])
    #     list_items += f'<li><a href="{month_path}">{capitalized_month}</a></li>'

    # response_data = f"<ul>{list_items}</ul>"
    # return HttpResponse(response_data)


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("<h1>Invalid month!</h1>")

    redirect_month = months[month - 1]
    redirect_path = reverse("month-challenge", args=[redirect_month])
    return HttpResponseRedirect(redirect_path)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return render(request, "challenges/challenge.html", {
            "text": challenge_text,
            "month": month
        })
        # response_data = render_to_string("challenges/challenge.html")
        # return HttpResponse(response_data)
    except:
        raise Http404()
