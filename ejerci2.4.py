#4) Realiza una función llamada intermedio() que a partir de dos números, devuelva su punto intermedio:

#Nota: El número intermedio de dos números corresponde a la suma de los dos números dividida entre 2

#Comprueba el punto intermedio entre -12 y 24

num1 = int(input("numero1"))
num2 = int(input("numero2"))

def intermedio(num1, num2):
    return (num1 + num2) / 2

print("intermedio(-12, 24)")