def suma(a,b):
    return a + b

def pedirNumeroEnteroValidado(messages = "Ingrese un numero Enter0"):
    num = input(messages)
    while not validarEntero(num):
        print("Error valor ingresado incompatible")
        num = input(messages)
    return int(num)

def validarEntero(num):
    isValid = False
    try:
        int(num)
        isValid = True
    except ValueError:
        isValid = False
    return isValid

def pedirNumeroDecimalValidado(messages = "Ingrese un numero Enter0"):
    num = input(messages)
    while not validarDecimal(num):
        print("Error valor ingresado incompatible")
        num = input(messages)
    return float(num)

def validarDecimal(num):
    isValid = False
    try:
        float(num)
        isValid = True
    except ValueError:
        isValid = False
    return isValid