from django.shortcuts import redirect, render
# Create your views here.
from . import forms
from . import models
def home(request):
    task = models.ToDoModel.objects.all()
    return render(request,'todo.html',{'task':task}) #

def add_task(request):
    if request.method == 'POST':
        form = forms.ToDoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('todo')
    else:
        form = forms.ToDoForm()
    return render(request, 'add_todo.html', {'todoform' : form})

def delete_todo(request, id):
    task=models.ToDoModel.objects.get(pk=id).delete()
    return redirect("todo")

def edit_todo(request, id):
    task = models.ToDoModel.objects.get(pk = id)
    form = forms.ToDoForm(instance = task)
    if request.method == 'POST':
        form = forms.ToDoForm(request.POST, instance = task)
        if form.is_valid():
            form.save()
            return redirect('todo')
    return render(request, 'add_todo.html', {'todoform':form})

def done_todo(request, id):
    task = models.ToDoModel.objects.get(pk=id)
    task.status = True
    task.save()
    return redirect('todo')
    