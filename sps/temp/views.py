from django.shortcuts import render, HttpResponse
# from .models import tempModel
from .forms import tempForm

# Create your views here.
def temp_home(request):
    return render(request, "temp/home.html")

def tempData(request):
    # return HttpResponse("Everything going good")
    form = tempForm()
    context = {
        'form':form,
        }
    return render(request, 'temp/temp.html', context )
    