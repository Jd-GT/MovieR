from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html',{'name':'El Gran david'})

def about(request):
    return render(request, 'about.html')

def abou(request):
    return render(request, 'abou.html')