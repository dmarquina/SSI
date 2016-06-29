from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.shortcuts import render,redirect
from datetime import datetime, timedelta
from .models import Task
from userprofiles.models import Userprofile
from components.models import Component
from progress.models import Progress

def createTask(request):
	if request.method == 'POST':
		name = request.POST.get('name', None)
		actions = request.POST.get('actions', None)
		pk_responsable = request.POST.get('responsable')
		pk_component = request.POST.get('component')

		component = Component.objects.get(pk=pk_component)
		responsable = Userprofile.objects.get(pk=pk_responsable)

		Task.objects.create(name=name,actions=actions,
							responsable=responsable,component=component)
		return redirect('/')

	components = Component.objects.all()
	responsables = Userprofile.objects.all()
	context = {'components' : components,
				'responsables' : responsables}
	return render(request, 'tasks/create_task.html', context)
    	
def showAllTasks(request):
	taskdata=[]
	tasks = Task.objects.order_by('component')
	today = datetime.now()
	yesterday = today - timedelta(days=1)
	beforeyesterday = yesterday - timedelta(days=1)
	for t in tasks:
		todayvalue = progressValue(t,today)
		yesterdayvalue = progressValue(t,yesterday)
		beforeyesterdayvalue = progressValue(t,beforeyesterday)
		data={'id':t.id, 
		'component':t.component,
		'name':t.name,
		'actions':t.actions,
		'responsable':t.responsable,
		'todayvalue':todayvalue,
		'yesterdayvalue':yesterdayvalue,
		'beforeyesterdayvalue':beforeyesterdayvalue,
		}
		taskdata.append(data) 
	context={'taskdata' : taskdata}
	context['todaydate']=today
	context['yesterdaydate']=yesterday
	context['beforeyesterdaydate']=beforeyesterday
	return render(request, 'tasks/show_all_tasks.html', context) 

def progressValue(task,daydate):
	totalValue=0
	try:
		progress = Progress.objects.get(task=task,date=daydate)
		totalValue = progress.value
	except Progress.DoesNotExist:
		totalValue = 0
	return totalValue
	