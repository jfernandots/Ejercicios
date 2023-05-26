# 1.- Indicar cuál es el menor de tres enteros solicitados al usuario

# n1 = int(input("Inserta el primer Número: "))
# n2 = int(input("Inserta el segundo Número: "))
# n3 = int(input("Inserta el tercer Número: "))
#
# if n1 < n2 and n1 < n3:
#     print(str(n1) +" es el menor")
# else:
#     if n2 < n1 and n2 < n3:
#         print(str(n2) +" es el menor")
#     else:
#         print(str(n3) +

# 2.- Dispones de frase y una letra, solicitados al usuario y debes
# mostrar la cantidad de veces que aparece la letra en la frase.

# frase = input("Ingrese la frase: ")
# letra = input("Ingrese la letra a buscar: ")
# cont = 0
# for i in frase:
#     if i == letra:
#         cont += 1
# print(cont)

# 3.- Suma o resta dos números reales solicita la información al usuario

# n1 = float(input("Ingrese el primer número: "))
# n2 = float(input("Ingrese el segundo número: "))
# operacion = input("Indique + si desea sumar o - si desea restar: ")
# if operacion == "+":
#     print("El resultado es: " + str(n1+n2))
# else:
#     print("El resultado es: " + str(n1-n2))

# 4.- Permite validar a un usuario con 3 intentos y los datos de
# validación correctos almacenados en dos constantes predefinidas.

USUARIO = "fernando"
CLAVE = "fernando"
i = 0
while i < 3:
    usuario = input("Ingrese su usuario: ")
    clave = input("Ingrese su clave: ")
    if usuario != USUARIO or clave != CLAVE:
        print("Datos erróneos, quedan " + str(2-i) + " intentos")
        i += 1
    else:
        print("Bienvenido")





# 5.- Crea una variable que sea una letra, si es una a muestra el número 7,
# si es una b, el 9, si es una c el 101 y si no es ninguno de los tres,
# indica que se han equivocado de letra

# 6.- Dispones de tres números enteros H, M, S correspondientes a hora,
# minutos y segundos respectivamente, debes comprobar si se trata de una hora válida.

# 7.- Solicita al usuario dos fechas del mismo año e indica la cantidad de días que hay entre ellas.

# 8.- Añade el año al ejercicio 7, siempre por encima del 2000 e indica la diferencia en semanas
# y días que hay entre las dos fechas y cuál es anterior y posterior.

# 9.-