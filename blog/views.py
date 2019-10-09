from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home (request):
    testo="hello world"
    nome_HTML="BASE_Home.html"

    return render(request, nome_HTML ,)

def contattami(request):
    testo="Sezione contattami"
    return HttpResponse(testo)
