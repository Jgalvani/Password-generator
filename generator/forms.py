from django import forms

class PasswordForm(forms.Form):
    length = forms.IntegerField(min_value=4, max_value=16, label='nombre de caractères')
    upper = forms.BooleanField(required=False, label='majuscules')
    lower = forms.BooleanField(required=False, label='minuscules')
    special = forms.BooleanField(required=False, label='caractères_spéciaux')
    number = forms.BooleanField(required=False, label='chiffres')
