""""Realiza un programa que lea dos números por teclado y permita elegir entre 3 opciones en un menú:
    Mostrar una suma de los dos números
    Mostrar una resta de los dos números (el primero menos el segundo)
    Mostrar una multiplicación de los dos números
    En caso de no introducir una opción válida, el programa informará de que no es correcta."""
    
nu1 = float(input("Ingrese un número: ") )
nu2 = float(input("Ingrese otro número: ") )
opcion = 0
           
print("¿Qué quieres hacer? \n1) Sumar los dos\n2) Restar los dos\n3) Multiplicar los dos")
opcion = int(input("Introduce un número: ") )     

if opcion == 1:
    print("suma de",nu1,"+",nu2,"es",nu1+nu2)
elif opcion == 2:
    print("resta de",nu1,"-",nu2,"es",nu1-nu2)
elif opcion == 3:
    print("producto de",nu1,"*",nu2,"es",nu1*nu2)
else:
    print("incorrecta")

