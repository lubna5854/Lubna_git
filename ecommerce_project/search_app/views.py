from django.shortcuts import render
from shopapp.models import Product
from django.db.models import Q

# Create your views here.
def search_result(request):
    products=None
    query=None
    if 'q' in request.GET:
        query=request.GET.get('q')
        q_products=Product.objects.all().filter(Q(name__contains=query) | Q(descr__contains=query))
        return render(request,'search.html',{'query':query,'products':q_products})