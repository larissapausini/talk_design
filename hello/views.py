from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.template import Context


# Create your views here.
def index(request):
    return render(request, 'index.html')


def pacotes(request):
    return render(request, 'pacotes.html')


def london_design(request):
    return render(request, 'london_design.html')


def parceiros(request):
    return render(request, 'parceiros.html')


def contact(request):
    contact_name = request.POST.get(
                   'inputName',
                   '')
    contact_email = request.POST.get(
                   'inputEmail',
                   '')
    contact_phone = request.POST.get(
                   'inputPhone',
                   '')
    contact_language = request.POST.get(
                   'inputLanguage',
                   '')
    contact_qty = request.POST.get(
                   'inputQty',
                   '')
    contact_date = request.POST.get(
                   'inputDate',
                   '')

    email = EmailMessage('New contact form submission',
                         'Body goes here',
                         'renata@talkdesign.co',
                         ['casanova.leandro@gmail.com'],
                         reply_to=['renata@talkdesign.co'],
                         headers={'Message-ID': 'foo'}
                         )
    email.send()
    return redirect('london_design')
