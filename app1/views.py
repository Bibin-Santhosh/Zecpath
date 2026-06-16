from django.shortcuts import render
from django.http import HttpResponse
from services.app1_service import App1Service

# Create your views here.
# app1/views.py



# app1/views.py




def home(request):
    message = App1Service.get_welcome_message()
    return HttpResponse(message)