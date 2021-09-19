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
    digito = int((input("Digite el último número de la placa: ")))
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

""" Calcular el promedio de edades de hombres, mujeres y de todo un grupo
de alumnos."""

hombres = int((input("Digite el número de hombres: ")))
mujeres = int((input("Digite el número de mujeres: ")))
curso = hombres + mujeres
edadh = 0
edadm = 0
for i in range(0, hombres):
    numh = int((input("Digite la edad del hombre número " + str(i)+": ")))
    edadh = edadh + numh
for j in range(0, mujeres):
    num_m = int((input("Digite la edad de la mujer número " + str(j)+": ")))
    edadm = edadm + num_m

print("La edad promedio de los hombres es: ", edadh/hombres)
print("La edad promedio de las mujeres es: ", edadm/mujeres)
print("La edad promedio total del curso es: ", (edadh+edadm)/curso)

# Encontrar el menor valor de un conjunto de n números dados

numeros = int((input("Digite la cantidad de números: ")))
menor = int((input("Digite el número 1: ")))
for i in range(0, numeros-1):
    num = int((input("Digite el número " + str(i+2)+": ")))
    if menor > num:
        menor = num

print("El número menor es: ", menor)

""" Cinco miembros de un club contra la obesidad desean saber cuanto han
bajado o subido de peso desde la última vez que se reunieron. Para esto se
debe realizar un ritual de pesaje en donde cada uno se pesa en diez
básculas distintas para así tener el pormedio mas exacto de su peso.
Si existe diferencia positiva entre este promedio de peso y el peso de la
última vez que se reunieron, significa que subieron de peso. Pero si la
diferencia es negativa, significa que bajaron. Lo que el problema requere es
que por cada persona se imprima un letrero que diga: “SUBIÓ” o “BAJÓ” y la
cantidad de kilos que subió o bajó de peso."""

peso = 0
for i in range(1, 6):
    peso_anterior = int((input("Digite el peso anterior del miembro n°" + str(i)+": ")))
    for j in range(1, 11):
        peso += int((input("Digite el peso de la báscula n°"+ str(j)+ " del miembro " + str(i)+": ")))     
    if(peso_anterior-peso < 0):
        print("El miembro bajó: ", peso_anterior - (peso/10), " kilos.")
    if(peso_anterior-peso > 0):
        print("El miembro subió: ", peso_anterior - (peso/10), " kilos.")

""" En un supermercado una ama de casa pone en su carrito los artículos que
va tomando de los estantes. La señora quiere asegurarse de que el cajero
le cobre bien lo que ella ha comprado, por lo que cada vez que toma un
artóculo anota su precio junto con la cantidad de artículos iguales que ha
tomado y determina cuanto dinero gastará en ese artículo; a esto le suma lo
que irá gastando en los demás artículos, hasta que decide que ya tomó
todo lo que necesitaba. Ayúdele a esta señora a obtener el total de su
compra."""

f = 1
total = 0

while (f == 1):
    f = int((input("Llevara otro artículo? 1 para sí, 2 para no: ")))
    if f == 1:
        precio = int(input('Cuál es el precio del artículo? '))
        cantidad = int(input('Qué cantidad llevará?'))
        total += precio * cantidad
    else:
        f = 0

print("El total de la compra es: ", total)

""" Un teatro otorga descuentos según la edad del cliente, determinar la
cantidad del dinero que el teatro deja de percibir por cada una de las
categorias. Tomar en cuenta que los niños menores de 5 años no pueden
entrar al teatro y que existe un precio único en los asientos. Los descuentos
se hacen tomando en cuenta el siguiente cuadro:
Edad % Descuento
5 – 14 35%
15-19 25%
20 – 45 10%
46 – 65 25%
66 en Adelante 35%"""

precio_boleta = int(input("Digite el precio de la boleta "))
num_personas = int(input("digite el número de personas "))
rango1 = 0
rango2 = 0
rango3 = 0
rango4 = 0
rango5 = 0
for i in range(0, num_personas):
    edad = int(input("Digite la edad de la persona "))
    if edad < 5:
        print("Los niños menores de 5 años no pueden entrar")
        i -= 1
    if edad > 5 and edad <= 14:
        rango1 += 1
    if edad > 15 and edad <= 19:
        rango2 += 1
    if edad > 20 and edad <= 45:
        rango3 += 1
    if edad > 46 and edad <= 65:
        rango4 += 1
    if edad > 66:
        rango5 += 1

print('El dinero perdido por el descuento en la categoría 5-14 es: ',
      rango1*precio_boleta*0.35)
print('El dinero perdido por el descuento en la categoría 15-20 es: ',
      rango2*precio_boleta*0.25)
print('El dinero perdido por el descuento en la categoría 20-45 es: ',
      rango3*precio_boleta*0.10)
print('El dinero perdido por el descuento en la categoría 46-65 es: ',
      rango4*precio_boleta*0.25)
print('El dinero perdido por el descuento en la categoría 66-adelante es: ',
      rango5*precio_boleta*0.35)

""" Kia Autos premia anualmente a sus mejores vendedores de acuerdo a la
siguiente tabla:
Valor vendido Comisión
Menor o igual que 20 Millones - 10%
Mayor de 20 Millones y menor de 40 Millones - 15%
Mayor o igual de 40 Millones y menor de 80 Millones - 20%
Mayor o igual de 80 millones y menor de 160 Millones - 25%
De 160 Millones en adelante - 30%"""

for i in range(0, 100):
        venta = int(input("Digite cuanto vendió el empleado número "+ str(i)+" en millones de pesos "))
        if(venta < 20):
            print("La comisión del empleado " + str(i)+"fue de ", venta*0.1)
        if(venta < 40 and venta > 20):
            print("La comisión del empleado " + str(i)+"fue de ", venta*0.15)
        if(venta < 80 and venta >= 40):
            print("La comisión del empleado " + str(i)+"fue de ", venta*0.20)
        if(venta < 160 and venta >= 80):
            print("La comisión del empleado " + str(i)+"fue de ", venta*0.25)
        if(venta > 160):
            print("La comisión del empleado " + str(i)+"fue de ", venta*0.30)
