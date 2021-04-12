from django.shortcuts import render
from django.http import HttpResponse
from django.template import RequestContext

from .forms import PasswordForm

import random
import string


MIN_CHARS_RANGE = 4

# Create your views here.
def home(request):
    form = PasswordForm(request.GET or None)

    return render(request, 'generator/home.html', {'form': form})

def password(request):
    chars = ''

    if request.GET.get('lower'):
        chars += string.ascii_lowercase

    if request.GET.get('upper'):
        chars += string.ascii_uppercase

    if request.GET.get('number'):
        chars += string.digits

    if request.GET.get('special'):
        chars += string.punctuation

    length = request.GET.get('length', MIN_CHARS_RANGE)
    password = ''

    if chars:
        for i in range(int(length)):
            password += random.choice(chars)

    return render(request, 'generator/password.html', {'password': password})