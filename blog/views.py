from django.shortcuts import render #we can return template insted of httpResponse
from .models import Post


  
def home(request):
    context ={
        'posts':Post.objects.all()
    }
     
    return render(request,'blog/home.html',context)

def about(request):
    return render(request,'blog/about.html',{'title':'About'})