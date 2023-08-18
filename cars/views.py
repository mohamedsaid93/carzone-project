from django.shortcuts import render, get_object_or_404
from .models import Car
from django.core.paginator import EmptyPage, PageNotAnInteger, Paginator

# Create your views here.

def cars(request):
    cars = Car.objects.order_by('-created_date')

    paginator = Paginator(cars,4)
    page = request.GET.get('page')
    paged_cars = paginator.get_page(page)


    context = {
        'cars': paged_cars,
    }

    return render(request, 'cars/cars.html', context)

###############################################################################

def car_detail(request, id):
    single_car = get_object_or_404(Car, pk=id)

    context = {
        'single_car': single_car
    }
    return render(request, 'cars/car_detail.html', context)

##################################################################################

def search(request):
    cars = Car.objects.order_by('-created_date')

    if 'keyword' in request.GET:          # try if request.method == 'GET' and else
        keyword = request.GET['keyword']
        if keyword:
            cars = Car.objects.filter(description__icontains=keyword)


    if 'model' in request.GET:          
        model = request.GET['model']
        if model:
            cars = Car.objects.filter(model__iexact=model)

    
    if 'city' in request.GET:          
        city = request.GET['city']
        if city:
            cars = Car.objects.filter(city__iexact=city)


    if 'year' in request.GET:          
        year = request.GET['year']
        if year:
            cars = Car.objects.filter(year__iexact=year)


    if 'body_style' in request.GET:          
        body_style = request.GET['body_style']
        if body_style:
            cars = Car.objects.filter(body_style__iexact=body_style)


    if 'min_price' in request.GET:          
        min_price = request.GET['min_price']
        max_price = request.GET['max_price']

        if max_price:
            cars = Car.objects.filter(price__gte=min_price, price__lte=max_price)


    context = {
        'cars': cars
    }

    return render(request, 'cars/search.html', context)
