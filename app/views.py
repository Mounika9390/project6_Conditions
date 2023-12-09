from django.shortcuts import render

# Create your views here.
def conditions(request):
    d={'a':10,'b':25,'c':10}
    return render(request,'conditions.html',d)