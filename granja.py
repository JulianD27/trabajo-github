class Produccion:
    def calcular_produccion(self):
        pass

class Cultivo(Produccion):
    def __init__(self, nombre, tipo, area, rendimiento):
        self.nombre = nombre
        self.tipo = tipo
        self.area = area
        self.rendimiento = rendimiento

    def calcular_produccion(self):
        return self.area * self.rendimiento

class Animal(Produccion):
    def __init__(self, especie, raza, edad, peso):
        self.especie = especie
        self.raza = raza
        self.edad = edad
        self.peso = peso

    def calcular_produccion(self):
        # Aquí puedes definir la producción de cada animal de acuerdo a tus necesidades
        # Por ejemplo, podrías calcularla en función del peso, edad, etc.
        return self.peso * 0.5

class Granja:
    def __init__(self):
        self.cultivos = []
        self.animales = []

    def agregar_cultivo(self, cultivo):
        self.cultivos.append(cultivo)

    def eliminar_cultivo(self, cultivo):
        self.cultivos.remove(cultivo)

    def agregar_animal(self, animal):
        self.animales.append(animal)

    def eliminar_animal(self, animal):
        self.animales.remove(animal)

    def calcular_produccion_total(self):
        produccion_total = 0
        for cultivo in self.cultivos:
            produccion_total += cultivo.calcular_produccion()
        for animal in self.animales:
            produccion_total += animal.calcular_produccion()
        return produccion_total

    def generar_reporte_produccion(self):
        print("Producción total de la granja:")
        print("Cultivos:")
        for cultivo in self.cultivos:
            print(f"{cultivo.nombre}: {cultivo.calcular_produccion()} unidades")
        print("Animales:")
        for animal in self.animales:
            print(f"{animal.especie}: {animal.calcular_produccion()} unidades")


# Ejemplo de uso del sistema
if __name__ == "__main__":
    granja = Granja()

    # Agregar cultivos
    cultivo_maiz = Cultivo("Maíz", "Cereal", 100, 10)
    cultivo_trigo = Cultivo("Trigo", "Cereal", 150, 8)
    granja.agregar_cultivo(cultivo_maiz)
    granja.agregar_cultivo(cultivo_trigo)

    # Agregar animales
    animal_vaca = Animal("Vaca", "Holstein", 5, 500)
    animal_cerdo = Animal("Cerdo", "Yorkshire", 2, 150)
    granja.agregar_animal(animal_vaca)
    granja.agregar_animal(animal_cerdo)

    # Generar reporte de producción
    granja.generar_reporte_produccion()

    # Calcular producción total
    produccion_total = granja.calcular_produccion_total()
    print(f"\nProducción total de la granja: {produccion_total} unidades")