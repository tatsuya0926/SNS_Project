from django.http.response import HttpResponse
from django.shortcuts import render

def signupfanc(request):
  return render(request, 'signup.html', {})
