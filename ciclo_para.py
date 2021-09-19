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

""" Un Zoólogo pretende determinar el porcentaje de animales que hay en las
siguiente categorias de edades: 0 a 1 año, de mas de 1 año y menos de 3 y
de 3 o mas años. El zoológico todavía no está seguro del animal que va
estudiar. Si se decide por elefantes solo tomará una muestra de 20 de ellos;
si se decide por jirafas, tomara 15 de muestras y si son chompancés tomará
40. """

animales = 0
edad1 = 0
edad2 = 0
edad3 = 0
animal = str(input("Digite el animal a estudiar "))
if (animal == "elefante"):
    animales = 20
if (animal == "jirafa"):
    animales = 15
if (animal == "chimpancés"):
    animales = 40

for i in range(0, animales):
    dig = int((input("Digite la edad del animal ")))
    if dig <= 1:
        edad1 = edad1+1
    if dig == 2:
        edad2 = edad2+1
    if dig >= 3:
        edad3 = edad3+1

print("El porcentaje de anímales entre 0 y 1 años es: ", edad1/animales * 100)
print("El porcentaje de anímales de 2  años es: ", edad2/animales * 100)
print("El porcentaje de anímales de más de 3 años es: ", edad3/animales * 100)

""" Una empresa se requiere calcular el salario semanal de cada uno de los n
obreros que laboran en ella. El salario se obtiene de la siguiente forma:
a. Si el obrero trabaja 40 horas o menos se le paga $20 por hora
b. Si trabaja mas de 40 horas se le paga $20 por cada una de
las primeras 40 horas y $25 por cada hora extra. """

obrero = int((input("Ingrese el número de trabajadores: ")))
for i in range(0, obrero):
    hora = int((input("Ingrese las horas trabajadas: ")))
    if hora <= 40:
        print("El salario de este obrero es: ", hora*20)
    if hora > 40:
        print("El salario de este obrero es: ", 800+((hora-40)*25))

