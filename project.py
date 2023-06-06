#1. preguntar al usuario la longitud de la contraseña
#2. preguntar si quiere que contenga caracteres especiales
#3. preguntar si quiere que contenga numeros
#4. preguntar si el usuario y sitio web
#5. preguntar si quiere generar uan contraseña(1, 2, 3) o usar ya creada
#6. poner la url del sitio, el usuario y la contraseña en un diccionario
#7. guardar la terna (sitio, user, pwd) en una lista
#8. pasar todos los elementos de la lista a un archivo txt (ver como se hace esto)

import random
import string

passwords = []
seguir = True
def generar_pass(min_long, nums=True, espchars=True):
    letras = string.ascii_letters
    digitos = string.digits
    especial = string.punctuation 

    caracteres = letras
    if (nums):
        caracteres += digitos
    if(espchars):
        caracteres += especial

    password = ""
    criterio = False
    tiene_num = False
    tiene_especial = False

    while(not criterio or len(password) < min_long):
        nuevo_char = random.choice(caracteres)
        password += nuevo_char

        if nuevo_char in digitos:
            tiene_num = True
        elif nuevo_char in especial:
            tiene_especial = True

        criterio = True
        if nums:
            criterio = tiene_num
        if espchars:
            criterio = criterio and tiene_especial
    return(password)

while(seguir):
    sitio = input("Ingrese la url el sitio web: ")
    user = input("Ingrese el usuario del sitio web: ")
    pregunta = input("¿Desea generar una contraseña? (y/n): ")
    if pregunta.lower() == 'y':
        min_long = int(input("Ingrese la longitud de la contraseña: "))
        nums = input("¿Desea tener numeros? (y/n): ").lower() == 'y'
        espchars = input("¿Desea tener caracteres especiales? (y/n): ").lower() == 'y'
        pwd = generar_pass(min_long, nums, espchars)
        print("Contraseña generada: " + pwd)
    else:
        pwd = input("Ingrese la contraseña del sitio web: ")

    d = {
        "Url Sitio": sitio,
        "User": user,
        "Contraseña": pwd,
    }

    print(d)
    passwords.append(str(d))
    seguir = input("¿Quiere seguir guardando contraseñas? (y/n)")
    if seguir.lower() == "n":
        seguir = False

with open('pass-list.txt', 'a', encoding='utf-8') as f:
    for p in passwords:
        print(p)
        f.write(p)
        f.write('\n ////////////////// \n')
    