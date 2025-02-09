# Vamos a repasar primero la operatoria entre int y string
int_1 = 1
int_2 = 2
# el operador + entre integers es la suma
suma_ints = int_1 + int_2
# usamos print con un f string (f"") para poder usar variables dentro
print(f"la suma de integers es: {suma_ints}")
# en este contexto, int_1 y int_2 no fueron modificados, solo suma_ints tiene el valor de la suma

string_1 = "Hola "
string_2 = "Github "
# el operador + entre strings es la concatenación (añadir un string al final de otro string)
suma_strings = string_1 + string_2
# suma_strings retorna "Hola Github"
print(f"la concatenación de strings es: {suma_strings}")
# en este contexto, string_1 y string_2 no fueron modificados, solo suma_strings tiene el valor de la concatenación

# cómo pasamos un int a string?
string_1 = str(int_1)
string_2 = str(int_2)
# el operador + entre strings es la concatenación (añadir un string al final de otro string)
suma_strings = string_1 + string_2
# suma_strings retorna el string "12"
print(f"la concatenación de strings es: {suma_strings}")

# cómo pasamos un string a integer?
int_3 = int(suma_strings)
# retorna el integer 12
multiplicacion = int_3 * 3
# retorna la multiplicación es 12 * 3 = 36
print(f"la multiplicación de integers es: {multiplicacion}")

# si cambiamos el valor de una variable, no afectamos las otras variables
int_1 = 50
print(f"el valor de int_1 es {int_1}")
print(f"el valor de int_2 siempre fue {int_2}")
print(f"el valor de multiplicacion siempre fue {multiplicacion}")

# Ahora vamos a ver los if y else
# if funciona con un argumento que va a ser un boolean
# boolean = True o False, no hay un entremedio
verdad = True
if verdad:
    print(f"Esto es Verdad, verdad es {verdad}")

# los boolean también se pueden negar
mentira = False
if not mentira:
    print(f"Esto no es mentira, mentira es {mentira}")

# si quiero comparar 2 integers la lógica sería
if int_1 == 1:
    # int_1 == 1 significa que compara el valor de la variable 'int_1' y lo compara con el integer 1. Si esto es
    # verdadero ejecuta el bloque correspondiente
    print("El int_1 es igual a 1 (como integer)")
if int_1 == "1":
    # int_1 == 1 significa que compara el valor de la variable 'int_1' y lo compara con el string 1. Si esto es
    # verdadero ejecuta el bloque correspondiente, pero en este caso, se ejecuta else dado que int_1 no es string
    print("Cuidado con esto !!! ")
else:
    # aqui queda el bloque que se ejecutaría en el caso de que la afirmación del if sea False
    print("El int_1 no es igual a '1' puesto que no es un string")
string_1 = "perro"
# si quiero comparar 2 strings la lógica sería
if string_1 == "perro":
    print("guau")
else:
    print("el string_1 no es un perro")
