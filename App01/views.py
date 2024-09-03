from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def index(request):
    html="""
    <h1> texto de prueba para app01 </h1>
    <h2> TEST TEXT </h2>
    """

    return HttpResponse(html)

def pagina1(request):
    html="""
    <h1 style="color:blue">texto en la pagina, texto azul</h1>
    <h2 style="color:red"> TEST TEXT </h2>
    """
    return HttpResponse(html) 