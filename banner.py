#!/usr/bin/python3
import sys
sys.stdout.reconfigure(encoding='utf-8')
#A continuacion se muestran los diccionarios utilizados para formar las palabras del banner.
diccionario1= {'a':"        ",'b':"        ",'c':"        ",'d':"        ",'e':"        ",'f':"        ",'g':"        ",'h':"        ",'i':"        ",'j':"        ",'k':"        ",'l':"        ",'m':"        ",'n':"        ",'o':"        ",'p':"        ",'q':"        ",'r':"        ",'s':"        ",'t':"        ",'u':"        ",'v':"        ",'w':"        ",'x':"        ",'y':"        ",'z':"        ",'A':"    A   ",'B':" BBBBBB ",'C':"  CCCCC ",'D':" DDDDDD ",'E':" EEEEEEE",'F':" FFFFFFF",'G':"  GGGGG ",'H':" H     H",'I':"   III  ",'J':"       J",'K':" K    K ",'L':" L      ",'M':" M     M",'N':" N     N",'O':"  OOOOO ",'P':" PPPPPP ",'Q':"  QQQQQ ",'R':" RRRRRR ",'S':"  SSSSS ",'T':" TTTTTTT",'U':" U     U",'V':" V     V",'W':" W     W",'X':" X     X",'Y':" Y     Y",'Z':" ZZZZZZZ",'?':"  ????? ",'¿':"    °   ",'0':"  00000 ",'1':"   11   ",'2':"  22222 ",'3':"  33333 ",'4':"      4 ",'5': " 5555555",'6':"  666666",'7':" 7777777",'8':"  88888 ",'9':" 999999 ",' ':"        ",'.':"        ",',':"        "}
diccionario2= {'a':"   aa   ",'b':" bbbbb  ",'c':"  cccc  ",'d':" ddddd  ",'e':" eeeeee ",'f':" ffffff ",'g':"  gggg  ",'h':" h    h ",'i':"   °    ",'j':"      j ",'k':" k    k ",'l':" l      ",'m':" m    m ",'n':" n    n ",'o':"  oooo  ",'p':" ppppp  ",'q':"  qqqq  ",'r':" rrrrr  ",'s':"  ssss  ",'t':"  ttttt ",'u':" u    u ",'v':" v    v ",'w':" w    w ",'x':" x    x ",'y':" y   y  ",'z':" zzzzzz ",'A':"   A A  ",'B':" B     B",'C':" C     C",'D':" D     D",'E':" E      ",'F':" F      ",'G':" G     G",'H':" H     H",'I':"    I   ",'J':"       J",'K':" K   K  ",'L':" L      ",'M':" MM   MM",'N':" NN    N",'O':" O     O",'P':" P     P",'Q':" Q     Q",'R':" R     R",'S':" S     S",'T':"    T   ",'U':" U     U",'V':" V     V",'W':" W     W",'X':"  X   X ",'Y':"  Y   Y ",'Z':"      Z ",'?':" ?     ?",'¿':"    ¿   ",'0':" 0     0",'1':"  111   ",'2':" 22   22",'3':" 3     3",'4':"     44 ",'5': " 55     ",'6':" 66   66",'7':"      7 ",'8':" 88   88",'9':"99    99",' ':"        ",'.':"        ",',':"        "}
diccionario3= {'a':"  a  a  ",'b':" b    b ",'c':" c    c ",'d':" d    d ",'e':" e      ",'f':" f      ",'g':" g    g ",'h':" h    h ",'i':"   i    ",'j':"      j ",'k':" k   k  ",'l':" l      ",'m':" mm  mm ",'n':" nn   n ",'o':" o    o ",'p':" p    p ",'q':" q    q ",'r':" r    r ",'s':" s      ",'t':"    t   ",'u':" u    u ",'v':" v    v ",'w':" w    w ",'x':"  x  x  ",'y':"  y y   ",'z':"     z  ",'A':"  A   A ",'B':" B     B",'C':" C      ",'D':" D     D",'E':" E      ",'F':" F      ",'G':" G      ",'H':" H     H",'I':"    I   ",'J':"       J",'K':" K  K   ",'L':" L      ",'M':" M M M M",'N':" N N   N",'O':" O     O",'P':" P     P",'Q':" Q     Q",'R':" R     R",'S':" S      ",'T':"    T   ",'U':" U     U",'V':" V     V",'W':" W     W",'X':"   X X  ",'Y':"   Y Y  ",'Z':"     Z  ",'?':"       ?",'¿':"    ¿   ",'0':" 0     0",'1':"   11   ",'2':"     22 ",'3':"       3",'4':"    4 4 ",'5': " 55     ",'6':" 66     ",'7':"     7  ",'8':" 88   88",'9':"99    99",' ':"        ",'.':"        ",',':"        "}
diccionario4= {'a':" a    a ",'b':" bbbbb  ",'c':" c      ",'d':" d    d ",'e':" eeeee  ",'f':" fffff  ",'g':" g      ",'h':" hhhhhh ",'i':"   i    ",'j':"      j ",'k':" kkkk   ",'l':" l      ",'m':" m mm m ",'n':" n n  n ",'o':" o    o ",'p':" p    p ",'q':" q    q ",'r':" r    r ",'s':"  ssss  ",'t':"    t   ",'u':" u    u ",'v':" v    v ",'w':" w    w ",'x':"   xx   ",'y':"   y    ",'z':"    z   ",'A':" A     A",'B':" BBBBBB ",'C':" C      ",'D':" D     D",'E':" EEEEEE ",'F':" FFFFFF ",'G':" G  GGGG",'H':" HHHHHHH",'I':"    I   ",'J':"       J",'K':" KKK    ",'L':" L      ",'M':" M  M  M",'N':" N  N  N",'O':" O     O",'P':" PPPPPP ",'Q':" Q     Q",'R':" RRRRRR ",'S':"  SSSSS ",'T':"    T   ",'U':" U     U",'V':" V     V",'W':" W     W",'X':"    X   ",'Y':"    Y   ",'Z':"    Z   ",'?':"    ??? ",'¿':"  ¿¿¿   ",'0':" 0     0",'1':"   11   ",'2':"    22  ",'3':"   3333 ",'4':"   4  4 ",'5': " 555555 ",'6':" 666666 ",'7':"    7   ",'8':" 8888888",'9':" 9999999",' ':"        ",'.':"        ",',':"        "}
diccionario5= {'a':" aaaaaa ",'b':" b    b ",'c':" c      ",'d':" d    d ",'e':" e      ",'f':" f      ",'g':" g  ggg ",'h':" h    h ",'i':"   i    ",'j':"      j ",'k':" k  k   ",'l':" l      ",'m':" m    m ",'n':" n  n n ",'o':" o    o ",'p':" ppppp  ",'q':" q  q q ",'r':" rrrrr  ",'s':"      s ",'t':"    t   ",'u':" u    u ",'v':" v    v ",'w':" w ww w ",'x':"   xx   ",'y':"   y    ",'z':"   z    ",'A':" AAAAAAA",'B':" B     B",'C':" C      ",'D':" D     D",'E':" E      ",'F':" F      ",'G':" G     G",'H':" H     H",'I':"    I   ",'J':" J     J",'K':" K  K   ",'L':" L      ",'M':" M     M",'N':" N   N N",'O':" O     O",'P':" P      ",'Q':" Q   Q Q",'R':" R   R  ",'S':"       S",'T':"    T   ",'U':" U     U",'V':"  V   V ",'W':" W  W  W",'X':"   X X  ",'Y':"    Y   ",'Z':"   Z    ",'?':"    ?   ",'¿':" ¿      ",'0':" 0     0",'1':"   11   ",'2':"   22   ",'3':"       3",'4':" 4444444",'5': "       5",'6':" 66   66",'7':"   7    ",'8':" 88   88",'9':"      99",' ':"        ",'.':"        ",',':"        "}
diccionario6= {'a':" a    a ",'b':" b    b ",'c':" c    c ",'d':" d    d ",'e':" e      ",'f':" f      ",'g':" g    g ",'h':" h    h ",'i':"   i    ",'j':" j    j ",'k':" k   k  ",'l':" l      ",'m':" m    m ",'n':" n   nn ",'o':" o    o ",'p':" p      ",'q':" q   q  ",'r':" r   r  ",'s':" s    s ",'t':"    t   ",'u':" u    u ",'v':"  v  v  ",'w':" ww  ww ",'x':"  x  x  ",'y':"   y    ",'z':"  z     ",'A':" A     A",'B':" B     B",'C':" C     C",'D':" D     D",'E':" E      ",'F':" F      ",'G':" G     G",'H':" H     H",'I':"    I   ",'J':" J     J",'K':" K   K  ",'L':" L      ",'M':" M     M",'N':" N    NN",'O':" O     O",'P':" P      ",'Q':" Q    QQ",'R':" R    R ",'S':" S     S",'T':"    T   ",'U':" U     U",'V':"   V V  ",'W':" W  W  W",'X':"  X   X ",'Y':"    Y   ",'Z':"  Z     ",'?':"    ?   ",'¿':" ¿     ¿",'0':" 0     0",'1':"   11   ",'2':"  22   2",'3':" 3     3",'4':"      4 ",'5': "       5",'6':" 66   66",'7':"  7     ",'8':" 88   88",'9':"99    99",' ':"        ",'.':"##      ",',':"  #     "}
diccionario7= {'a':" a    a ",'b':" bbbbb  ",'c':"  cccc  ",'d':" ddddd  ",'e':" eeeeee ",'f':" f      ",'g':"  gggg  ",'h':" h    h ",'i':" iiiii  ",'j':"  jjjj  ",'k':" k    k ",'l':" llllll ",'m':" m    m ",'n':" n    n ",'o':"  oooo  ",'p':" p      ",'q':"  qqq q ",'r':" r    r ",'s':"  ssss  ",'t':"    t   ",'u':"  uuuu  ",'v':"   vv   ",'w':" w    w ",'x':" x    x ",'y':"   y    ",'z':" zzzzzz ",'A':" A     A",'B':" BBBBBB ",'C':"  CCCCC ",'D':" DDDDDD ",'E':" EEEEEEE",'F':" F      ",'G':"  GGGGG ",'H':" H     H",'I':"   III  ",'J':"  JJJJJ ",'K':" K    K ",'L':" LLLLLLL",'M':" M     M",'N':" N     N",'O':"  OOOOO ",'P':" P      ",'Q':"  QQQQ Q",'R':" R     R",'S':"  SSSSS ",'T':"    T   ",'U':"  UUUUU ",'V':"    V   ",'W':"  WW WW ",'X':" X     X",'Y':"    Y   ",'Z':" ZZZZZZZ",'?':"    °   ",'¿':"  ¿¿¿¿¿ ",'0':"  00000 ",'1':" 111111 ",'2':" 2222222",'3':"  333333",'4':"      4 ",'5': " 555555 ",'6':"  66666 ",'7':" 7      ",'8':"  88888 ",'9':" 999999 ",' ':"        ",'.':"##      ",',':" #      "}
#Aqui tenemos a Tux, la mascota de Linux esperando pacientemente, que corras este espectacular programa. 
print("                  .88888888:.              ")
print("                88888888.88888.            ")
print("              .8888888888888888.           ") 
print("              888888888888888888           ") 
print("              88' _`88'_  `88888           ")
print("              88 88 88 88  88888           ")
print("              88_88_::_88_:88888           ") 
print("              88:::,::,:::::8888           ")
print("              88`:::::::::'`8888           ")
print("             .88  `::::'    8:88.          ")
print("            8888            `8:888.        ")
print("          .8888'             `888888.      ")
print("         .8888:..  .::.  ...:'8888888:.    ")
print("        .8888.'     :'     `'::`88:88888   ")
print("       .8888        '         `.888:8888.  ")
print("      888:8         .           888:88888  ")
print("    .888:88        .:           888:88888: ")
print("    8888888.       ::           88:888888  ")
print("    `.::.888.      ::          .88888888   ")
print("   .::::::.888.    ::         :::`8888'.:. ")
print("  ::::::::::.888   '         .:::::::::::: ")
print("  ::::::::::::.8    '      .:8::::::::::::.")
print(" .::::::::::::::.        .:888:::::::::::::")
print(" :::::::::::::::88:.__..:88888:::::::::::' ")
print("  `'.:::::::::::88888888888.88:::::::::'   ")
print("       `':::_:' -- '' -'-' `':_::::'`      ")
#Este comando permite interactuar con el programa a traves de la consola, de manera que uno introduzca la palabra deseada.
palabra = input("Ingresar palabra u oración: ")[0:10]
#En estas listas se almacenaran las letras.
lista1=[]
lista2=[]
lista3=[]
lista4=[]
lista5=[]
lista6=[]
lista7=[]
#Con este comando se recorrera cada palabra letra por letra.
for letra in palabra:
#Luego se procede a agregar cada parte de las letras en su respectivas listas.
	lista1.append(diccionario1[letra])
	lista2.append(diccionario2[letra])
	lista3.append(diccionario3[letra])
	lista4.append(diccionario4[letra])
	lista5.append(diccionario5[letra])
	lista6.append(diccionario6[letra])
	lista7.append(diccionario7[letra])
