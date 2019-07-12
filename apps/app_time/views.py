from django.shortcuts import render
from time import gmtime, strftime
    
def index(request):
    context = {
        "time": strftime("%b-%d-%y %I:%M %P", gmtime())
    }
    return render(request,'app_time/index.html', context)

def timedisplay(request):
    return(index(request))