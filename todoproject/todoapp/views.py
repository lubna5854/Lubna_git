from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from . models import Task
from . forms import Todoforms
from django.views.generic import ListView,DetailView,UpdateView,DeleteView
# Create your views here.

class Tasklistview(ListView):
     model=Task
     template_name='home.html'
     context_object_name='task1'

class Taskdetailview(DetailView):
     model=Task
     template_name='detail.html'
     context_object_name='task'

class Taskupdateview(UpdateView):
     model=Task
     template_name='update.html'
     context_object_name='task2'
     fields=('name','prio','date')

     def get_success_url(self):
          return reverse_lazy('cbvdetail',kwargs={'pk':self.object.id})

class Taskdeleteview(DeleteView):
     model=Task
     template_name='delete.html'
     success_url=reverse_lazy('cbview')



def homefun(request):
    task1=Task.objects.all()
    if request.method=="POST":
        name=request.POST.get('task','')
        priority=request.POST.get('priority','')
        date=request.POST.get('date','')
        task=Task(name=name,prio=priority,date=date)
        task.save()
    return render(request,"home.html",{'task1':task1})

def deletefun(request,taskid):
    task=Task.objects.get(id=taskid)
    if request.method=="POST":
        task.delete()
        return redirect('/')
    return render(request,'delete.html')

def updatefun(request,id):
        task1=Task.objects.get(id=id)
        f=Todoforms(request.POST or None, instance=task1)
        if f.is_valid():
             f.save()
             return redirect('/')
        
        return render(request,'edit.html',{'form':f,'task':task1})
    