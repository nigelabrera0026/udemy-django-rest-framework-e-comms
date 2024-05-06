from django.shortcuts import render
from django.http import HttpResponse

def home(request):
  # Rendering the html template
  return render(request, "index.html")