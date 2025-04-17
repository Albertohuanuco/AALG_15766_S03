#Function Suma
def mutiply(num1: int, num2 : int)->int:
    return num1*num2
#Calling the function
print(mutiply(4,5))

#Funcion resta
def resta(a,b):
     return a-b
def multiplicacion (a: int, b: int)->int:
    return a*b

def saludo(a:str)->str:
    x="hola "+a
    return x

def despedida(a:str)->None:
    x="chau "+a
    print(x)
print(resta(5,2))
print(multiplicacion(5,2))
print(saludo("carlos"))
despedida("carlos")