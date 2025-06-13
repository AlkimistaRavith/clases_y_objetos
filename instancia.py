from te import Te

#instanciando la clase
te1 = Te()
te2 = Te()

#Obteniendo el tipo de la variable te1 y te2 (isntancias)
tipo1 = type(te1)
tipo2 = type(te2)

#Verificando si son del mismo tipo o no.
if tipo1 == tipo2:
    print("Ambos objetos son del mismo tipo")
else:
    print("Los objetos no son del mismo tipo")