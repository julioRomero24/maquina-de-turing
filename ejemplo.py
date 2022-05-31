
from ast import Str
from tokenize import String


class prueba:
    regla1=["a","1","a","R"]
    regla2=["b","2","a","R"]
    regla3=["B","3","B","L"]
    q1=[regla1,regla2,regla3]
    #q2
    regla4=["a","2","a","R"]
    regla5=["b","2","a","R"]
    regla6=["B","3","B","L"]
    q2=[regla4,regla5,regla6]
    #q3
    regla7=["a","3","a","L"]
    regla8=["B","4","B","R"]
    q3=[regla7,regla8]

    reglas=[q1,q2,q3]  
    cadena="perra"
    cadena2="2"
    
    for xx in range(len(cadena)-2,-1,-1):
        print(cadena[xx])

    #print(reglas[0][0][0])