from django import forms
from .models import TripPreference, Comment


class TripPreferenceForm(forms.ModelForm):
    class Meta:
        model = TripPreference
        fields = ("destination", "date")


class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ["text"]
        widgets = {
            "text": forms.Textarea(attrs={"rows": 4}),
        }
