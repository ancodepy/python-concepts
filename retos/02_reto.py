"""
Reto #6: INVIRTIENDO CADENAS

 
 * Crea un programa que invierta el orden de una cadena de texto
 * sin usar funciones propias del lenguaje que lo hagan de forma automática.
 * - Si le pasamos "Hola mundo" nos retornaría "odnum aloH"
"""

reverso = lambda cadena: cadena[::-1]

print(reverso("Hola mundo"))