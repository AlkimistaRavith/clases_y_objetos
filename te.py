#Clase te.
class Te():
    #Atributo de clase
    duracion = 365
    
    #Sabores
    sabores = {
        1 : {"Nombre": "Té negro", "Tiempo": 3 , "Recomendacion": "Desayuno"} ,
        2 : {"Nombre": "Té verde", "Tiempo": 5 , "Recomendacion": "Almuerzo"} ,
        3 : {"Nombre": "Agua de Hierbas", "Tiempo": 6 , "Recomendacion": "Once"}
    }

    precios = {
        300 : 3000 ,
        500 : 5000
    }

    #metodo estatico
    @staticmethod
    def receta(sabor:int):
        """Retorna:
        Tiempo de preparación (en minutos), y recomendación de uso, según el sabor de té.
        Sabores disponibles
        1: Corresponde a Té negro
        2: Corresponde a Té verde
        3: Corresponde a Agua de hierbas.
        """

        pedido = Te.sabores[sabor] #llamar el objeto del diccionario sabores de la clase Te. en el numero sabor.

        return pedido["Nombre"], pedido["Tiempo"], pedido["Recomendacion"]

    #Obtener precio
    @staticmethod
    def obtener_precio(formato:int):
        """Retorna precio para el formato indicado.
        Formatos disponibles:
        300 gr : $3000
        500 gr : $5000
        """

        return Te.precios[formato]