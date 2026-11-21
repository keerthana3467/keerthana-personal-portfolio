from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import Http404
from .forms import ContactForm
PROJECTS={
 'fitness-tracking-system':{'title':'Fitness Tracking System','description':'A web-based application that helps users track workouts, monitor daily activities, set fitness goals, and visualize progress to support a healthy lifestyle.','features':['Track workouts and daily activity','Set personal fitness goals','Visualize progress over time'],'technologies':['HTML','CSS','JavaScript','Bootstrap','Django','SQLite3']},
 'blog-platform':{'title':'Blog Platform','description':'A dynamic blog platform that allows users to create, publish, and manage blog posts through a structured web application.','features':['Create and publish blog posts','Manage published content','Browse a structured blog experience'],'technologies':['HTML','CSS','JavaScript','Bootstrap','React.js','Django','SQLite3']}}
def home(request):
 form=ContactForm(request.POST or None)
 if request.method=='POST':
  if form.is_valid():
   form.save(); messages.success(request,'Thank you! Your message has been saved successfully.'); return redirect('home')
  messages.error(request,'Please check the form and correct the highlighted fields.')
 return render(request,'portfolio/index.html',{'form':form,'projects':PROJECTS,'linkedin':'https://www.linkedin.com/in/keerthana-jagannathan-72a678361/'})
def project_detail(request,slug):
 project=PROJECTS.get(slug)
 if not project: raise Http404('Project not found')
 return render(request,'portfolio/project_detail.html',{'project':project,'slug':slug})
