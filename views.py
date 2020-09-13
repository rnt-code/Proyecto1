from django.http import HttpResponse
import datetime
from django.template import Template, Context 

#Construimos una clase persona para hacer lo mismo que lo anterior
#pero esta vez con objetos.
class Persona(object) :
    #Constructor
    def __init__(self, nombre, apellido):
        self.nombre = nombre
        self.apellido = apellido


def saludo(request): #es nuestra primera vista
    
    persona1 = Persona("Ramón", "Taboada")
    temasDelCurso = ["Plantillas", "Modelos", "Formularios", "Listas", "Despliegue"]
    #nombre = "Juan"
    #apellido = "Díaz"
    ahora=datetime.datetime.now()

    doc_externo = open("C:/Users/ingra/OneDrive/00 UTN/2020/Curso_Django/Proyecto1/Proyecto1/plantillas/miPlantilla.html")
    plt=Template(doc_externo.read())
    doc_externo.close()

    #en el contexto estoy trabajando con bibliotecas de python
    ctx = Context({"nombre_persona":persona1.nombre, "apellido_persona":persona1.apellido, "momento_actual":ahora, "temas":temasDelCurso})
    #ctx = Context({"nombre_persona":persona1.nombre, "apellido_persona":persona1.apellido, "momento_actual":ahora, "temas":["Plantillas", "Modelos", "Formularios", "Listas", "Despliegue"]})
    #ctx = Context({"nombre_persona":persona1.nombre, "apellido_persona":persona1.apellido, "momento_actual":ahora})
    #ctx = Context({"nombre_persona":"Juan", "apellido_persona":"Díaz"})

    documento = plt.render(ctx)

    return HttpResponse(documento)

def despedida(request):
    return HttpResponse('Hasta luego alumnos de Django')

def damefecha(request):
    
    fecha_actual=datetime.datetime.now()
    
    documento="""
    <html>
        <body>
            <h2>
                Fecha y hora actuales %s
            </h2>
        </body>
    </html>    
    """ %fecha_actual
    # %s es un marcador de posición
    return HttpResponse(documento)

def calculaEdad(request, edadActual, anioFuturo):
    
    #edadActual = 52
    periodo = anioFuturo - 2020
    edadFutura = edadActual + periodo
    documento="""
    <html>
        <body>
            <h2>
                En el año %s tendrás %s años
            </h2>
        </body>
    </html>
    """ %(anioFuturo, edadFutura)
    # %s es un marcador de posición
    return HttpResponse(documento)
