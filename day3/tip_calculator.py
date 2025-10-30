#Calculador de propina

cuenta = float(input("Ingresa el monto total de la cueta: "))
propina = int(input("Ingresa el porcentaje de propina que deseas agregar: "))
personas = int(input("Ingresa la cantidad de personas: "))
total = cuenta + (cuenta * propina / 100)
division = total / personas

print(f"Total con propina es: {total:.2f} ")
print(f"cada persona debe pagar: {division:.2f}")