#Luego se utiliza el comando join para convertir los elementos de cada lista en una cadena.
lista1=''.join(lista1)
lista2=''.join(lista2)
lista3=''.join(lista3)
lista4=''.join(lista4)
lista5=''.join(lista5)
lista6=''.join(lista6)
lista7=''.join(lista7)
#Posteriormente de ingresar la palabra, podremos elegir entre 6 tipos diferentes de decoraciones, los cuales se eligen marcando un numero natural del 1 al 6,  
decoracion = input("Tipo de decoración (marcar un numero del 1 al 6): ")
largo_palabra=len(palabra)
#Aqui se definen los diseños de cada decoracion, en los que la variable largo_palabra influye en el largo de la decoracion para mejorar la apariencia de los diseños.  
decoracion_sup_inf={'1':(2+(largo_palabra))*"*-*--*-*",'2':(2+(largo_palabra))*"#-#--#-#",'3':(2+(largo_palabra))*"$-$--$-$",'3':(2+(largo_palabra))*"$-$--$-$"
,'4':(2+(largo_palabra))*"<><><><>",'5':(2+(largo_palabra))*"°°-°°-°°",'6':(2+(largo_palabra))*"+*-*+*-*"}
decoracion_izq={'1':"*-*-*   ",'2':"#-#-#   " ,'3':"$-$-$   ",'4':"<----   ",'5':"°_°_°   " ,'6':"+-+-+   "}
decoracion_der={'1':"   *-*-*",'2':"   #-#-#" ,'3':"   $-$-$",'4':"   ---->",'5':"   °_°_°" ,'6':"   +-+-+"}
# Esta variable permitira generar un espacio en blanco necesario para la optima vizualizacion del diseño.
espacio=" "
#Luego de elegir la palabra, el diseño, se procede a elegir el color con el que contara el banner.
numero = input("Color (marcar un numero del 1 al 7): ")
color ={'1':"[0;31m",'2':"[0;32m",'3':"[0;33m",'4':"[0;34m",'5':"[0;35m",'6':"[0;36m",'7':"[0;37m"}
#Este comando permite configurar el color del banner, segun la eleccion marcada anteriormente. Estas lineas se generara la parte superior del adorno deseado.
print(chr(27)+color[numero]+decoracion_sup_inf[decoracion])
print(chr(27)+color[numero]+decoracion_sup_inf[decoracion])
print(chr(27)+color[numero]+decoracion_sup_inf[decoracion])

