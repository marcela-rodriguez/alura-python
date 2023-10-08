import random
print("Adivina el numero")

#numero_secreto = round(random.random()*100)
numero_secreto = random.randint(1,100)
total_intentos = 3

     
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
            print("¡Has acertado!")
            break
        else:
            if mayor:
                print("El numero que dijitaste es mayor")
            elif menor:
                print("El numero que dijistate es menor")
                
print("El juego a concluido")
