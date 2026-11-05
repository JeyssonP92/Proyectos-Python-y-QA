import random
# Juego de adivinar el número
numero_secreto = random.randint(1, 50)
print("¡Bienvenido al juego de adivinar el número!, tienes 5 intentos para adivinar el número.")
print("Estoy pensando en un número entre 1 y 50.")
#se usa range(1, 6) para que el bucle se ejecute 5 veces.
for intento in range(1, 6):
    print(f"\n Intento {intento} de 5:")
    
    intento_usuario = int(input("Ingresa tu número:"))
    if intento_usuario == numero_secreto:
        print("¡Felicidades! Has adivinado el número.")
        break
    elif intento_usuario < numero_secreto:
        print("El número es mayor.")
    else:
        print("El número es menor.")
else:
    print(f"Lo siento, no has adivinado el número. El número secreto era {numero_secreto}.")