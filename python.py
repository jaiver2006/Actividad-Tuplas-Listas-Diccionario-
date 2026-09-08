#Crea una tupla con las coordenadas GPS de tu ciudad (latitud, longitud) e imprime cada valor por separado.
coordenadas = (40.7128, -74.0060)  # Ejemplo: Nueva York
print("Latitud:", coordenadas[0])
print("Longitud:", coordenadas[1])



#Crea una tupla (nombre, edad, curso) para representar un estudiante. Intenta modificar el curso y explica qué error aparece y por qué.
estudiante = ("Juan", 20, "Matemáticas")
# Intentando modificar el curso
# estudiante[2] = "Física"  # Esto causará un error porque las tuplas son inmutables
print("Estudiante:", estudiante[0])
print("Edad:", estudiante[1])
print("Curso:", estudiante[2])



#Dada la tupla dias = ("Lunes", "Martes", "Miércoles", "Jueves", "Viernes"), imprime solo el tercer día usando su índice.
dias = ("Lunes", "Martes", "Miércoles", "Jueves", "Viernes")
print("Tercer día:", dias[2])
