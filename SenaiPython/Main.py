#Main
from Operario import Operario
 
class Main:
    def inicio():
        print("esta entrando como:")
        r = input("1-Operario   2-Gerente")
        if r == 1:
            Operario.Main()
        else:
            Operario.Main()
        
Main.inicio()