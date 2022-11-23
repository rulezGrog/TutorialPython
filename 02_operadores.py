### Operadores Aritméticos ###

print(3 + 4)
print(3 - 4)
print(3 * 4)
print(3 / 4)
print(10 % 3)
print(10 / 3)
print(10 // 3) # floor division (redondeo)
print(2 ** 3)  # exponenete, 2 elevado a 3

print("Hola " + "Python " + "¿Qué tal?")
print("Hola " + str(5))
print("Hola " * 5)
print("Hola " * (2 ** 3))

my_float = 2.5 * 2
print("Hola " * int(my_float))

### Operadores Comparativos ###

print(3 > 4)
print(3 < 4)
print(3 >= 4)
print(4 <= 4)
print(3 == 4)
print(3 != 4)

print("\n")

print("Hola" > "Python")
print("Hola" < "Python")
print("Hola" >= "Python")
print("Hola" <= "Python")
print("Hola" == "Lola") # Comprueba una ordenación alabética por ASCII
print("aaaa" <= "abaa") # Comprueba una ordenación alfabética por ASCII
print(len("Hola") == len("Lola")) # Cuenta caracteres
print("Hola" != "Python")
print("\n")

### Operadores Lógicos ###

print(3 > 4 and "Hola" > "Python")
print(3 > 4 or "Hola" > "Python")
print(3 < 4 and "Hola" < "Python")
print(3 < 4 or "Hola" > "Python")
print(3 < 4 or "Hola" > "Python" and 4 == 4)
print(not(3 > 4))