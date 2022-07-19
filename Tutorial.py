# Tutorial Python

#------------------------------------------------------

# Imprimir por pantalla
from asyncio.windows_utils import pipe
from gettext import install


print('hello world!')

# Obtener tipo de la variable
type(2.14)
type(2)
type("2.14")

# Definir variable
name = "Santiago"
print(name[0])

# Operadores de comparacion
# == True si son iguales
# != True si son distintos
# < True si el primer elemento es menor que el segundo
# > True si el primer elemento es mayor que el segundo
# <= True si el primer elemento es menor o igual que el segundo
# <= True si el primer elemento es mayor o igual que el segundo

# Operadores relacionales 
# ~ Negate
# & And
# | Or

# Operaciones aritmeticas
# + suma
# - resta
# / division
# * multiplicacion 
# ** potencia
# % mod
# // division piso

#------------------------------------------------------

# Estructura Tupla
tup1 = (1,2)
tup2 = tuple()
tup3 = tuple([1,2,3])
tup4 = ('fantasia',10,5)
tup5 = ()

# Indexacion
print(tup4[0])
print(tup4[1])
print(tup4[2])

# Concatenacion
tup2 = tup1 + ("Ciencia ficcion", 1)
tup2 

# Slice 
tup2[0:3]

# Longitud
len(tup2)

# Sort
numeros = (0, 1, 2, 3, 4, 9, 8, 7, 6, 5)
sorted(numeros)

# Anidamiento
tup6 = (1, 2, ("terror", "fantasma") ,(3,4),("fantasía",(1,2)))
print("Element 2, 0 of Tuple: ",   tup6[2][0])

# Cantidad de apariciones
tup7 = ('a', 'b', 'c', 'a')
tup7.count('a')

# Get indice (retorna siempre la primer aparicion)
tup7.index('a')

#------------------------------------------------------

# Estructura List
list1 = []
list2 = list()
list3 = ['a','b','c']
list4 = ['Harry Potter y la Piedra Filosofal',2001,5]
print(list4[0])
print(list4[1])
print(list4[2])

# Append agrega al final de la lista
list4.append('hola')

# Insert
list4.insert(0,'fanatico')

# Sobreescribir 
list4[0] = 1

# Pop
print(list4.pop())

# Borrar un elemento por posicion
del(list4[0])

# Borrar la primer aparicion de un elemento
list4.remove(2001)

# Sort
list4.sort()
list4.sort(reverse=True)

# Copia una lista, si modifico una afecta a la otra
A = ['Harry','Potter']
B = A

# Clonar una lista, si modifico una no afecta a la otra
C = A[:]

#------------------------------------------------------

# Estructura Diccionario/Mapas
dic1 = dict()
dic2 = {'key1' : 1, 'key2' : 2 , 'key3' : 3, 'key4' : 3}

# Obtener dato por key
print(dic1.get('key1'))

# Borrar un dato 
del(dic2['key2'])

# Obtener todas las keys del diccionario
dic2.keys()

# Obtener todos los valores del diccionario
dic2.values()

# Obtener (key, value) del diccionario
dic2.items()

# Agregar un valor al diccionario
dic2['key5'] = 'hola'

#------------------------------------------------------

# Condicion if 
if (6 > 5):
    print('hola')
else:
    print('chau')

# Condicion if-elif
if (6 == 5):
    print('hola')
elif (6 <= 5):
    print('chau')
else:
    print('buenas tardes')

# Iteracion for
dates = [1975,1989,2021]
for i in range(len(dates)): # creamos un range desde 0 hasta el tamaño de la lista
    print(dates[i])  

for year in dates:  
    print(year)   

for i in range(0, 8):
    print(i)

# Iteracion while
i = 0
while (i < 3):
    print(i)
    i = i + 1

#------------------------------------------------------

# Funcion
def saludar():
    print('hola mundo')

# Funcion var local y global
def globalAndLocal(x,y):
    a = x * y
    return a
    
print(globalAndLocal(1,2))
print(a) # Arrojara error porque la variable dejo de existir

# Funcion con parametro default (Si no se le pasa valor utiliza ese)
def add(x,y=1):
    return x + y

# Funcion con cantidad de parametros variables
def add_n(*args):
    reslist = []
    # Recorro todos los parametros pasados y los guardo en una lista
    for i in args:
        reslist.append(i)
    return sum(reslist)

# Funcion con multiples retornos
def multReturns():
    return 'Hello', 'World'

#------------------------------------------------------

# Manejo de archivos - Descarga
import gdown 
url = "https://drive.google.com/uc?export=download&id=1DEQPa2kjRIxDWfL0NiizUs0sdr6ZsyYa"
datapath = 'test.txt'
gdown.download(url,datapath, quiet = False)

# Apertura 
# r : modo lectura; w : modo escritura; a : modo de escritura append
file = open(datapath, "r") 

# Nombre del archivo
file.name

# Modo en el que se encuentra
file.mode

# Ver si esta cerrado
file.close

# Cerrar el archivo
file.close()

# Leer el contenido
fileContent = file.read()
fileContent

# Leer por lineas y abrir con la sentencia with, la cual realiza el cierre del archivo de forma automática
with open(datapath,"r") as file1:
        i = 0;
        for line in file1:
            print("Iteration", str(i), ": ", line)
            i = i + 1;

# Escribir una linea 
with open('test_escritura.txt', 'w') as writefile:
    writefile.write("linea A\n") # escribe una línea de texto en el archivo indicado sin incluir el salto de línea (por eso lo agregamos)