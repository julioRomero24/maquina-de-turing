from django.http import HttpResponse
import datetime
from django.template import Template, Context
from django.template.loader import get_template
from django.shortcuts import render

global reglas
global cinta
cinta=[]
global estadoActual
estadoActual=1
global indiceMaq #aqui se va el indice de las letras evaluadas
indiceMaq=0

def pedirCadena():
    return input("digite una cadena compuestas de a y b:")
def construirMaquina():
    global reglas
    #lee,estado sigiente,poner en cinta,movimiento
     #q1
    regla1=["a","1","a","R"]
    regla2=["b","2","a","R"]
    regla3=[" ","3","B","L"]
    q1=[regla1,regla2,regla3]
    #q2
    regla4=["a","2","a","R"]
    regla5=["b","2","a","R"]
    regla6=[" ","3","B","L"]
    q2=[regla4,regla5,regla6]
    #q3
    regla7=["a","3","a","L"]
    regla8=[" ","4","B","R"]
    q3=[regla7,regla8]

    reglas=[q1,q2,q3]
def ponerEnCinta(letra):

    global cinta
    cinta.pop(indiceMaq)
    cinta.insert(indiceMaq,letra)
    print(letra,'se ha puesto en la cinta')
def moverCinta(movimiento):
    global indiceMaq
    if(movimiento=='R'):
        indiceMaq+=1
    if(movimiento=='L'):
        indiceMaq-=1
def evaluarLetra(letra):
     #lee,estado sigiente,poner en cinta,movimiento
     #q1
    '''q1=[regla1,regla2,regla3]
    regla1=["a","1","a","R"]
    regla2=["b","2","a","R"]
    regla3=[" ","3","B","L"]'''

    #[' ',b,b.' ']
    global estadoActual#1
    for q in reglas[estadoActual-1]:#q1
        if(q[0]==letra):
            estadoSiguiente=int(q[1])
            estadoActual=estadoSiguiente #q3
            letraEnCinta=q[2]#B
            movimiento=q[3]#L
            ponerEnCinta(letraEnCinta)#B
            moverCinta(movimiento)#indiceMaq=1
            break
def ponerVacioF():
    global cinta
    cinta.append(' ')
def ponerVacioI():
    global cinta
    cinta.insert(0,'B')
def devolverCinta():
    global estadoActual
    if(estadoActual==3 and reglas[2][0][2]=='a'):

            estadoActual=4
            ponerVacioI()
def iniciarMaquina():

    ponerVacioF()
    aux=len(cinta)*2
    print(aux)

    for x in cinta:
        evaluarLetra(x)
    devolverCinta()
def VacioFinal():
    global cinta
    cinta.append(' ')
def ponerCadenaEnCinta(cadena):

    global cinta
    #cadena=aba

    for x in cadena:
        #aappend agrega un elemento al final de la lista
        cinta.append(x)
def mostrarEstadoFinal():
    print('estado final=',estadoActual)
def imprimirCinta():

    return(cinta)
def saludo(request):
    cadena = ""
    test=[1]
    construirMaquina()
    cadena = pedirCadena()
    lis= cadena
    numeroCadena= len(cadena)
    ponerCadenaEnCinta(cadena)
    #imprimirCinta()
    iniciarMaquina()
    final=imprimirCinta()
    #mostrarEstadoFinal()
    return render(request, "miplantilla.html", {"Cadena":cadena, "numero":numeroCadena, "tes":test,"cinta":final})
