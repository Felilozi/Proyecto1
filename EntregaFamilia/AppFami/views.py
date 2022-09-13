
from re import template
from django.shortcuts import render
from django.http import HttpResponse
from AppFami.models import Familia
from django.template import Template,Context,loader



def hermano(request):
    nombreH = ("Franci")
    yearh = 32
    fechah= ("1990-02-12")
    vinculoh= "Hermano"
    fami = Familia(nombre = nombreH ,year = yearh,fecha=fechah,vinculo= vinculoh )
    diccionario = {"nombre":nombreH,"año":yearh,"fecha":fechah,"vinculo":vinculoh}  
    plantilla =loader.get_template('AppFami/hermano.html') 
    documento = plantilla.render(diccionario)  
    fami.save()   
    return HttpResponse(documento)
    
def hermano1(request):    
    nombreH1 = ("Socrates")
    yearhH1 = (39)
    fechaH1 = ("1983-04-28")
    vinculoH1 =("Hermano")
    fami1 = Familia(nombre =nombreH1 ,year =yearhH1  ,fecha=fechaH1,vinculo = vinculoH1)
    diccionarioH = {"nombre":nombreH1,"año":yearhH1,"fecha":fechaH1,"vinculo":vinculoH1 }
    plantilla =loader.get_template('AppFami/hermano1.html') 
    documento = plantilla.render(diccionarioH)  
    fami1.save()   
    return HttpResponse(documento)

def madre(request): 
    nombreM = ("Neria")
    yearM = 64
    fechaM = ("1957-09-10")
    vinculoM= ("Madre")  
    fami2 = Familia(nombre = nombreM,year = yearM  ,fecha= fechaM ,vinculo =vinculoM )
    diccionarioM = {"nombre":nombreM,"año":yearM,"fecha":fechaM,"vinculo":vinculoM }
    plantilla =loader.get_template('AppFami/madre.html') 
    documento = plantilla.render(diccionarioM)  
    fami2.save()   
    return HttpResponse(documento)

def padre(request):    
    nombreP = ("Milciades")
    yearP = 70
    fechaP = ("1952-09-28")
    vinculoP =("Padre")
    fami3 = Familia(nombre =nombreP,year = yearP,fecha= fechaP,vinculo =vinculoP )
    plantilla =loader.get_template('AppFami/padre.html') 
    diccionarioP = {"nombre":nombreP,"año":yearP,"fecha":fechaP,"vinculo": vinculoP }
    documento = plantilla.render(diccionarioP)  
    fami3.save()   
    return HttpResponse(documento)
    


    