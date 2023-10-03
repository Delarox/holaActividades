#   Operadores de Asignación
x = 30
x += 32
x -= 2
x *= 2
x /= 2
print(x)

#   Operadores Logicos de Comparacion
a = 3
b = 2
# Igual
print(a == b)
# Diferente
print(a != b)
# Mayor
print(a > b)
# Menor
print(a < b)
# Mayor igual
print(a >= b)
# Menor igual
print(a <= b)
# Operadores Logicos
promedio = 100
asistencias = True
aprobado = (promedio > 70) and asistencias
# and, or, not
print(aprobado)

#   Operadores de identidad
j = "HOLA"
k = "HOLA "
print(j is k.replace(" ", ""))
print(j is not k)

#   Operadores de pertenencia
print("A" in "HOLA")
print("A" not in "HOLA")
# Listas
frutas = ["Manzana", "Banana", "Mango"]
frutas2 = ["🍎", "🍌", "🥭"]
print(frutas)
print(frutas2)
lista = [1, 2, 3, 4, 5, 6]
logico = [True, False, True]


lista1 = ["abc", 34, True, 'a', "🍑"]
print(type(lista))
print(lista1)

#   list, Tuple, Set, Dictionary
"""
List: es una colección la cual esta ordenada
y modificable, la cual permite duplicados.
Tuple: Es una coleccion la cual esta ordenada y
no es modificable. Permite duplicados
Set: Es una coleccion la cual NO❌ esta ordenada y
no es modificable ni indexada. No❌ permite Duplicados
Dictionary: Es una coleccion la cual esta ordenada
es modificable. No Permite duplicados.
"""
#Lista
lista1 = ["🐥", "🙊", "🐷", "🐷", "🐷"]
lista1.insert(3, "🐶")
lista1[2] = "🐯"
print(lista1)
#Tupla
tupla1 = ("🐥", "🙊", "🐷", "🐷")
print(tupla1)
# Set
set1 = {"🐥", "🙊", "🐷"}
set1.add("🐨")
set1.add("🐙")
print(set1)
# Diccionario
diccionario1 = {
 "pollo": "🐥",
 "monito": "🙊",
 "cerdito": "🐷"

}
diccionario1["koala"] = "🐨"
diccionario1["tigre"] = "🐯"
print(diccionario1["monito"])
print(diccionario1)
"""
#0 CREAR UNA LISTA : 1, 2, 5, 3, 2, 3, 3, 6, 10, 8, 9
#1.CONVERTIR LA LISTA EN UN SET PARA ELIMINAR DUPLICADOS
#2. CALCULAR LA SUMA DE LOS NUMEROS USANDO UNA LISTA
#3.CALCULAR LA SUMA DE LOS NUMEROS USANDO UN SET
#4.CREAR UN DICCIONARIO PARA ALMACENAR LAS ESTADISTICAS
 NUMEROS UNICOS, SUMA TOTAL LISTA, SUMA TOTAL SET
 MAXIMO VALOR, MINIMO VALOR
#5. IMPRIMIR LAS ESTADISTICAS"""

numberList = [1, 2, 5, 3, 2, 3, 3, 6, 10, 8, 9]
uniqueList = set (numberList)
totalSumList = sum(numberList)
totalSumUnique = sum(uniqueList)
maxNumber = max(numberList)
minNumber = min(numberList)
stats = {
"totalSumList": totalSumList,
"totalSumSet": totalSumUnique,
"max": maxNumber,
"min": minNumber,
}
print(stats)