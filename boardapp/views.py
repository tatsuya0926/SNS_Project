from django.shortcuts import render
from django.contrib.auth.models import User

def signupfanc(request):
  object_list = User.objects.all()
  print(object_list)
  if request.method == "POST":
    print()
  else:
    print()
  return render(request, 'signup.html', {})
