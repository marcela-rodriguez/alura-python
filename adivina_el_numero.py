import random

def jugar():
    print("Adivina el numero")
    print("Elige el nivel de dificultad")
    print(" (1)novato (2) intermedio (3) avanzado")

    nivel1=int(input("Nivel: "))
    if nivel1 ==1:
        total_intentos=20
    elif nivel1==2:
        total_intentos=10
    else:
        total_intentos=5

    #numero_secreto = round(random.random()*100)
    numero_secreto = random.randint(1,100)
    print(numero_secreto)
    puntos=1000

    for intento in range(1,total_intentos +1):
            print(f"intentos {intento} de {total_intentos}")
                
            entrada = int(input("Digita un numero: "))
            if entrada < 1 or entrada >100:
                print("Digite un numero mayor que 0 y menor o igual a 100.")
                continue
            
            print("El numero que dijistaste es: ", entrada)

            acerto = numero_secreto == entrada

            mayor = entrada > numero_secreto
            menor = entrada < numero_secreto

            if acerto:
                print(f"¡Has acertado!tu puntaje es {puntos}")
                break
            else:
                if mayor:
                    print("El numero que dijitaste es mayor")
                elif menor:
                    print("El numero que dijistate es menor")
                puntos_perdidos =abs(numero_secreto - entrada)
                puntos= puntos - puntos_perdidos    
    print("El juego a concluido")
if (__name__=="__main__"):
    jugar()
