## Mi primer script en Python
## Daniel Rojas S
print("Hola Mundo!!")

## essentials of Python

x = 100

while x > 5 :
    print(x)
    x = x/4
 
## 😊 Any number of labels (or variables) can refer to the same object, 
#  and when that object changes, the value referred to by 
# all of those variables also changes.

a = [1, 2, 3]
b = a
c = b

b[2] = 10

print(a,b,c)

# 😃 Mira que pasa cuando son constantes

a = 1
b = a
c = b

b = 3

print(a, b, c)

## ✌️ Borrar una variable

a = "Hola Mundo"
print(a)

del a
print(a)


## Strings

a = "\t Vladimir es un perro pequeño"
print(a)

b = "El PRI es corrupto (\\)"
print(b)

c = "Este es un mensaje para tania y Rocio \"Te amo\""
print(c)


mensaje = """ Este es un mensaje a todos los humanos, "Dejen de morir" xd """
print(mensaje)

