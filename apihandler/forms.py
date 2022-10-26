from django import forms

class search_user_form(forms.Form):
    query = forms.CharField()