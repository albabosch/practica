print("Si vols fer una suma, indica 1 \nSi vols fer una resta 2 \nSi vols fer una multiplicacio 3 \nSi vols fer una divisio 4")
valor = input("Indica 1,2,3 o 4: ")

num1 = input ("Indica valor: ")
num2 = input("Indica valor: ")


if (valor == 1):
    suma = num1 + num2
    print("La suma dels dos nombres " + str(num1) + " + " + str(num2) + " es " + str(suma))


if (valor == 2):
    resta = num1 - num2
    print("La resta dels dos nombres " + str(num1) + " - " + str(num2) + " es " + str(resta))


if (valor == 3):
    multi = num1 * num2
    print("La multiplicacio dels dos nombres " + str(num1) + " x " + str(num2) + " es " + str(multi))


if (valor == 4):
    if (num1 != 0):
        div = num1/num2
        print("La divisio dels dos nombres " + str(num1) + " : " + str(num2) + " es " + str(div))
    else:
        print("Infinit")