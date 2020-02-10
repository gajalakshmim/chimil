from django.shortcuts import render
import requests
from django.http import HttpResponse
from .forms import DictionaryForm

# Create your views here.q
# 
response = requests.get('https://api.github.com/emojis')
gitpicture=response.json()

def api(request):
    return render(request,'conapi.html',{'picture':gitpicture['ant']} )
    #return render(request, 'conapi.html')

def getgit(request):
    response = requests.get('https://api.github.com/emojis')
    gitpicture=response.json()
    user = {}
    if 'username' in request.GET:
        username = request.GET['username']
        url = 'https://api.github.com/users/%s' % username
        response = requests.get(url)
        user = response.json()
        return render(request, 'conapi.html', {'user': user, 'picture':gitpicture['baby'],'username':username})

def getword(request):
    search_result = {}
    if 'word' in request.GET:
        form = DictionaryForm(request.GET)
        if form.is_valid():
            search_result = form.search()

    else:
        form = DictionaryForm()
    return render(request, 'conapi.html', {'form': form, 'search_result': search_result, 'picture':gitpicture['ant']})