from django.shortcuts import render

# Create your views here.
def index(request):
    d={'name':'Lotus','age':22}
    return render(request,'index.html',context=d)