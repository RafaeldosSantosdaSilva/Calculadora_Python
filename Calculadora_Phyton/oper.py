def Soma(a,b):

    return str(float(a) + float(b))

def Sub(a,b):

    return str(float(a) - float(b))

def Mult(a,b):

    return str(float(a) * float(b))


def Div(a,b):

 if(float (a) == 0 or float(b) == 0):
    return "Não foi possível dividir um número por 0"

 else:
    return str(float(a) / float(b))
