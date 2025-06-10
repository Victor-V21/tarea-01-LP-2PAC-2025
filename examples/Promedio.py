# Sacar el promedio de un estudiante y que salga si el estudiante aprobo o no la clase.
print("---Cálculo del Promedio de una Materia---\n")
materia = input("Ingrese el nombre de la materia: ")
nota1 = float(input("Ingresa la primera nota del estudiante: "))
nota2 = float(input("Ingresa la segunda nota del estudiante: "))
nota3 = float(input("Ingresa la tercera nota del estudiante: "))
nota4 = float(input("Ingresa la cuarta nota del estudiante: "))

promedio = round((nota1 + nota2 + nota3 + nota4) / 4, 2)

if promedio >= 65:
    print("El promedio de ",materia, "es de:", promedio, "Su materia ha sido aprobada, ¡Felicidades!")
else:
    print("El promedio de ",materia, "es de:", promedio, "Su materia ha sido reprobada.")