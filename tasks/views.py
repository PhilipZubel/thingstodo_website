from django.shortcuts import render
import datetime
from django.utils import timezone

# Create your views here.
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required


from .models import Task
from .forms import TaskForm
from django.shortcuts import redirect, reverse
from django.http import HttpResponseRedirect

@login_required
def welcome(request):
	context = {} 
	tasks = Task.objects.filter(user = request.user)
	context['tasks_total'] = tasks.count()
	context['tasks_completed'] = tasks.filter( isCompleted = True).count()
	context['tasks_incompleted'] = context['tasks_total'] - context['tasks_completed']
	context['tasks_past_deadline'] = tasks.filter(isCompleted = False).filter(date__lt=datetime.date.today()).count()
	return render(request, 'tasks/welcome_page.html', {'context': context})

@login_required
def tasks(request, task_type):
	context = {}
	context['task_type'] = task_type
	print(timezone.now)
	if request.method == 'GET':
		pass;
	elif request.method == 'POST':
		form = TaskForm(request.POST)
		if form.is_valid():
			form.instance.user = request.user
			form.save()
	tasks = Task.objects.filter(user = request.user)
	
	if task_type == "Completed":
		context['tasks'] = tasks.filter(isCompleted = True) 
	elif task_type == "Incomplete":
		context['tasks'] = tasks.filter(isCompleted = False) 
	else:
		context['tasks'] = tasks

	return render(request, 'tasks/tasks.html', {'context': context})

@login_required
def delete(request, task_id):
    task = Task.objects.get(id=task_id)
    task.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))

@login_required
def set_completed(request, task_id):
    task = Task.objects.get(id=task_id)
    task.isCompleted = True
    task.save()
    request.META.get('HTTP_REFERER', '/')
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
 
@login_required
def set_incomplete(request, task_id):
    task = Task.objects.get(id=task_id)
    task.isCompleted = False
    task.save()
    print(request.META.get('HTTP_REFERER', '/'))
    return HttpResponseRedirect(request.META.get('HTTP_REFERER', '/'))
