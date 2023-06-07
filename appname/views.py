from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
data = [ ] # TODO: What data structure will we get the dataframes in? Array of array?

def load_dataframe(request):
    global data
    backend_data = [1, 2, 3] # Sample data
    # get the data from backend datastore
    data = backend_data
    return JsonResponse({'result': 'Data loaded', 'data': data})

def perform_analysis(request):
    analyzer_func(data)
    return JsonResponse({'result': 'analysis performed', 'data': data})

def analyzer_func(some_data):
    for i in range(len(some_data)):
        some_data[i] += 1
