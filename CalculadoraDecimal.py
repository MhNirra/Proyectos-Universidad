text = "Calculadora de los magios"
print("\n" + text + "\n" + "=" * len(text) + "\n") #texto solo decorativo para mostrar en pantalla

text2 = "Vamos a probar nuestra calculadora"
print("\n" + text2 + "\n" + "-" * len(text2) + "\n")#texto solo decorativo para mostrar en pantalla

select = input("Seleccione a qué desea convertir: \n" #le pido al usuario que seleccione en qué desea trabajar.
               "A: Decimal - Octal\n"
               "B: Decimal - Binario\n"
               "C: Decimal - Hexadecimal\n"
               "D: Octal - Decimal\n"
               "E: Binario - Decimal\n"
               "F: Hexadecimal - Decimal\n")

if select == "A":
    numero = int(input("Ingrese el valor en decimal (entero): "))

    lista = [] #creo una lista vacia

    while numero >= 1:
        lista.append(str(numero % 8)) #lleno la lista con el .append
        numero //= 8
    print("La conversión de decimal a octal es: ")
    print("".join(lista[::-1]))

elif select == "B":
    def decimal_a_binario(decimal):
        if decimal <= 0:
            return "0"
        # Aquí almacenamos el resultado
        binario = ""
        # Mientras se pueda dividir...
        while decimal > 0:
            # Saber si es 1 o 0
            residuo = int(decimal % 2)
            # E ir dividiendo el decimal
            decimal = int(decimal / 2)
            # Ir agregando el número (1 o 0) a la izquierda del resultado
            binario = str(residuo) + binario
        return binario


    decimal = int(input("Ingresa un número decimal: "))
    binario = decimal_a_binario(decimal)
    print(f"El número {decimal} es {binario} en binario")

elif select == "C":
    # Función que regresa el verdadero valor hexadecimal.
    # Por ejemplo, si recibe un 15 devuelve f, y si recibe un número menor a 10, devuelve el número sin modificarlo
    def obtener_caracter_hexadecimal(valor):
        # Lo necesitamos como cadena
        valor = str(valor)
        equivalencias = {
            "10": "a",
            "11": "b",
            "12": "c",
            "13": "d",
            "14": "e",
            "15": "f",
        }
        if valor in equivalencias:
            return equivalencias[valor]
        else:
            return valor


    def decimal_a_hexadecimal(decimal):
        hexadecimal = ""
        while decimal > 0:
            residuo = decimal % 16
            verdadero_caracter = obtener_caracter_hexadecimal(residuo)
            hexadecimal = verdadero_caracter + hexadecimal
            decimal = int(decimal / 16)
        return hexadecimal


    decimal = int(
        input("Escribe un número decimal, yo lo convertiré a hexadecimal: "))
    hexadecimal = decimal_a_hexadecimal(decimal)
    print(f"El decimal {decimal} es {hexadecimal} en hexadecimal")

elif select == "D":
    def octal_a_decimal(octal):
        decimal = 0
        posicion = 0
        # Invertir octal, porque debemos recorrerlo de derecha a izquierda
        # pero for in empieza de izquierda a derecha
        octal = octal[::-1]
        for digito in octal:
            valor_entero = int(digito)
            numero_elevado = int(8 ** posicion)
            equivalencia = int(numero_elevado * valor_entero)
            decimal += equivalencia
            posicion += 1
        return decimal


    octal = input("Ingresa un número octal: ")
    decimal = octal_a_decimal(octal)
    print(f"El octal {octal} es {decimal} en decimal")

elif select == "E":
    def binario_a_decimal(binario):
        posicion = 0
        decimal = 0
        # Invertir la cadena porque debemos recorrerla de derecha a izquierda
        binario = binario[::-1]
        for digito in binario:
            # Elevar 2 a la posición actual
            multiplicador = 2 ** posicion
            decimal += int(digito) * multiplicador
            posicion += 1
        return decimal
    binario = input("Ingresa un número binario: ")
    decimal = binario_a_decimal(binario)
    print(decimal)

elif select == "F":
    def obtener_valor_real(caracter_hexadecimal):
        equivalencias = {
            "f": 15,
            "e": 14,
            "d": 13,
            "c": 12,
            "b": 11,
            "a": 10,
        }
        if caracter_hexadecimal in equivalencias:
            return equivalencias[caracter_hexadecimal]
        else:
            return int(caracter_hexadecimal)


    def hexadecimal_a_decimal(hexadecimal):
        # Convertir a minúsculas para hacer las cosas más simples
        hexadecimal = hexadecimal.lower()
        # La debemos recorrer del final al principio, así que la invertimos
        hexadecimal = hexadecimal[::-1]
        decimal = 0
        posicion = 0
        for digito in hexadecimal:

            # Necesitamos que nos dé un 10 para la A, un 9 para el 9, un 11 para la B, etcétera
            valor = obtener_valor_real(digito)

            elevado = 16 ** posicion

            equivalencia = elevado * valor
            decimal += equivalencia

            posicion += 1
        return decimal


    hexadecimal = input("Ingresa un número hexadecimal: ")
    decimal = hexadecimal_a_decimal(hexadecimal)
    print(f"El hexadecimal {hexadecimal} equivale a {decimal} en decimal")
else:
    print("Las opciones disponibles son solo A, B, C, D, E y F")
    exit()
