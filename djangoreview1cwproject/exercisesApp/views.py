from django.shortcuts import render
from django.http import HttpResponse

 # Create your views here.
# def index(request):
#      context = {"pages": pages}
#     return render(request, 'exercisesApp/pages.html', context)

def home(request):
    return HttpResponse("This came from the Home page.")


def page2(request):
    return HttpResponse("This came from page 2.")

def page3(request):
    return HttpResponse("This came from page 3.")

def page4(request):
    return HttpResponse("This came from page 4.")

def page5(request):
    return HttpResponse("This came from page 5.")