# Dilan Santiago Cañón González-Julian David Murcia Muñoz-Cesar Andres Contreras Suárez

# Problema de ordenamiento de una tienda de 
# cosmeticos de sofia. el objetivo es ordear los productos
# de la tienda y calcular el promedio de ventas por dia
# y el total de ventas mensuales.

class Producto:
    def __init__(self, nombre, categoria, precio, stock):
        self.nombre, self.categoria, self.precio, self.stock = nombre, categoria, precio, stock

    def __str__(self):
        return f"Nombre: {self.nombre}\nCategoria: {self.categoria}\nPrecio: {self.precio}\nStock: {self.stock}"

    def vender(self, cantidad):
        if self.stock >= cantidad:
            self.stock -= cantidad
            return True
        return False

    def aumentar_stock(self, cantidad):
        self.stock += cantidad

class Tienda:
    def __init__(self, nombre):
        self.nombre, self.productos, self.ventas_mensuales = nombre, [], 0

    def agregar_producto(self, producto):
        self.productos.append(producto)

    def vender_producto(self, nombre_producto, cantidad):
        producto = self.buscar_producto(nombre_producto)
        if producto:
            if producto.vender(cantidad):
                self.ventas_mensuales += producto.precio * cantidad
                return f"Venta realizada: {producto.nombre} x {cantidad}"
            return f"No hay stock suficiente de {producto.nombre}"
        return f"No se encontró el producto {nombre_producto}"

    def buscar_producto(self, nombre_producto):
        return next((p for p in self.productos if p.nombre == nombre_producto), None)

    def calcular_promedio_ventas_dia(self):
        return self.ventas_mensuales / (30 if self.ventas_mensuales > 0 else 1)

    def __str__(self):
        return f"Nombre: {self.nombre}\nProductos: {len(self.productos)}\nVentas mensuales: {self.ventas_mensuales}"

# Ejemplo de uso
tienda = Tienda("Sofia's Shop")

# Agregar productos a la tienda \\ usar la clase producto para crear objeto de venta 
tienda.agregar_producto(Producto("Labial rojo", "Labios", 10000, 10))
tienda.agregar_producto(Producto("Base de maquillaje", "Piel", 20000, 5))
tienda.agregar_producto(Producto("Máscara de pestañas", "Pestañas", 15000, 8))

# Vender productos
ventas = [
    tienda.vender_producto("Labial rojo", 2),
    tienda.vender_producto("Base de maquillaje", 1),
    tienda.vender_producto("Máscara de pestañas", 3),
]

# Mostrar información
print(tienda)
print(*ventas, sep="\n")

promedio_ventas_dia = tienda.calcular_promedio_ventas_dia()
print(f"Promedio de ventas por día: {promedio_ventas_dia}")
