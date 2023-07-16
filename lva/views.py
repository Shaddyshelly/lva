from django.shortcuts import render
from django.http import HttpResponse
from django.http import QueryDict
import smtplib
from email.mime.text import MIMEText
from django.http import HttpResponse, JsonResponse

# Home page
def home(request):
    return render(request, 'index.html')