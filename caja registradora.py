""" Proyecto caja registradora
Realizado por: Jeysson Peña
Descripción: Este programa simula una caja registradora que permite 
al usuario ingresar los precios de los productos comprados y luego 
imprime un recibo con el total de ventas y la cantidad de productos.
"""
#Definicion de funciones
def imprimir_recibo(recibo, total_ventas, cantidad_productos):
    print("\n--- RECIBO DE COMPRAS ---")
    for elemento in recibo:
        print(f"$ {elemento:.2f}")
    print("-------------------------")
    print(f"Total: $ {total_ventas:.2f}")
    print(f"Cantidad de productos: {cantidad_productos}")
def guardar_en_archivo(recibo, total_ventas, cantidad_productos):
    with open("recibo.txt", "w") as archivo:
        archivo.write("--- RECIBO DE COMPRAS ---\n")
        for elemento in recibo:
            archivo.write(f"$ {elemento:.2f}\n")
        archivo.write("-------------------------\n")
        archivo.write(f"Total: $ {total_ventas:.2f}\n")
        archivo.write(f"Cantidad de productos: {cantidad_productos}\n")
        print("Recibo guardado en 'recibo.txt'.")
#programa principal
total_ventas = 0 #acumulador para el total de ventas
recibo = []      #estructura de datos para almacenar los precios de los productos
#bucle infinito para ingresar los precios de los productos ilimitadamente hasta que el usuario decida terminar
while True:
    entrada = input("precio del producto o presiona la letra t para terminar: ")
    #Si el usuario ingresa "t", se rompe el bucle y se termina la entrada de datos
    if entrada == "t":
        break
    #proteccion de errores para evitar que el programa se caiga si el usuario ingresa un valor no numérico
    try:
     precio = float(entrada)
     recibo.append(precio)
     total_ventas += precio
    except ValueError:
        print("Por favor ingresa un número válido o 't' para terminar.")
#cierre del proceso fuera del bucle.
cantidad_productos = len(recibo)
#se llama a la función para imprimir el recibo con los datos recopilados
imprimir_recibo(recibo, total_ventas, cantidad_productos)
#se llama a la función para guardar el recibo en un archivo .txt
guardar_en_archivo(recibo, total_ventas, cantidad_productos)