from django import forms


class ReviewForm(forms.Form):
    username = forms.CharField(max_length=10, error_messages={
        "required": "Username must not be empty.",
        "max_length": "Please enter a shorter Username."
    })
    review_text = forms.CharField(
        label="Your Feedback", widget=forms.Textarea, max_length=200)
    rating = forms.IntegerField(label="Your Rating", min_value=1, max_value=5)
