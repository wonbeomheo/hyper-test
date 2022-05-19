from django import forms


class UserForm(forms.Form):
    validationFirstname = forms.CharField(label='First Name', max_length=50)
    validationLastname = forms.CharField(label='Last Name', max_length=50)
    validationUsername = forms.CharField(label='Username', max_length=50)
    validationPassword = forms.CharField(label='Password', max_length=50, widget=forms.PasswordInput)
    validationEmail = forms.CharField(label='Email', max_length=50, widget=forms.EmailInput)
