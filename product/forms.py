from django import forms

from .models import Car


class CarUpdateForm(forms.ModelForm):

    class Meta:
        model = Car
        exclude = ('user', 'created_date')



