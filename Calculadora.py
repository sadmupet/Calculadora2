num1 = int(input("numero 1: ")) 
num2 = int(input("numero 2: "))

valor = 0
while True:
    print("""seleccione opcion
            1- Sumar 

        """)

    valor = int(input("Elige una opcion: ") )     

    if valor == 1:
        print("la suma es",num1+num2)
        break;

    else:
        print("Opcion incorrecta")
        break;
