from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from app.models import *

def insert_topic(request):
    if request.method=='POST':
        topicname=request.POST['topic']
        t=Topic.objects.get_or_create(topic_name=topicname)[0]
        t.save()
        return HttpResponse('data inserted succcessfully')
    return render(request,'insert_topic.html')

def insert_webpage(request):
    if request.method=='POST':
        topicname=request.POST['topic']
        name=request.POST['name']
        url=request.POST['url']
        t=Topic.objects.get_or_create(topic_name=topicname)[0]
        t.save()
        w=Webpage.objects.get_or_create(topic_name=t,name=name,url=url)[0]
        w.save()
        return HttpResponse('webpage data is inserted')

    return render(request,'insert_webpage.html')

def select_topic(request):
    topics=Topic.objects.all()
    if request.method=='POST':
        topicname=request.POST['topic']

        webpages=Webpage.objects.filter(topic_name=topicname)
        d={'webpages':webpages}
        return render(request,'display_webpage.html',context=d)

    return render(request,'select_topic.html',context={'topics':topics})
def delete_webpage(request):
    if request.method=='POST':
        topicname=request.POST['topic']
        Webpage.objects.filter(topic_name=topicname).delete()
        webpages=Webpage.objects.all()
        d={'webpages':webpages}
        return render(request,'display_webpage.html',context=d)

def multi_selected(request):
    topics=Topic.objects.all()
    if request.method=='POST':
        topic_selected=request.POST.getlist('topic')
        #print(topic_selected)
        webpage=Webpage.objects.none()
        for i in topic_selected:
            webpages=webpage | Webpage.objects.filter(topic_name=i)
            return render(request,'display_webpage.html',context={'webpages':webpages})
    return render(request,'multi_selected.html',context={'topics':topics})

def checkbox(request):
    topics=Topic.objects.all()
    return render(request,'checkbox.html',context={'topics':topics})
