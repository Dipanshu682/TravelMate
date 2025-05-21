from django import forms
from .models import Profile


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ["name", "age", "gender", "bio", "location", "profile_picture"]

    def clean_age(self):
        age = self.cleaned_data.get("age")
        if age is not None and age <= 0:
            raise forms.ValidationError("Age must be a positive number.")
        return age
