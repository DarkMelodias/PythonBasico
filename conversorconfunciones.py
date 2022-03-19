# def suma(a,b):
#     print('Se suma dos numeros')
#     resultado = a+b
#     return resultado

# sumatoria = suma(1,4)

# print(sumatoria)

def conversor(tipo_pesos, valor_dolar):
    pesos = input("¿Cuantos pesos "+tipo_pesos+ " tienes?:")
    pesos = float(pesos)
    dolares = pesos/valor_dolar
    dolares = round(dolares , 2)
    dolares = str(dolares)
    print("Tienes $"+dolares+" dolares")

#convierte pesos mexicanos, argentinos y colombianos a dólares


# """ """ permite crear strings multilineas

menu = """
Bienvenido al conversor de monedas 💰

1-Pesos Mexicanos
2-Pesos Colombianos
3-Pesos Argentinos

Elige una opción: 

"""

# de derecha a izquierda: llamo a la funcion input, le paso la variable menu para que la imprima y reciba el número que el usuario escogió, lo convierto a int y lo guardo en la variable 'opcion'
opcion = int(input(menu))

if opcion == 1: #pesos mexicanos
    conversor("mexicanos",24)
elif opcion == 2: #pesos colombianos
	
    conversor("colombianos",3875)
elif opcion == 3: #pesos argentinos
    conversor("argentinos",65)
else:  #el usuario escribió algo diferente
	print('Escribe una opción correcta: ')
