from django.shortcuts import render, redirect
from .models import Team
from cars.models import Car
from django.core.mail import send_mail
from django.contrib.auth.models import User
from django.contrib import messages

# Create your views here.

def home(request):
    teams = Team.objects.all()
    featured_cars = Car.objects.order_by('-created_date').filter(is_featured=True)
    all_cars = Car.objects.order_by('-created_date')

    #search_fields = Car.objects.all() ==>> #This doesn't work
    #
    # {% for search in search_field %}
    #
    # {{search. model}} {{search. model}} {{search. model}} {{search. model}}



    #search_fields = Car.objects.values('model', 'city', 'year', 'body_style') ==>> #This doesn't work
    #
    # {% for model in search_fields %} ### {% for city in search_fields %} ### {% for year in search_fields %} ### {% for body_style in search_fields %}
    #
    # {{model.model}}###{{city.city}}###{{year.year}}###{{body_style. body_style}}


    model_search = Car.objects.values_list('model', flat=True).distinct()
    city_search = Car.objects.values_list('city', flat=True).distinct()
    year_search = Car.objects.values_list('year', flat=True).distinct()
    body_style_search = Car.objects.values_list('body_style', flat=True).distinct()

    context = {
        'teams': teams,
        'featured_cars': featured_cars,
        'all_cars': all_cars,
        'model_search': model_search,
        'city_search': city_search,
        'year_search': year_search,
        'body_style_search': body_style_search,
    }

    return render(request, 'pages/home.html', context)

#########################################################################

def about(request):
    teams = Team.objects.all()

    context = {
        'teams': teams
    }

    return render(request, 'pages/about.html', context)

#########################################################################

def services(request):
    return render(request, 'pages/services.html')

##########################################################################

def contact(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        phone = request.POST['phone']
        message = request.POST['message']

        email_subject = 'You have a new message from Carzone website regarding ' + subject
        message_body = 'Name: ' + name + '. Email: ' + email + '. Phone: ' + phone + '. Message: ' + message

        admin_info = User.objects.get(is_superuser=True)
        admin_email = admin_info.email 

        send_mail(
        email_subject,
        message_body,
        "msm.793@hotmail.com",
        [admin_email],
        fail_silently=False,
        )

        messages.success(request, 'Thank you for contacting us. We will get back to you shortly')
        return redirect('contact')

    return render(request, 'pages/contact.html')

##########################################################################
