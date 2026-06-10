from django.http import HttpResponse
from django.shortcuts import render
import datetime

def trial(request):
    context = {
        "user_name": "Master Dhruv",
        "current_time": datetime.datetime.now(),
        "topics": ["Urls", "Views", "Templates","Dynamic Data"]
    }
    return render(request, 'index.html', context)

def new_fun(request, name): # Added 'name' as a parameter
    context = {
        "user_name": name,  # Now it uses the variable from the URL!
    }
    return render(request, 'new.html', context)

def add_view(request, num1, num2):
    # Perform the math in Python
    result = num1 + num2
    
    context = {
        "n1": num1,
        "n2": num2,
        "sum": result,
    }
    return render(request, 'add.html', context)