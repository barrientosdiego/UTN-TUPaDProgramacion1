nombre_cliente = input("Ingrese su nombre: ")

while not nombre_cliente.isalpha():
    nombre_cliente = input("Ingrese su nombre correctamente (solo letras): ")

cantidad_productos = input("Ingrese la cantidad de productos a comprar: ")

while not cantidad_productos.isdigit():
    cantidad_productos = input("Ingrese la cantidad de productos a comprar correctamente: ")

lista_precios = ""
lista_descuentos = ""

for i in range (1, int(cantidad_productos) + 1):
    precio_producto = input(f"Ingrese el precio del producto {i}: ")
    lista_precios += (precio_producto + " ")
    descuento = input("¿El Procuto tiene descuento? (Ingrese s/n): ")
    lista_descuentos += descuento

print(f"Cliente: {nombre_cliente}")
print(f"Cantidad de productos: {cantidad_productos}")

total_sinDescuentos = 0
total_conDescuentos = 0
total_precios = 0

for i in range(int(cantidad_productos)):
    lista_precios2 = lista_precios.split()
    print(f"Producto {i + 1} - Precio: {lista_precios2[i]} Descuento (s/n): {lista_descuentos[i]}")
    total_sinDescuentos += float(lista_precios2[i])
    if lista_descuentos[i] == "s":
        total_conDescuentos += (float(lista_precios2[i]) - ((float(lista_precios2[i]) * 10) / 100))
        total_precios += (float(lista_precios2[i]) - ((float(lista_precios2[i]) * 10) / 100))
    else: total_precios += float(lista_precios2[i])

ahorro = 0
if "s" in lista_descuentos:
    ahorro = total_sinDescuentos - total_conDescuentos

promedio_productos = total_precios / float(cantidad_productos)

print(f"Total sin descuentos: ${total_sinDescuentos}")
print(f"Total con descuentos: ${total_conDescuentos}")
print(f"Ahorro: ${ahorro:.2f}")
print(f"Promedio por producto: {promedio_productos:.2f}")