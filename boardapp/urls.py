from django.urls import path
from .views import signupfanc, loginfanc

urlpatterns = [
    path('signup/', signupfanc),
    path('login/', loginfanc),
]
