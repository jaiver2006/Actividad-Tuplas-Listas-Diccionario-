#Crea una lista con las notas de 5 estudiantes. Agrega una nota más al final, y elimina la más baja.
notas = [85, 90, 78, 92, 88]
notas.append(95)  # Agrega una nota más al final
notas.remove(min(notas))  # Elimina la nota más baja
print("Notas actualizadas:", notas)



#Dada la lista asistencias = [1, 0, 1, 1, 0, 1, 1] (1 = asistió, 0 = faltó), cuenta cuántas veces asistió el estudiante usando un bucle.
asistencias = [1, 0, 1, 1, 0, 1, 1]
total_asistencias = 0
for asistencia in asistencias:
    if asistencia == 1:
        total_asistencias += 1
print("El estudiante asistió", total_asistencias, "veces.")



#Crea una lista de nombres de estudiantes. Ordénala alfabéticamente con .sort() e imprime el resultado.
nombres = ["Ana", "Carlos", "Beatriz", "David", "Elena"]
nombres.sort()
print("Nombres ordenados:", nombres)



#Dada la lista precios = [15000, 8000, 22000, 5000], calcula el total y el promedio sin usar sum().
precios = [15000, 8000, 22000, 5000]
total = 0
for precio in precios:
    total += precio
promedio = total / len(precios)
print("Total:", total)
print("Promedio:", promedio)



#Dada la lista edades = [15, 22, 17, 30, 16, 25], crea dos listas nuevas: una con los mayores de edad y otra con los menores de edad, recorriendo la lista original con un bucle.
edades = [15, 22, 17, 30, 16, 25]
mayores_edad = []
menores_edad = []
for edad in edades:
    if edad >= 18:
        mayores_edad.append(edad)
    else:
        menores_edad.append(edad)
print("Mayores de edad:", mayores_edad)
print("Menores de edad:", menores_edad)
