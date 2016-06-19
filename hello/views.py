from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.template.loader import get_template
from django.core.mail import EmailMessage
from django.template import Context

from rq import Queue
from worker import conn


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

    q = Queue(connection=conn)

    email = EmailMessage('New contact form submission',
                         'Body goes here',
                         'renata@talkdesign.co',
                         ['casanova.leandro@gmail.com'],
                         reply_to=['renata@talkdesign.co'],
                         headers={'Message-ID': 'foo'}
                         )
    result = q.enqueue(email.send)
    return redirect('london_design')
