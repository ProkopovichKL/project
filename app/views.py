from django.shortcuts import render, redirect
from app.models import Offers
from app.forms import ContactForm
from app.forms import ClientForm

from django.template.loader import get_template
from django.core.mail import EmailMultiAlternatives
from django.http import HttpResponseRedirect


def home(request):
    offers = Offers.objects.all()
    if request.method == 'POST':
        form = ClientForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/seccess')
        else:
            return HttpResponseRedirect('/fails')
    else:
        form = ClientForm()
    return render(request, "home.html", {'offers':offers, 'form': form})

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            send_message(form.cleaned_data['name'], form.cleaned_data['email'], form.cleaned_data['message'])
            return HttpResponseRedirect('/seccess')
        else:
            return HttpResponseRedirect('/fails')
    else:
        form = ContactForm()
    return render(request, 'contact.html', {'form': form})

def send_message(name, email, message):
    html = get_template('message.html')
    text = get_template('message.html')
    context = {'name': name, 'email': email, 'message': message}
    subject = 'Message from the client'
    from_email = email
    text_content = text.render(context)
    html_content = html.render(context)
  
    msg = EmailMultiAlternatives(subject, text_content, from_email, ['tomashovec@gmail.com'])
    msg.attach_alternative(html_content, 'text/html')
    msg.send()

def seccess(request):
    return render(request, 'seccess.html')

def fails(request):
    return render(request, 'fails.html')