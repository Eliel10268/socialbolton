from django import forms

class CreateAccountForm(forms.Form):
    fullname = forms.CharField(max_length=100)
    email = forms.EmailField()
    password = forms.CharField(max_length=100)
    password_confirmation = forms.CharField(max_length=100)


    def clean(self):
        cleaned_data = super().clean()
        pwd = cleaned_data.get("password")
        pwd_conf = cleaned_data.get("password_confirmation")
        if pwd != pwd_conf:
            raise forms.ValidationError("Paswords not the same!")
        return cleaned_data



class LoginForm(forms.Form):
    email = forms.EmailField()
    password = forms.CharField()


