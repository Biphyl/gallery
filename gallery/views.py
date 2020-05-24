from .models import Category,Image,Location
from django.shortcuts import render,redirect
from django.http import HttpResponse
import datetime as dt

# Create your views here.
def index(request):
    photo=Image.display_photo()
    return render (request ,'index.html',{"photo":photo})


def photo_today(request):
    date = dt.date.today()
    photo = Image.display_photo()
    return render(request, 'photos/todays_photos.html', {"date":date,"photo":photo})

def convert_dates():
    # Function that get the weekday number for the date.
    day_number = dt.date.weekday(dates)

    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday',"Sunday"]

    # Returning the actual day of the week
    day = days[day_number]
    return day

# View Function to present news from the past days
def past_days_photos(request,past_date):

    try:
        # Convert data from the string Url
        date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()

    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404()
        assert False
    
    if date == dt.date.today():
        return redirect(news_of_day)

    photo = Image.days_photo(date)
    return render(request, 'photos/past_photos.html', {"date": date,"photo":photo})

def search_results(request):

    if 'category' in request.GET and request.GET["category"]:
        search_term = request.GET.get("category")
        searched_category = Category.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'photos/search.html',{"message":message,"category": searched_category})

    else:
        message = "You haven't searched for any term"
        return render(request, 'photos/search.html',{"message":message})

def category(request,category_id):
    try:
        category = Category.objects.get(id = category_id)
    except DoesNotExist:
        raise Http404()
    return render(request,"photos/category.html", {"category":category})
