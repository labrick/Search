# Create your views here.
from django.shortcuts import render_to_response
from django.db.models import Q
from smodel.models import Person

def index(request):
    first_name = request.GET.get('first_name','')
    last_name = request.GET.get('last_name','')


    if first_name and last_name:
        qset = (
            Q(first_name__icontains=first_name) & 
            Q(last_name__icontains=last_name)
        )
        results = Person.objects.filter(qset).distinct()
        if results:
            #already have
            return render_to_response('index.html',{'results':results[0]})
        else:
            #register
            p = Person(first_name=first_name,last_name=last_name)
            p.save()
            return render_to_response('index.html',{'first_name':first_name,'last_name':last_name,})
    else:
        #not null
        if not first_name:
            error = 'first_name'
        if not last_name:
            error = 'last_name'
        return render_to_response('index.html',{'error':error})
