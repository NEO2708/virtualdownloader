from django.shortcuts import render
from django.http import HttpResponse
from django.template import Context, loader

# from django.shortcuts import render_to_response

def homepage (request):
    return render(request, 'index.html')