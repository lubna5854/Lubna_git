
from django.shortcuts import redirect, render
from . models import Movie
from . form import Movieform

# Create your views here.
def index(request):
    movieobj=Movie.objects.all()
    context={
        'movie_list':movieobj
    }
    
    return render(request,'index.html',context)

def detailfun(request,movie_id):
    movie=Movie.objects.get(id=movie_id)
    return render(request,"detail.html",{'movieobj1':movie})


def addfun(request):
    if request.method=="POST":
        name=request.POST.get('mname')
        desc=request.POST.get('mdesc')
        yr=request.POST.get('myear')
        img=request.FILES['mimage']
        movie=Movie(name=name,desc=desc,year=yr,img=img)
        movie.save()
    return render(request,"add.html")


def updatefun(request,id):
    mov=Movie.objects.get(id=id)
    form=Movieform(request.POST or None, request.FILES, instance=mov)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,"edit.html",{'form':form,'movie':mov})

def deletefun(request,id):
    if request.method=="POST":
        dmov=Movie.objects.get(id=id)
        dmov.delete()
        return redirect('/')
    return render(request,"delet.html")