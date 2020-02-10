from django.shortcuts import render
from rest_framework import viewsets
from django.core  import serializers
from .models import Employee
from .serializers import EmployeeSerializer
import json
from django_filters.rest_framework import DjangoFilterBackend
from django.http import JsonResponse, HttpResponse

# Creating proapi view to show the api of employee model
def proapi(request):
    #serialize the objects from Model Employee and return a json 
    data = serializers.serialize('json',Employee.objects.all()) 

    #convert the json to python primitive type like dict
    data2=json.loads(data)

    #convert the dict to json with indent 4 to have pretty look of json
    data3=json.dumps(data2, indent=4)
    
    return render(request, 'proapi.html',{'data': data3})
   
# creating view set to display the hyperlinked model thru' router.url
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset =Employee.objects.all().order_by('fname')
    serializer_class = EmployeeSerializer
    
    #using django filter backend to filter the data
    filter_backends =(DjangoFilterBackend,)
    filter_fields =('empid',)