#CREAMOS UNA CLASE LLAMADA CALCULO
from ast import Num
from pickle import TRUE
from tkinter import N

class calculo:
    def __init__(self):
        self

    def factorial(self):
        self.num1=int(input("Numero: "))
        factorial=1
        if self.num1!=0:
            for i in range (1,self.num1+1):
                factorial=factorial+1
        print("Factorial: ", factorial)

    def suma (self):
        self.num2=int(input("Ingrese el valor final: "))
        b=0
        for i in range(1, self.num2+1):
            print(i)
            b=b+1 
        print("La suma es: ", b)
    
    def primalidad(self, num):
        self.num3=int(input("Ingrese un numero entero para saber si es primo o no: "))
        self.num3=num
        def primo(num):
            for i in range(2, num):
                if num%i == 0:
                    return False
            return True
        print(primo(num))
    
    def multiplicacion(self):
        def tabla(n1, n2):
            return str(n1) + " * " + str(n2) + " = " + str(n1+n2)
        self.num4=int(input("Ingrese un numero para sacar su tabla: "))
        for i in range(0,13):
            print(tabla(self.num4, i))