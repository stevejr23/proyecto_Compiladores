import ply.lex as lex
import codecs
import os

reservadas = ['Iron',  # If
              'Majo',  # While
              'Nadya',  # For
              'return',
              'Man',  # ifelse
              'int',
              'float']

tokens = reservadas+['Id', 'Numero', 'Suma', 'Menos', 'Multi', 'Dividir', 'Modulo', 'Potencia',
                     'Igual', 'Menor', 'MenorIgual', 'Mayor', 'MayorIgual', 'Diferente', 'DobleIgual',
                     'And', 'OR', 'Not', 'ParentIrq', 'ParentDer', 'LlaveIrq', 'LlaveDer', 'PuntoYComa'
                     ]

# declaracion de los tokens

t_ignore = '\t '
t_Suma = r'\+'
t_Menos = r'\-'
t_Multi = r'\*'
t_Dividir = r'/'
t_Modulo = r'\%'
t_Potencia = r'(\*{2} | \^)'
t_Igual = r'='
t_Menor = r'<'
t_MenorIgual = r'<='
t_Mayor = r'>'
t_MayorIgual = r'>='
t_Diferente = r'!='
t_DobleIgual = r'=='
t_And = r'\&'
t_OR = r'\|'
t_Not = r'\~'
t_ParentIrq = r'\('
t_ParentDer = r'\)'
t_LlaveIrq = r'\{'
t_LlaveDer = r'\}'
t_PuntoYComa = r';'

# identificador

def t_Id(t):
    r'[a-zA-Z][a-zA-Z]*'  # Reconocer todo el Abecedario En Mayuscula o Minuscula
    if t.value.upper() in reservadas:
        t.value = t.value.upper()  # Mayusculas
        t.type = t.value  # Minusculas

    return t

# nueva linea

def t_nuevalinea(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# comentario

def t_Comentario(t):
    r'\#.*'
    pass

# numero

def t_Numero(t):
    r'\d+'
    t.value = int(t.value)
    return t

# para el error

def t_error(t):
    print(chr(27)+"[1;35m"+"Caracter No Reconocido '%s'" % t.value[0])
    t.lexer.skip(1)

# busca y seleciona el fichero

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

directorio = 'Prueba/'
archivo = buscarFicheros(directorio)
test = directorio+archivo
fp = codecs.open(test, "r", "utf-8")
cadena = fp.read()
fp.close()

analizador = lex.lex()
analizador.input(cadena)
i = 1 #Representa la línea
while True:
	tok = analizador.token()
	if not tok : break
	print ("\t"+str(i)+" - " +
    "Linea: " + str(tok.lineno) + 
    "\t Tipo: " + str(tok.type) + 
    "\t Valor:  " + str(tok.value) + 
    "\t Posicion -->  " + str(tok.lexpos))
	i += 1
