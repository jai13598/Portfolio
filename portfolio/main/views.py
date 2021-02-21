from django.shortcuts import render

# Create your views here.
def index(request):
    context={}
    return render(request,'main/index.html',context)
def projects(request):
    context={}
    return render(request,'main/projects.html',context)
def skills(request):
    context={}
    return render(request,'main/skills.html',context)