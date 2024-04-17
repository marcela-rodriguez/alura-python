def jugar():
    print("El ahorcado")
    print(".......................")

    jugar()
    
    
    palabra_secreta= "banana".upper()
    letras_acertadas= ['-'for letra in palabra_secreta]
    oportunidades= 3
    print(oportunidades)

    ahorco= False
    acerto= False
    errores=0 
   
        
    while (not ahorco and not acerto):
        intento=input("\n Digite una letra : ")
        intento= intento.strip().upper()

        if intento in palabra_secreta:
            indice= 0
            print(f"la {intento} es corecta y te quedan {oportunidades - errores} intentos más")
            
            for letra in palabra_secreta:
                if intento == letra:
                    letras_acertadas[indice]=letra
                    #print(f"encontre la '{letra}' en la posicion {indice}")
                indice+=1
            print(letras_acertadas)
            if  "-" not in letras_acertadas:
                print("ganaste ")
                break
        else:
            errores+=1
            print(f"la {intento} es incorecto y te quedan {oportunidades - errores} intentos más")
            if errores == oportunidades:
                print("perdiste")
                break

        print(f"Errores: {errores}")

        
        #if ahorco:
            #print("perdiste el juego")
        #elif acerto:
            #print("ganaste el juego")
    print("fin del jugo")



