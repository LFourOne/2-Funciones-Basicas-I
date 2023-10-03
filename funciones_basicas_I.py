#1
def number_of_food_groups():
    return 5                                # Va a retornar el número 5 y este será impreso en la linea 4 
print(number_of_food_groups())

"""
#2
def number_of_military_branches():
    return 5
print(number_of_days_in_a_week_silicon_or_triangle_sides() + number_of_military_branches())#Una función no está definida, por lo tanto no se puede ejecutar.

"""

#3
def number_of_books_on_hold():
    return 5
    return 10                        # Solo retornará el número 5, porque return termina la función y devuelve los valores establecidos hasta esa linea. 
print(number_of_books_on_hold())


#4
def number_of_fingers():
    return 5                                 # Lo mismo de arriba.
    print(10)
print(number_of_fingers())


#5
def number_of_great_lakes():
    print(5)                                 # Supongo que dará imprimirá 5 y luego indefido, no hay valor dentro de ese parentesis.
x = number_of_great_lakes()
print(x)

"""
#6
def add(b,c):
    print(b+c)                               # Al principio pensé que haría un print del número 8, pero me di cuenta que no existe un return 
print(add(1,2) + add(2,3))

"""

#7
def concatenate(b,c):
    return str(b)+str(c)                     # Aquí suma dos strings (creo que se les dice así), por lo tanto será 25.
print(concatenate(2,5))


#8
def number_of_oceans_or_fingers_or_continents():
    b = 100
    print(b)
    if b < 10:   
        return 5                            # Aquí por la linea 45 imprimirá 100, y luego en la linea 49 al no cumplirse la 47, imprimirá 10, por lo tanto 100 y 10
    else:
        return 10
    return 7
print(number_of_oceans_or_fingers_or_continents())

#9
def number_of_days_in_a_week_silicon_or_triangle_sides(b,c):
    if b<c:
        return 7
    else:
        return 14
    return 3
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3)) # Imprimirá 7
print(number_of_days_in_a_week_silicon_or_triangle_sides(5,3)) # Imprimirá 14
print(number_of_days_in_a_week_silicon_or_triangle_sides(2,3) + number_of_days_in_a_week_silicon_or_triangle_sides(5,3)) # Imprimirá 21


#10
def addition(b,c):
    return b+c          # Imprimirá 8
    return 10
print(addition(3,5))


#11
b = 500
print(b)        # Imprimirá 500 - 1
def foobar():
    b = 300
    print(b)    # Imprimirá 300 - 3
print(b)        # Imprimirá 500 - 2
foobar()
print(b)        # Imprimirá 500 - 4


#12
b = 500
print(b)       # Imprimirá 500 - 1
def foobar():
    b = 300
    print(b)   # Imprimirá 300 - 3
    return b   # Retorna b = 300 - 4
print(b)       # Imprimirá 500 - 2
foobar()
print(b)       # Imprimirá 300 - 5


#13
b = 500
print(b)     # Imprimirá 500 - 1
def foobar():
    b = 300
    print(b) # Imprimirá 300 - 3
    return b # Retorna b = 300 - 4
print(b)    # Imprimirá 500 - 2
b=foobar()  
print(b)    # Imprimirá 300 - 5


#14
def foo():
    print(1) # Imprime 1 - 2
    bar()    # Llama a la función bar(), pero según yo primero terminará de leer todo lo de la primera función - 3
    print(2) # Imprime 2 - 4   
def bar():   # Ahora toma la función - 5
    print(3) # Imprime 3 - 6                                    # Al final se imprime primero la segunda función que se llamó dentro de la primera, luego de terminar ->
foo() # Se llama a la función - 1                               # -> su bucle vuelve a ejecutarse las siguientes lineas de la primera función.


#15
def foo():
    print(1) # Se imprime 1 - 1
    x = bar() # Se llama y se ejecuta la función bar - 2 # Al retornar, x = bar(5) - 5
    print(x) # Se imprime 5 - 6
    return 10 # Retorna 10 - 7
def bar():
    print(3) # Imprime 3 - 3
    return 5 # Retorna con valor 5 - 4 
y = foo() # y = foo(10) - 8
print(y) # Imprime 10 - 9       ### En total se imprime = 1, 3 , 5, 10 ###
