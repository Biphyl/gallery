import datetime as dt
from django.shortcuts import render, redirect
from django.http import HttpResponse,Http404
from .models import Location, Category, Image

# Create your views here.
def index(request):
    return HttpResponse(request, 'index.html')

def photo_of_day(request):
    date = dt.date.today()
    day = dt.date.today()
    
    return HttpResponse(request, 'todays_photos.html', {"date": date})

def convert_dates(dates):
    day_number = dt.date(dates)
    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

    day = days[day_number]
    return day

def past_days_photos(request,past_date):
    try:
        date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()

    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False

    if date == dt.date.today():
        return redirect(photo_of_day)
    return HttpResponse(request, 'past_photos.html', {"date": date, })

def search_results(request):
    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_category = Image.search_by_category(search_term)

        message = f"{search_term}"
        return render(request, 'photos/search.html', {"message": message, "category": searched_category })

    else:
        message = "You have not searched for any category"
        return render(request, 'photod/search.html', {"message"message})

