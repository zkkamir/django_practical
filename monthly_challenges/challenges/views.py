from django.shortcuts import render
from django.http import HttpResponse, HttpResponseNotFound


def monthly_challenges_by_number(request, month):
    return HttpResponse(month)


def monthly_challenges(request, month):
    challenge_text = None
    if month == "january":
        challenge_text = "Eat more fruits!"
    elif month == "february":
        challenge_text = "Walk!"
    elif month == "march":
        challenge_text = "Read!"
    else:
        return HttpResponseNotFound("This month is not supported!")
    return HttpResponse(challenge_text)
