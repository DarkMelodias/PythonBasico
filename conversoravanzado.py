#convierte pesos mexicanos, argentinos y colombianos a d贸lares

# """ """ permite crear strings multilineas
menu = """
Bienvenido al conversor de monedas 馃挵

1-Pesos Mexicanos
2-Pesos Colombianos
3-Pesos Argentinos

Elige una opci贸n: 

"""
# de derecha a izquierda: llamo a la funcion input, le paso la variable menu para que la imprima y reciba el n煤mero que el usuario escogi贸, lo convierto a int y lo guardo en la variable 'opcion'
opcion = int(input(menu))

if opcion == 1: #pesos mexicanos
	#pregunto al usuario la cantidad a convertir
	pesos = input('驴Cu谩ntos pesos mexicanos tienes?: ')
	#convierto a float para mejor manejo de datos
	pesos = float(pesos)
	#escribo el valor del dolar en pesos mexicanos
	tipo_de_cambio = 21.5
elif opcion == 2: #pesos colombianos
	#pregunto al usuario la cantidad a convertir
	pesos = input('驴Cu谩ntos pesos colombianos tienes?: ')
	#convierto a float para mejor manejo de datos
	pesos = float(pesos)
	#escribo el valor del dolar en pesos colombianos
	tipo_de_cambio = 3715.01
elif opcion == 3: #pesos argentinos
	#pregunto al usuario la cantidad a convertir
	pesos = input('驴Cu谩ntos pesos argentinos tienes?: ')
	#convierto a float para mejor manejo de datos
	pesos = float(pesos)
	#escribo el valor del dolar en pesos argentinos
	tipo_de_cambio = 74.44
else:  #el usuario escribi贸 algo diferente
	print('Escribe una opci贸n correcta: ')

#hago la conversi贸n
dolares = pesos / tipo_de_cambio
#redondeo los d贸lares a dos decimales
dolares = round(dolares, 2)
#convierto el float de dolares a un string
dolares = str(dolares)

#imprimo el valor de la conversion. Se pueden sumar (concatenar) strings con '+'
print('Tienes $' + dolares +' d贸lares')

