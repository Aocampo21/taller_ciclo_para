# -*- coding: utf-8 -*-
import random
"""
Created on Sun Sep 19 14:01:36 2021

@author: amand
"""
""" El departamento de Seguridad de Transito de Barranquilla, desea saber de
los n autos que entrar a la ciudad, cuantos entran con calcomanía de cada
color. Conociendo el último digito de la placa de cada automóvil se puede
determinar el color de la calcomanía utilizando la siguiente relación:
DIGITO COLOR
1 o 2 Amarilla
3 o 4 Rosa
5 o 6 Roja
7 u 8 Verde
9 o 0 Azul """

auto = random.randrange(15)
amarilla = 0
rosa = 0
roja = 0
verde = 0
azul = 0
for i in range(0, auto):
    digito = int((input("Digite el último número de la placa")))
    if digito == 1 or digito == 2:
        amarilla = amarilla+1
    if digito == 3 or digito == 4:
        rosa = rosa+1
    if digito == 5 or digito == 6:
        roja = roja+1
    if digito == 7 or digito == 8:
        verde = verde+1
    if digito == 9 or digito == 0:
        azul += azul+1

print("El número de calcomanías Amarillas es ", amarilla)
print("El número de calcomanías Rosas es: ", rosa)
print("El número de calcomanías Rojas es: ", roja)
print("El número de calcomanías Verdes es: ", verde)
print("El número de calcomanías Azul es: ", azul)
