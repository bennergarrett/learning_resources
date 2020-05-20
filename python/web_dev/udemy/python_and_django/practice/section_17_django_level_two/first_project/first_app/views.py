from django.shortcuts import render
##added
##
from django.http import HttpResponse
from first_app.models import Topic, Webpage, AccessRecord
# Create your views here.

##added code
##created view called index
##by convention input called request
##
def index(request):
    ## SQL command
    ##
    webpages_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records' :webpages_list}
    ##must return http model
    ##
    ##return HttpResponse("Hello World!")
    return render(request, 'first_app/index.html', date_dict)

def help(request):
    my_dict = {'insert_help': "Help Page"}
    return render(request, 'first_app/help.html', my_dict)

