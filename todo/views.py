from django.shortcuts import redirect,render
from todo.models import Task
# Create your views here.

def addtask(request):
    # Logic to add a task
    task = request.POST.get('task')
    Task.objects.create(task=task)

    return redirect('home')

def mark_as_done(request, pk):
    # Logic to mark a task as done
    task = Task.objects.get(pk=pk)
    task.is_completed = True
    task.save()

    return redirect('home')

def mark_as_undone(request, pk):
    # Logic to mark a task as undone
    task = Task.objects.get(pk=pk)
    task.is_completed = False
    task.save()

    return redirect('home')

def edit_task(request, pk):
    # Logic to edit a task
    get_task = Task.objects.get(pk=pk)
    if request.method == 'POST':
        new_task = request.POST.get('task')
        get_task.task = new_task
        get_task.save() 
        return redirect('home')
    else:
        context = {
            'get_task': get_task,
        }
        

    return render(request, 'edit_task.html', context)

def delete_task(request, pk):
    # Logic to delete a task
    task = Task.objects.get(pk=pk)
    task.delete()

    return redirect('home')