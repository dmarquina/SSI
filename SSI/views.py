from django.shortcuts import render
from django.shortcuts import redirect
from datetime import datetime, timedelta
from tasks.models import Task
from components.models import Component
from progress.models import Progress

def start(request):
	if request.user.is_authenticated():
		if request.user.is_admin:
			componentdata=[]
			components = Component.objects.all()
			today = datetime.now()
			yesterday = today - timedelta(days=1)
			beforeyesterday = yesterday - timedelta(days=1)
			for c in components:
				taskquantity=Task.objects.filter(component=c).count()
				todayvalue = totalValue(c,today)
				yesterdayvalue = totalValue(c,yesterday)
				beforeyesterdayvalue = totalValue(c,beforeyesterday)
				data={'id':c.id, 
				'name':c.name,
				'taskquantity':taskquantity,
				'todayvalue':todayvalue,
				'yesterdayvalue':yesterdayvalue,
				'beforeyesterdayvalue':beforeyesterdayvalue,
				}
				componentdata.append(data) 
			context={'componentdata' : componentdata}
			context['todaydate']=today
			context['yesterdaydate']=yesterday
			context['beforeyesterdaydate']=beforeyesterday
			return render(request, 'index.html', context) 
		else:
			tasks = Task.objects.filter(responsable = request.user)
			taskdata=[]
			for t in tasks:
				try:
					progress=Progress.objects.get(task=t,date=datetime.now())
					progressvalue=progress.value
				except Progress.DoesNotExist:
					progressvalue=0
				data={'id':t.id,
						'name':t.name,
						'component':t.component.name,
						'progressvalue':progressvalue,
				}
				taskdata.append(data)
			context = {'taskdata' : taskdata,}
			return render(request, 'progress/set_progress.html', context) 
	else:    
		return render(request, 'sign/signin.html', {}) 

def totalValue(component,daydate):
	tasks = Task.objects.filter(component=component)
	totalValue=0
	cant=0
	for t in tasks:
		try:
			progress = Progress.objects.get(task=t,date=daydate)
			totalValue += progress.value
		except Progress.DoesNotExist:
			totalValue += 0
		cant+=1
	
	return round(totalValue/cant,2)
	
