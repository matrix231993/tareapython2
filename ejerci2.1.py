#1) Realiza una función llamada area_rectangulo() que devuelva el área del rectangulo a partir de una base y una altura. Calcula el área de un rectángulo de 15 de base y 10 de altura.

#Nota: El área de un rectángulo se obtiene al multiplicar la base por la altura.

base = int(input("base"))
altura = int(input("altura"))

def area_rectan(base, altura):
    return base * altura