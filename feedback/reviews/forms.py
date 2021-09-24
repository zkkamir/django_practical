from django import forms
from django.forms import fields

from .models import Review


class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = "__all__"
        labels = {
            "username": "Your Name",
            "review_text": "Your Feedback",
            "rating": "Your Rating"
        }
        error_messages = {
            "username": {
                "required": "Your name must not be empty!",
                "max_length": "Please enter a shorter name!"
            }
        }
