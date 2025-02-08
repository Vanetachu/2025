
# Listas
# las listas son estructuras que permiten enlazar datos, estos datos pueden ser de cualquier tipo.
lista_integers = [1, 2, 3]
lista_strings = ["a", "b", "c"]
print(f"la lista de integers es: {lista_integers}")
print(f"la lista de strings es: {lista_strings}")

# las listas incluso podrían llegar a tener cosas de distinto tipo, pero no es recomendable
lista_mixta = ["12345", 3344, "guau"]
print(f"la lista mixta es: {lista_mixta}")

# para acceder a cosas de la lista se usa lista[n], donde n es un número que va de 0 al tamaño de la lista
print(lista_mixta[0])
print(lista_mixta[2])

# para saber el tamaño de una lista se usa len(lista), retorna un integer
lista_length = len(lista_mixta)
print(f"el tamaño de la lista_mixta es {lista_length}")


# Diccionarios
# los diccionarios son elementos que obedecen la regla {llave: valor}
# de esta manera podemos almacenar distinta información en un diccionario, incluso agregarle o quitarle elementos
# la llave se recomienda que sea un string y el valor puede ser lo que quieras (una lista, otro diccionario, int, etc)
diccionario_fecha = {"año": 2022, "mes": "Julio", "día": 13}
# accedemos a los elementos del diccionario llamando por su llave
cum = (
    str(diccionario_fecha["día"])
    + " de "
    + diccionario_fecha["mes"]
    + " del año "
    + str(diccionario_fecha["año"])
)
print(f"El cumpleaños del profe es {cum}")

# Listas de diccionario:
# las listas tambien pueden contener diccionarios, como en el ejemplo del escrito japonés
escritura1 = {
    "palabra": "かさ",
    "significado": "paraguas",
    "silabario": "hiragana",
    "origen": "Japón",
}
escritura2 = {
    "palabra": "ケーキ",
    "significado": "torta",
    "silabario": "katakana",
    "origen": "Japón",
}
escritura3 = {
    "palabra": "本",
    "significado": "libro",
    "silabario": "kanji",
    "origen": "China",
}
escritura4 = {
    "palabra": "日",
    "significado": "día",
    "silabario": "kanji",
    "origen": "China",
}

lista_escrituras = [escritura1, escritura2, escritura3, escritura4]
