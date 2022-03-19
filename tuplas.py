#declarar tupla
mi_tupla = ()
mi_tupla = (1,2,3)

#generar una tupla de 1 solo valor (Obligatorio la ,)
mi_tupla = (1,)

#acceder a un indice de la tupla
mi_tupla = (1,2,3)
mi_tupla[0] #1
mi_tupla[1] #2
mi_tupla[2] #3

#reasignar una tupla
mi_tupla = (1,2,3)
mi_otra_tupla = (4,5,6)
mi_tupla =+ mi_otra_tupla

#metodos de las tuplas
mi_tupla = (1,1,1,2,2,3)
mi_tupla.count(1) #3	el numero 1 aparece 3 veces en la tupla
mi_tupla.index(3) #5	indice de la primera instancia donde se encuentra un elemento
mi_tupla.index(1) #0
mi_tupla.index(2) #3