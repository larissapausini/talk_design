import os

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
    return render(request, 'pacotes_london_design.html')


def london_retro(request):
    return render(request, 'pacotes_london_retro.html')


def parceiros(request):
    return render(request, 'parceiros.html')


def contact(request):
    contact_name = request.POST.get(
                  'inputName', '')
    contact_email = request.POST.get(
                  'inputEmail', '')
    contact_phone = request.POST.get(
                  'inputPhone', '')
    contact_msg = request.POST.get(
                  'inputMsg', '')

    template = get_template('contact_template.txt')
    context = {
              'contact_name': contact_name,
              'contact_email': contact_email,
              'contact_phone': contact_phone,
              'contact_msg': contact_msg,
              }
    content = template.render(context)

    email = EmailMessage('New contact from Talk Design',
                         content,
                         contact_email,
                         [os.environ['OWNER_EMAIL']],
                         headers={'Reply-To': contact_email }
                         )
    email.send()
    return redirect('/')


def contact_tour(request):
    contact_name = request.POST.get(
                  'inputName', '')
    contact_email = request.POST.get(
                  'inputEmail', '')
    contact_phone = request.POST.get(
                  'inputPhone', '')
    contact_language = request.POST.get(
                  'inputLanguage', '')
    contact_country = request.POST.get(
                  'inputCountry', '')
    contact_city = request.POST.get(
                  'inputCity', '')
    contact_nationality = request.POST.get(
                  'inputNationality', '')
    contact_qty = request.POST.get(
                  'inputQty', '')
    contact_date = request.POST.get(
                  'inputDate', '')

    template = get_template('contact_tour_template.txt')
    context = {
              'contact_name': contact_name,
              'contact_email': contact_email,
              'contact_phone': contact_phone,
              'contact_language': contact_language,
              'contact_country': contact_country,
              'contact_city': contact_city,
              'contact_nationality': contact_nationality,
              'contact_qty': contact_qty,
              'contact_date': contact_date,
              }
    content = template.render(context)

    email = EmailMessage('New booking for London Design tour',
                         content,
                         contact_email,
                         [os.environ['OWNER_EMAIL']],
                         headers={'Reply-To': contact_email }
                         )
    email.send()
    return redirect('london_design')
