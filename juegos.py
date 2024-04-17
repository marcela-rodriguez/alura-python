import adivina_el_numero
import el_ahorcado
print("juegos python")
print("              ")
print("(1) adivinaza (2) horca")
juego=int(input("elige una de las opciones de juego: "))
if juego == 1:
    print("juego de adivinanza")
    adivina_el_numero.jugar()
elif juego== 2:
    print("juego de horca")
    el_ahorcado.jugar()
