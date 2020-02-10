from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def calc(request):
    return render(request,'index1.html')

def compute(request):
    val1=int(request.POST["num1"]) #Get the number1
    val2=int(request.POST["num2"]) #Get the number2
    calculate=request.POST["operation"] #Get the operation
    if calculate == "Addition":
     res=val1+val2
    elif calculate == "Subtraction":
     res=val1-val2
    elif calculate == "Multiplication":
     res = val1 * val2
    else: 
     res= val1 / val2
        
    return render(request,'index1.html',{'result':res})

