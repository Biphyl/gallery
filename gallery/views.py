import datetime as dt
from django.shortcuts import render
from django.http import HttpResponse,Http404

# Create your views here.
def index(request):
    return HttpResponse(request, 'index.html')

def photo_of_day(request):
    date = dt.date.today()
    day = dt.date.today()
    html = f'''
        <html>
            <body>
                <h1> {date.day}-{date.month}-{date.year}</h1>
            </body>
        </html>
            '''
    return HttpResponse(html)

def convert_dates(dates):
    day_number = dt.date.(dates)
    days = ['Monday','Tuesday','Wednesday','Thursday','Friday','Saturday','Sunday']

    day = days[day_number]
    return day

def past_days_photos(request,past_date):
    try:
        date = dt.datetime.strptime(past_date,'%Y-%m-%d').date()

    except ValueError:
        # Raise 404 error when ValueError is thrown
        raise Http404())
    return HttpResponse(html)