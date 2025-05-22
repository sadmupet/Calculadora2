num1 = int(input("numero 1: ")) 
num2 = int(input("numero 2: "))

valor = 0
while True:
    print("""seleccione opcion
            1- Sumar 
            2- Resta
        """)

    valor = int(input("Elige una opcion: ") )     

    if valor == 1:
        print("La suma es: ", num1+num2)
        break;
    if valor == 2:
        print("La resta es: ", num1 - num2)
        break;

    else:
        print("Opcion incorrecta")
        break;
