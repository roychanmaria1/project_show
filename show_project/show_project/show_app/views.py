from django.http import HttpResponse
from django.shortcuts import render, redirect
from . models import Show
from .forms import ShowForm
# Create your views here.
def index(request):
    show = Show.objects.all()
    context = {
        'show_list':show
    }
    return  render(request,'index.html',context)


def detail(request,show_id):
    show = Show.objects.get(id=show_id)
    return render(request,"detail.html",{'show':show})

def add_show(request):
    if request.method == "POST":
        name = request.POST.get('name', )
        desc = request.POST.get('desc', )
        year = request.POST.get('year', )
        img = request.FILES['img']
        show = Show(name=name, desc=desc, year=year, img=img)
        show.save()
        return redirect('/')
    return render(request,'add.html')

def update(request,id):
    show = Show.objects.get(id=id)
    form = ShowForm(request.POST or None,request.FILES,instance=show)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'show':show})

def delete(request,id):
    if request.method == 'POST':
        show = Show.objects.get(id=id)
        show.delete()
        return redirect('/')
    return render(request,'delete.html')



