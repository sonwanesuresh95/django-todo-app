from django.shortcuts import render, redirect
from .forms import Taskform
from .models import Task


# Create your views here.
def show(request):
    if request.method == 'POST':
        form = Taskform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = Taskform()
        records = Task.objects.all()
        return render(request, 'todoapp/show.html', context={"form": form, "records":records[::-1]})


def done(request, id):
    record = Task.objects.get(id=id)

    if record.done:
        record.done = False
    else:
        record.done = True
    record.save()
    return redirect('/')


def delete(request, id):
    record = Task.objects.get(id=id)
    record.delete()
    return redirect('/')
