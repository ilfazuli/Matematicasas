#Para las suceciones Podemos hacer un calcula asi
#Sabiendo la diferencia de las suceciones
# Con ciclo while
n = 1 #Nuestra pocision
termino = 45 # Termino de inicio
d =20 # Diferencia

while n < 900: #Aqui el termino que buscamos es el termino 900
    n =+1
    termino = termino + d
print(termino)

#Con ciclo For 
for n in range(2,901): #Aqui el termino que buscamos es el termino 900 aqui se le da 1 numero demas por como funciona el for 
    termino = termino +d
print(termino)


#Ejemple: Una casa se arrienda por 2 anos, considerando que durante este periodo el arriendo se incrementar a todos 
#los meses en una cantidad constante. Si el quinto mes de arriendo se pagara $204.000 y el decimo tercer
#mes $252.000, ¿cual seria el valor del arriendo del primer y ultimo mes?

n = 13
termino = 252000
d = 6000

for n in range(14,25):
    termino = termino + d

print(termino)

#La altura de un arbol de r ´ apido crecimiento aumenta cada a ´ no a una raz ˜ on constante. Si en el segundo a ´ no˜
#tiene una altura de 1,125 metros y el quinto ano mide exactamente ˜ 3,796875 metros. ¿Cuantos metros de ´
#altura aproximadamente, tendra el ´ arbol al noveno a ´ no? (aproxime el resultado a la cent ˜ esima).

n=2
termino = 1.125
r= 1.5

for n in range(3,10):
    termino =termino * r
print(round(termino,2))
