from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def pagina1(request):
    html="""
    <h1>Soy la página 1</h1>
    """
    return HttpResponse(html)

def pagina2(request):
    html="""
    <h1>Soy la página 2</h1>
    """
    return HttpResponse(html)