
def sumar(x,y):
    result = x + y
    print("La suma es : "+str(result))
    print("jajajaja vaya telaaa")


def restar(x,y):
    result = x - y
    print("La resta es : "+str(result))


def multiplicar(x,y):
    result = x * y
    print("La multiplicacion es : "+str(result))


def dividir(x,y):
    result = x / y
    print("La division es: {}".format(result))


x = int(input("Ingresa un numero: "))
y = int(input("Ingresa el segundo numero: "))


sumar(x,y)

restar(x,y)

multiplicar(x,y)

dividir(x,y)
