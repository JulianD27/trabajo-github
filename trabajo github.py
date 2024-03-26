# Julian David Murcia Muñoz
# ejercicio 1:
print("hola, ingresa 15 valores")

numeros = []
for i in range(15):
    valor = float(input("ingresa el valor {}: ".format(i+1)))
    numeros.append(valor)

suma_total = sum(numeros)

promedio = suma_total / len(numeros)

print("La suma de los valores es:", suma_total)
print("El promedio de los valores es:", promedio)

#ejercicio 2: 

def reparto_vacunas():
    inventario = 1000

    while inventario > 0:
        print("Inventario actual de vacunas:", inventario)

        if inventario < 200:
            print("El inventario es menor a 200 unidades.")
        
        entregas = int(input("ingrese la cantidad de vacunas entregadas hoy (o 0 para salir): "))

        if entregas == 0:
            print("saliendo del programa")
            break
        inventario -= entregas

    print("el inventario de vacunas ha llegado a cero. Fin del programa")

if __name__ == "__main__":
    reparto_vacunas()
