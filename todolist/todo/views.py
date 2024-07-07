from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import todoses
from .forms import todos, updater
from django.shortcuts import get_object_or_404
# Create your views here.
tasks = todoses.objects.all()
def todolis(request):
    tasks = todoses.objects.all()
    condition = len(tasks)
    form = None
    # print(todos(request.post))
    if request.method == 'POST':
        form = todos(request.POST)
        if form.is_valid():
            task = todoses()
            task.task = form.cleaned_data['name']
            task.save()
        return HttpResponseRedirect('/todo/')
    else:
        form =  {"todo":todos(),"update":updater()}
        tasks = reversed(tasks)
        return render(request,"todo.html",{'todos': todos,'form':form,'tasks':tasks,'len':condition})
    

def delete(request,ids):
         print(request)
         todoses.objects.filter( id = ids).delete()
         return HttpResponseRedirect("/todo/")

# update function
def update(request,ids):
     if request.method == 'POST':
        form = updater(request.POST)
        if form.is_valid():
             taskes = form.cleaned_data['new_value']
             todoses.objects.filter( id = ids).update(task = taskes )
        return HttpResponseRedirect('/todo/')
         
# too delete from database
    # a = student.objects.all()
    # b = a[0].name
    # print(b)
    # student.objects.filter(name = b).delete()