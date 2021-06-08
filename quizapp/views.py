from django.shortcuts import render,redirect
from django.http import HttpResponse
from quizapp.models import QUIZFORM


def mainpage(request): #directs to main  index.html 
    return render(request,"index.html")

def panel(request):       #directs to panel.html
    return render(request,'quizpanel.html')
    

def beginner(request):   #directs to beginner.html
    Result = QUIZFORM.objects.all()
    return render(request,"beginner.html",{"QUIZFORM":Result})


def portfolio(request):       #directs to portfolio.html
    return render(request,'portfolio.html')
def aboutus(request):       #directs to aboutus.html
    return render(request,'aboutus.html')