from django.shortcuts import render

# Create your views here.
def staticfun(request):
    return render(request,"index.html")