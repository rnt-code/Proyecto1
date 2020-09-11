from django.http import HttpResponse

def saludo(request): #es nuestra primera vista
    return HttpResponse("Hola alumnos esta es nuestra primer página con Django")