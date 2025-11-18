from django import forms


class AddNewPost(forms.Form):
    text = forms.CharField()