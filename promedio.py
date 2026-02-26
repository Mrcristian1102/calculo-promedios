nombre_estudiantes = input("Ingrese su nombre: ")

nota1 = float(input("Ingrese su primera nota: "))
nota2 = float(input("Ingrese su segunda nota: "))
nota3 = float(input("Ingrese su tercera nota: "))

promedio_notas = (nota1 + nota2 + nota3) / 3

print("El estudiante", nombre_estudiantes, "tiene un promedio de:", round(promedio_notas, 2))