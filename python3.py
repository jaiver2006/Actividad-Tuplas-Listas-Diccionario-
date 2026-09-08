#Crea un diccionario que represente un producto de una tienda: nombre, precio, cantidad_en_stock. Actualiza el stock después de una venta.
producto = {
    "nombre": "Laptop",
    "precio": 15000,
    "cantidad_en_stock": 10
}
# Simular una venta (reducir el stock en 1)
producto["cantidad_en_stock"] -= 1
print("Stock actualizado:", producto["cantidad_en_stock"])



#Crea un diccionario con las notas de un estudiante por materia ({"Matemáticas": 8.5, "Inglés": 7.0, "Programación": 9.2}) y calcula el promedio recorriendo los valores.
notas = {
    "Matemáticas": 8.5,
    "Inglés": 7.0,
    "Programación": 9.2
}
total = sum(notas.values())
promedio = total / len(notas)
print("Promedio:", promedio)



#Dado el diccionario estudiante = {"nombre": "Ana", "nota": 7.0}, escribe un condicional que imprima "Aprobado" si la nota es mayor o igual a 6.0, o "Reprobado" si no.
estudiante = {"nombre": "Ana", "nota": 7.0}
if estudiante["nota"] >= 6.0:
    print("Aprobado")
else:
    print("Reprobado")



#Crea un diccionario horario = {"Lunes": "Matemáticas", "Martes": "Inglés", "Miércoles": "Programación"}. Pide al usuario que ingrese un día y muestra qué materia le corresponde (usa .get() para manejar el caso en que el día no exista en el horario).
horario = {"Lunes": "Matemáticas", "Martes": "Inglés", "Miércoles": "Programación"}
dia = input("Ingrese un día de la semana: ")
materia = horario.get(dia, "No hay clase ese día")
print("Materia:", materia)
