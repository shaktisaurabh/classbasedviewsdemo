from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
# Create your views here.
class greetingview(View):
    greetingmessage="<b>First CBV says hello OK:</b>"
    def get(self,request):
        return HttpResponse(self.greetingmessage)  
