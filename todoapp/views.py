from django.shortcuts import render,redirect
from .models import TodoModel
from .forms import TodoForm
from django.urls import reverse
# Create your views here.
def list_task(request):
    list_of_tasks = TodoModel.objects.all()
    return render(request,'index.html',{'task_list':list_of_tasks})

def create_task(request):
    todo_form = TodoForm(request.POST or None)
    if request.method=='POST':
        if todo_form.is_valid():
            todo_form.save()
            return redirect(reverse('list_tasks'))
    return render(request,'add_task.html',{'todo_form':todo_form})


def edit_task(request,id):
    todoinstance = TodoModel.objects.filter(pk=id).first()
    todo_form = TodoForm(request.POST or None,instance=todoinstance)
    if request.method=='POST':
        if todo_form.is_valid and todo_form.has_changed():
            todoinstance.name = request.POST.get("name")
            todoinstance.status = request.POST.get("status")
            todoinstance.save()
            return redirect(reverse('list_tasks'))
    return render(request,'add_task.html',{'todo_form':todo_form})

def delete_task(request,id):
    istance = TodoModel.objects.get(pk=id)
    istance.delete()
    return redirect(reverse('list_tasks'))
 

