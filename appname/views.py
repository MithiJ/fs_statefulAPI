from django.shortcuts import render
from django.http import JsonResponse
from .data import Data

# Create your views here
data = Data([])

def load_dataframe(request):
    global data
    backend_data = [1, 2, 3] # Sample data
    # get the data from backend datastore
    data.set_data(backend_data)
    return JsonResponse({'result': 'Data loaded', 'data': data.get_data()})

def perform_analysis(request):
    new_data = analyzer_func(data.get_data()) 
    data.set_data(new_data)
    """
    Here, we can copy over the dataframe in order to not amend it. Likely,
    we should have getters and setters for the data in a separate file that are
    imported in and leave the data as a private variable in that class.
    """
    return JsonResponse({'result': 'analysis performed', 'data': data.get_data()})

def analyzer_func(some_data):
    for i in range(len(some_data)):
        some_data[i] += 1
    return some_data
