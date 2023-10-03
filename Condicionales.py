# Condicionales
a = 200
b = 33
if b > a:
 print("b es mayor que a")
elif a == b:
 print("a y b son iguales")
else:
 print("a es mayor que b")
# Ciclo while - mientras
quiereVolver = True
vecesRegresaron = 0
while vecesRegresaron < 3:
 vecesRegresaron += 1
 print("Han Vuelto " + str(vecesRegresaron) + "Veces")
# Break
i = 8
while i < 6:
 print(i)
 if i == 3:
    break
 i += 1
else:
 print("error")
print("Continue")
# Continue
i = 0
while i < 6:
 i += 1
 if i == 3:
    continue
    print(i)