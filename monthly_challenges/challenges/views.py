from django.http.response import HttpResponseRedirect
from django.shortcuts import redirect, render
from django.http import HttpResponse, HttpResponseNotFound


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
    "december": "challenge for dec"
}


def monthly_challenge_by_number(request, month):
    months = list(monthly_challenges.keys())

    if month > len(months):
        return HttpResponseNotFound("Invalid month!")

    redirect_month = months[month - 1]
    return HttpResponseRedirect("/challenges/" + redirect_month)


def monthly_challenge(request, month):
    try:
        challenge_text = monthly_challenges[month]
        return HttpResponse(challenge_text)
    except:
        return HttpResponseNotFound("This is not a valid month!")
