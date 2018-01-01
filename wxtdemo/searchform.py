from django import forms
from .models import ATI


class SearchForm(forms.Form):
    searchtext = forms.CharField(
        label='Enter search terms:',
        required=True,
        widget=forms.TextInput,
        error_messages={
            'required': 'Please enter your search terms'
        }
    )
