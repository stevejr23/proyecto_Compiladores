

from curses.ascii import isdigit
import codecs
import os

# Aritmeticos
operador_aritmetico = [
    '+',
    '-',
    '*',
    '/',
    '%',
    '=']
# Relacionales
operador_relacionales = [
    '<',
    '>',
    '<=',
    '>=',
    '!=',
    '==']
# Reservadas
palabras_reservadas = [
    'Iron',  # If
    'Majo',  # While
    'Nadya',  # For
    'return',
    'Man',  # ifelse
    'int',
    'float',
    'inicio',
    'fin']
# Separadores
separadores = ['(',
               ')',
               '{',
               '}',
               ';',
               '$',
               '[',
               ']',
               '"',
               ' ']
# Logicos
operadores_logicos = [
    '&',  # And
    '|',  # Or
    '~',  # Not
    '&&',  # And
    '||',  # Or
]
# busca y seleciona el archivo

def buscarFicheros(directorio):
    ficheros = []
    numArchivo = ''
    respuesta = False
    cont = 1

    for base, dirs, files in os.walk(directorio):
        ficheros.append(files)

    for file in files:
        print(str(cont)+". "+file)
        cont = cont+1

    while respuesta == False:
        numArchivo = input(chr(27)+"[1;37m"+'Numero del test: ')
        for file in files:
            if file == files[int(numArchivo)-1]:
                respuesta = True
                break
    print(chr(27) + "[1;33m"+"\nSeleccionste el archivo \"%s\" \n" %
          files[int(numArchivo)-1])
    return files[int(numArchivo)-1]

file = 'proyecto_Compiladores/Prueba/'
archivo = buscarFicheros(file)
test = file + archivo
fp = codecs.open(test, "r", "utf-8")
cadena = fp.read()
token = cadena.split()
length = len(token)
fp.close()

for i in range(0, length):
    if token[i] in operador_aritmetico:
        print("Operador Aritmetico (", token[i], ")")
    elif token[i] in operador_relacionales:
        print("Operador Relacional (", token[i], ")")
    elif token[i] in palabras_reservadas:
        # if token[i].value.upper() in palabras_reservadas:
        # i.value = i.value.upper()  # Mayusculas
        # i.type = i.value  # Minusculas
        print("Palabras Reservadas (", token[i], ")")
    elif token[i] in separadores:
        print("Separadores (", token[i], ")")
    elif token[i] in operadores_logicos:
        print("Operadores Logicos (", token[i], ")")
    elif token[i].isdigit():
        print("Esto es un digito (", token[i], ")")
    elif token[i].islower():
        print("Esto es un Texto (", token[i], ")")
    else:
        print("No pertenece al analizador lexico (", token[i],")") 

        
    