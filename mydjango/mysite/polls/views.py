from cgitb import html
from this import d
from polls.forms import *
from django.shortcuts import render
# from django.http import HttpResponse
from django.http import HttpResponseRedirect
from polls.models import Degree
from templates import *

from .forms import DegreeForm
import json

from .forms import DegreeForm    
# Create your views here.
count = 0
srchname =""
def index2(request) :
    global count
    count += 1
    degree_values = Degree.objects.all()
    my_dict = { 'inject_var' : count,'degree_rows':degree_values}
    evenOrOdd = count % 2
    my_dict['evenOrOdd'] = evenOrOdd
    fruitList = ['Mango', 'Banana',  'Apple','Gauva']
    my_dict['fruits'] = fruitList
    return render(request,'index2.html',context=my_dict)

def index1(request) :
    return render(request,'help.html')



               # Relative import from our forms.py using .forms



def get_degree(request):
  print("Hello")
  if request.method == 'POST':                  # if this is a POST request we need to process the form data
    form = DegreeForm(request.POST, request.FILES)   # create a form instance and populate it with data from the request:
    if form.is_valid():                         # check whether it's valid:
      title = form.cleaned_data['title']        # process the data in form.cleaned_data as required
      branch = form.cleaned_data['branch']
      print(title, branch)

      d = Degree(title=title, branch=branch)    # write to the database
      d.save()

      # Retrieve the json file and process here
      f = request.FILES['file']          # open the json files - get file handle
      data = json.load(f)
      for deg in data['degree']:         # iterate through the degree list
        t = deg['title']                 # get the title of each item in the list
        b = deg['branch']                # get the branch of each item in the list
        dl = Degree(title=t, branch=b)   # Create a Degree model instance
        dl.save()                        # save

      return HttpResponseRedirect('/degree/')   # redirect to a new URL:
  else:                                   # if a GET (or any other method) we'll create a blank form
    form = DegreeForm()
    return render(request, 'degree.html', {'form': form })

# Search by Name
def srchbyname(request):
    print("request",request)
    print("name in text")
    return HttpResponseRedirect('/degree/')