#Menu.py - todo junto

#----------------------------[Códigos]---------------------------------------
def Hola_mundo():#Decir Hola Mundo

  print('Hola mundo')

def Tabla_7(): #Enseñar tabla 7
  
  print("\nTabla del 7\n")
  i = 0
  while i < 71:
    print(i)
    i += 7

def Tablas(): #Tablas del 1 al 10


  for i in range (11):
    print("\n")
    print("Tabla:",i)
    print("\n")
    for j in range (11):
      print(i,"*",j,"=",i*j)
      j += 1

def Adivina():#Adivina num. 1 - 100
    
  import random

  def adivina_num():
    numero_secreto = random.randint(0, 100)
    intentos = 0

    print("Bienvenido a Adivina el Número")
    print("Adivina el número entre 1 y 100")

    while intentos < 5:
     intento = int(input("Adivina el número: "))
     intentos += 1
     if intento < int(numero_secreto):
       print("El número es mayor")
     elif intento > int(numero_secreto):
       print("El número es menor")
     elif intento == numero_secreto:
      print("¡Felicidades! Has ganado. Lo has conseguido en:",intentos)
      h=input("pulsa enter para continuar")
      break
    if intento != numero_secreto:
     print("Has perdido. El número era:",numero_secreto)

  adivina_num()
  
def Ordena():#Ordena 3 numeros
  while 1:
    try:

        numero1= int(input("ingrese 3 números diferentes: "))
        numero2= int(input("ingrese otro número más que sea diferente: "))
        numero3= int(input("ingrese 1 último número diferente: "))


        if numero1 > numero2:
            if numero2>numero3:
                print("Los números de mayor a menor son: ",numero3, numero2, numero1)
            elif numero1>numero3:
                print("Los números de mayor a menor son: ",numero2, numero3, numero1)
            else:
                print("Los números de mayor a menor son: ",numero2, numero1, numero3)    
        else:
            if numero1>numero3:
                print("Los númerosde mayor a menor son: ",numero3, numero1, numero2)

            elif numero2>numero3:
                print("Los números de mayor a menor son: ",numero1, numero3, numero2)       
            else:
                print("Los números de mayor a menor son: ",numero1, numero2, numero3)
        return()                    
    except ValueError:
        print("Debe ingresar un número de tipo entero")

def Ordena_100(): #Ordena 100 numeros

  import random

  # Generate 100 random numbers between 1 and 5000
  random_numbers = [random.randint(1, 5000) for _ in range(100)]

  # Sort the list of numbers
  random_numbers.sort()

  # Print the sorted numbers
  print(random_numbers)

def Rad_Circunferencia():

      l = int(input("Introduzca el perímeto de su circunferéncia: ")

      r = l/2*3.1416

      print("El radio de su circunferéncia es:", r)
  
# ------------------------------[Principal]----------------------------------
while True: #Función principal 
  
  print ("""
    Menú

  1- Hola_mundo
  2- Tabla_7
  3- Tablas
  4- Adivina
  5- Ordena
  6- Ordena_100
  7- Rad_Circunferencia
  8- Salir menú

    Selecciona opción """)
  import os
  # Limpiar la pantalla al finalizar
  
  n = int(input())
  if n==1:
    print()
    Hola_mundo()
    print()
    input("Presione enter para continuar al menú")
    os.system('clear')
  elif n==2:
    print()
    Tabla_7()
    print()
    input("Presione enter para continuar al menú")
    os.system('clear')
  elif n==3:
    print()
    Tablas()
    print()
    input("Presione enter para continuar al menú")
    os.system('clear')
  elif n==4:
    print()
    Adivina()
    print()
    input("Presione enter para continuar al menú")
    os.system('clear')
  elif n==5:
    print()
    Ordena()
    print()
    input("Presione enter para continuar al menú")
    os.system('clear')
  elif n==6:
    print()
    Ordena_100()
    print()
    input("Presione enter para continuar al menú")
    os.system('clear')
  elif n==7:
    print()
    print("Hasta la próxima")
    print()
    input("Presione enter para continuar al menú")
  elif n==8:
    print()
    print("Hasta la próxima ;)")
    print()
    input("Presione enter para continuar al menú")
    break
  else:
    print("Elige un número del menú")
