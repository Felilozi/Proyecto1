from django.http import HttpResponse
from django.template import Template,Context,loader
def inicia(request):

    mHML =  open("plantilla_1.html")
    plantilla =loader.get_template("plantilla_1.html")
    documento = plantilla.render()
    return HttpResponse()


