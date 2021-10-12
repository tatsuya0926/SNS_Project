from django.urls import path
from .views import signupfanc

urlpatterns = [
    path('signup/', signupfanc),
]
