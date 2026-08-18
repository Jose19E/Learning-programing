def usuario():    
     usuario = input("Ingrese su Nombre:")
     return usuario

def nota1():
     nota1=float(input("Ingrese su primera nota:"))
     return nota1

def nota2():
     nota2=float(input("Ingrese su segunda nota:"))
     return nota2

def nota3():
     nota3=float(input("Ingrese su tercera nota:"))
     return nota3

def promedio(nota1,nota2,nota3):
     promedio= (nota1 + nota2 + nota3 ) / 3
     return promedio

def estado(promedio):
     if promedio >= 3:
          return "Aprobo"
     else:
          return "Reprobo"

def mostrar_datos(usuario, nota1, nota2, nota3, promedio, estado):
     print("Usuario:", usuario)
     print("Nota 1:",nota1)
     print("Nota 2:",nota2)
     print("Nota 3:", nota3)
     print("Promedio:", promedio)
     print("Estado:", estado)

nombre = usuario()
n1 = nota1()
n2 = nota2()
n3 = nota3()

prom = promedio(n1, n2, n3)
resultado = estado(prom)

mostrar_datos(nombre, n1, n2, n3, prom, resultado)




        










