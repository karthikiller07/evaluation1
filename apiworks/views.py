from django.shortcuts import render
from django.http import JsonResponse

# Create your views here.
def display(request):
    data={
        "Experience": "2 years",
        "Role": "Developer",
        "Company": "Xyz",
        "Name":"karthik"



    }
    return JsonResponse(data)

def health(request):
    data={
        "Heath":"Good",
        "Test":"evaluation1",
        "Date":"16-09-2021"
    }
    return JsonResponse(data)