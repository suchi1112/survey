from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render, redirect
from . models import Sample

# Create your views here.
def register(request):

    return render(request, "register.html", )

def add_survey(request):
    if request.method=='POST':
        question=request.POST.get('question',)
        answer = request.POST.get('answer', )
        survey=Sample(question=question,answer=answer)
        survey.save()
        return redirect('/')
    return render(request,"add.html",)
def index(request):
    sur=Sample.objects.all()
    context={
        'movie_list':sur
    }
    return render(request,"home.html",context)

def thank(request):

    return render(request, "thank.html", )