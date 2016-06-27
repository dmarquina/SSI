from django.shortcuts import render,redirect
from tasks.models import Task
from .models import Progress
from datetime import datetime
from django.contrib import messages

def showProgress(request):
	tasks = Task.objects.filter(responsable = request.user)
	taskdata=[]
	for t in tasks:
		try:
			progress=Progress.objects.get(task=t,date=datetime.now(),)
			print(progress)
			progressvalue=progress.value
		except Progress.DoesNotExist:
			progressvalue=0
		data={'id':t.id,
				'name':t.name,
				'component':t.component.name,
				'progressvalue':progressvalue,
		}
		taskdata.append(data)
	today = datetime.now()		
	context = {'taskdata' : taskdata,}
	context['todaydate']=today
	return render(request, 'progress/set_progress.html', context) 

def setProgress(request):
	if request.method == 'POST':
		task_progress_list={}
		cant_task = request.POST.get('cant_task')
		i=0
		while i< int(cant_task):
			task_id= int(request.POST.get('task_progress_list['+str(i)+'][task_id]'))
			progressvalue = int(request.POST.get('task_progress_list['+str(i)+'][progress]'))
			task = Task.objects.get(id=task_id)
			try:
				progress = Progress.objects.get(task=task,date=datetime.now(),)
				progress.value=progressvalue
				progress.save()
			except Progress.DoesNotExist:
				Progress.objects.create(task=task,
									value=progressvalue,
									date=datetime.now(),)
			i+=1
			messages.success(request,"Progreso Guardado")
	return render(request, 'progress/set_progress.html', {}) 

