print("Adivina el numero")

numero_secreto = 55
total_intentos = 3
intento = 1

while total_intentos >= intento:       
        print(f"intentos {intento} de {total_intentos}")
        intento += 1  

        entrada = int(input("Digita un numero: "))
        print("El numero que dijistaste es: ", entrada)

        acerto = numero_secreto == entrada

        mayor = entrada > numero_secreto
        menor = entrada < numero_secreto

        if acerto:
         print("¡Has acertado!")
        else:
            if mayor:
                print("El numero que dijitaste es mayor")
            elif menor:
                print("El numero que dijistate es menor")
        
print("El juego a concluido")
