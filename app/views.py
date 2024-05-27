from django.shortcuts import render

# Create your views here.
from app.forms import *
from app.models import *
from django.http import HttpResponse
def insert_topic(request):
    ETFO=TopicForm()
    d={'ETFO':ETFO}
    if request.method=='POST':
        TFDO=TopicForm(request.POST)
        if TFDO.is_valid():
            tn=TFDO.cleaned_data['topic_name']
            TO=Topic.objects.get_or_create(topic_name=tn)[0]
            TO.save()
            return HttpResponse('Data is submitted')
        else:
            return HttpResponse('Invalid data')

    return render(request,'insert_topic.html',d)

def insert_webpage(request):
    EWFO=WebpageForm()
    d={'EWFO':EWFO}
    if request.method=='POST':
        WFDO=WebpageForm(request.POST)
        if WFDO.is_valid():
            tn=WFDO.cleaned_data['topic_name']
            na=WFDO.cleaned_data['name']
            ur=WFDO.cleaned_data['url']
            em=WFDO.cleaned_data['email']
            #WO=Webpage.objects.get_or_create(topic_name=tn,name=na,url=ur,email=em)[0]
            #WO.save()
            return HttpResponse('Data is submitted')
        else:
            return HttpResponse('Data is invalid')
    return render(request,'insert_webpage.html',d)

def insert_accessrecord(request):
    EAFO=AccessRecordForm()
    d={'EAFO':EAFO}
    if request.method=='POST':
        AFDO=AccessRecordForm(request.POST)
        if AFDO.is_valid():
            na=AFDO.cleaned_data['name']
            da=AFDO.cleaned_data['date']
            au=AFDO.cleaned_data['author']
            AO=AccessRecord.objects.get_or_create(name=na,date=da,author=au)[0]
            AO.save()
            return HttpResponse('Data is submitted')
        else:
            return HttpResponse('Data is invalid')
    return render(request,'insert_accessrecord.html',d)