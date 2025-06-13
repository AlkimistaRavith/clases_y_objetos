from te import Te

#Solictando sabor (con numero 1, 2 o 3)
print("Selecciona el sabor de té (1. Té negro | 2. Té verde | 3. Agua de hierbas): ")
sabor = int(input(f"Ingresa tu elección: "))

#Solictando formato (con numero 300 o 500)
print("Elige el formato que quieres llevar (300 o 500) grs: ")
formato = int(input(f"Ingresa tu opción: "))

nombre, tiempo, recomendacion = Te.receta(sabor) #Para traer los datos de la clase (preocuparse del orden: nombre = Nombre, tiempo = Tiempo, recomendacion = Recomendacion).

precio = Te.obtener_precio(formato)

duracion = Te.duracion

print(f"""
a. Sabor del tipo de té (como texto) {nombre}
b. Formato (como número) {formato}
c. Precio (como número) {precio}
d. Tiempo (como número) {tiempo}
e. Recomendación (como texto) {recomendacion}
f. Duración (numero): {duracion}
""")