print(chr(27)+color[numero]+decoracion_izq[decoracion]+(largo_palabra*8)*espacio+decoracion_der[decoracion])
print(chr(27)+color[numero]+decoracion_izq[decoracion]+(largo_palabra*8)*espacio+decoracion_der[decoracion])
#Luego se imprimen las decoraciones laterales y la palabra introducida al comienzo en el medio del adorno.
print (decoracion_izq[decoracion]+lista1+decoracion_der[decoracion])
print (decoracion_izq[decoracion]+lista2+decoracion_der[decoracion])
print (decoracion_izq[decoracion]+lista3+decoracion_der[decoracion])
print (decoracion_izq[decoracion]+lista4+decoracion_der[decoracion])
print (decoracion_izq[decoracion]+lista5+decoracion_der[decoracion])
print (decoracion_izq[decoracion]+lista6+decoracion_der[decoracion])
print (decoracion_izq[decoracion]+lista7+decoracion_der[decoracion])
#Finalmente se imprimira la parte inferior de la decoracion.
print(chr(27)+color[numero]+decoracion_izq[decoracion]+(largo_palabra*8)*espacio+decoracion_der[decoracion])
print(chr(27)+color[numero]+decoracion_izq[decoracion]+(largo_palabra*8)*espacio+decoracion_der[decoracion])

print(chr(27)+color[numero]+decoracion_sup_inf[decoracion])
print(chr(27)+color[numero]+decoracion_sup_inf[decoracion])
print(chr(27)+color[numero]+decoracion_sup_inf[decoracion])
