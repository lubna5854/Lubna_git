
from django.shortcuts import redirect, render
from django.contrib.auth.models import User
from django.contrib import messages, auth

# Create your views here.
def logfun(request):
    if request.method=='POST':
        user_name=request.POST['username']
        pass_word=request.POST['password']
        authvar=auth.authenticate(username=user_name,password=pass_word)

        if authvar is not None:
            auth.login(request,authvar)
            return redirect('/')
        else:
            messages.info(request,"invalid credentials")
            return redirect('logfun')
             
    return render(request,"loginpg.html") 



def regfun(request):
    if request.method=='POST':
        user_name=request.POST['username']
        first_name=request.POST['first_name']
        l_name=request.POST['last_name']
        email=request.POST['email']
        pword=request.POST['p_word']
        cpword=request.POST['cp_word']
        if pword==cpword:
            if User.objects.filter(username=user_name).exists():
                messages.info(request,"Username already Exists")
                return redirect('regfun')
            elif User.objects.filter(email=email).exists():
                messages.info(request,"Email already exists")
                return redirect('regfun')
            else:
                user=User.objects.create_user(username=user_name,password=pword,first_name=first_name,last_name=l_name,email=email)
                user.save();
                return redirect('logfun')
            
        else:
            messages.info(request,"Password not matching!!")
            return redirect('regfun')
      
    return render(request,"register.html") 

def logoutfun(request):
    auth.logout(request)
    return redirect('/')