from django.shortcuts import render

# Create your views here.



def courses(request):
    return render(request,'course/courses.html')

def trainers(request):
    return render(request,'course/trainers.html')

def events(request):
    return render(request,'course/events.html')

def pricing(request):
    return render(request,'course/pricing.html')