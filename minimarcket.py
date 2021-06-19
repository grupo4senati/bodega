def PRODUCTOSDELIMPIEZA(total):
    while True:
        print("""|------------------------------|
|   PRODUCTOS DE LIMPIEZA      |
|----------------------------- |       
| A |LEJIA             |S/2.50 |   
| B |SUAVIZANTE        |S/2.00 |
| C |JABON BOLIVAR     |S/2.50 |
| D |DETERGENTE SAPOLIO|S/4.00 | 
| E |---------SALIR -----------|
|------------------------------|""")
        opa=input("|OPCION:..:").upper()
        if opa=="A":
            total+=2.5
        elif opa=="B":
            total+=2
        elif opa=="C":
            total+=2.5
        elif opa=="D":
            total+=4
        elif opa=="E":
            break
        else:
            print("OPCION INCORRECTA")
    return total
def ABARROTES(total):
    while True:
        print("""
|          ABARROTES             |
|--------------------------------|   
| A |ARROZ COSTEÑO 1KG   |S/4.50 |  
| B |FIDEO MOLITALIA     |S/4.00 |
| C |AZUCAR COSTEÑO 1KG  |S/3.00 |
| D |HARINA MOLITALIA 1KG|S/4.50 |
| E |-----------SALIR -----------|
|--------------------------------|""")
        opb=input("|OPCION:..:").upper()
        if opb=="A":
            total+=4.5
        elif opb=="B":
            total+=4
        elif opb=="C":
            total+=3
        elif opb=="D":
            total+=4.5
        elif opb=="E":
            break
        else:
            print("OPCION INCORRECTA")
    return total
def POLLOCARNESPESCADOS(total):
    while True:
        print("""|=================================|
|   POLLO / CARNES / PESCADOS     |  
|=================================|
| A |POLLO ENTERO EL KILO|S/9.50  |  
| B |FILETE DE POLLO     |S/7.50  |
| C |MENUDENCIA          |S/6.00  |
| D |FILETE DE PERICO    |S/6.00  |  
| E |BONITO ENTERO       |S/6.50  |
| F |BIFE DE VACIO       |S/43.00 |
| G |ENTRAÑA FINA        |S/53.00 |
| H |============= SALIR =========|
|=================================|""")
        opc=input("|OPCION:..:").upper()
        if opc=="A":
            total+=9.5
        elif opc=="B":
            total+=7.5
        elif opc=="C":
            total+=6
        elif opc=="D":
            total+=6
        elif opc=="E":
            total+=6.5
        elif opc=="F":
            total+=43
        elif opc=="G":
            total+=53
        elif opc=="H":
            break
        else:
            print("OPCION INCORRECTA")
    return total
def BEBIDAS(total):
    while True:
        print("""|=====================================|
|             BEBIDAS                 |  
|=====================================|
| A |AGUA CIELO DE 5 LITROS |S/6.50   |  
| B |COCA COLA DE 3 LITROS  |S/11.50  |
| C |INKA KOLA DE 3 LITROS  |S/11.00  |
| D |GATORED                |S/3.00   |  
| E |PILSEN                 |S/6.50   |
| F |CORONA                 |S/23.00  |
| G |CUZQUEÑA               |S/25.00  |
| H |CRISTAL                |S/6.00   |
| I |============= SALIR =============|
|=====================================|""")
        opc=input("|OPCION:..:").upper()
        if opc=="A":
            total+=6.5
        elif opc=="B":
            total+=11.5
        elif opc=="C":
            total+=11
        elif opc=="D":
            total+=3
        elif opc=="E":
            total+=6.5
        elif opc=="F":
            total+=23
        elif opc=="G":
            total+=25
        elif opc=="H":
            total+=6
        elif opc=="I":
            break
        else:
            print("OPCION INCORRECTA")
    return total
def FRUTASYVERDURAS(total):
    while True:
        print("""|=====================================|
|           FRUTAS Y VERDURAS         |  
|=====================================|
| A |MANZANA EL KILO        |S/6.50   |  
| B |MANDARINA EL KILO      |S/3.50   |
| C |DURAZNO EL KILO        |S/3.00   |
| D |PERA EL KILO           |S/4.50   |  
| E |APIO ENTERO            |S/2.00   |
| F |ZAPALLO EL KILO        |S/3.00   |
| G |CEBOLLA EL KILO        |S/5.00   |
| H |PAPA EL KILO           |S/3.50   |
| I |TOMATE EL KILO         |S/4.30   |
| J |============= SALIR =============|
|=====================================|""")
        opc=input("|OPCION:..:").upper()
        if opc=="A":
            total+=6.5
        elif opc=="B":
            total+=3.5
        elif opc=="C":
            total+=3
        elif opc=="D":
            total+=4.5
        elif opc=="E":
            total+=2
        elif opc=="F":
            total+=3
        elif opc=="G":
            total+=5
        elif opc=="H":
            total+=3.5
        elif opc=="I":
            total+=4.3
        elif opc=="J":
            break
        else:
            print("OPCION INCORRECTA")
    return total
def GOLOSINAS(total):
    while True:
        print("""|========================================|
|             GOLOSINAS                  |  
|========================================|
| A |CHOCOLATES M&M            |S/19.50  |  
| B |WAFFERS RELLENOS          |S/11.50  |
| C |CHOCOLATES PRINCESA       |S/11.00  |
| D |CHOCOLATE BITTER          |S/9.00   |  
| E |PAPAS ONDULADAS           |S/6.50   |
| F |GOMITAS DE OSO            |S/3.00   |
| G |PUDIN SABOR A CHOCOLATE   |S/5.00   |
| H |SNACK CASHEW              |S/6.00   |
| I |PECANAS PELADAS           |S/13.00  |
| J |NUECES PELADAS            |S/9.40   |
| K |GELATINA SABOR A FRESA    |S/2.90   |
| L |GELATINA SABOR A VAINILLAS|S/3.00   |
| M |============= SALIR ================|
|========================================|""")
        opc=input("|OPCION:..:").upper()
        if opc=="A":
            total+=19.5
        elif opc=="B":
            total+=11.5
        elif opc=="C":
            total+=11
        elif opc=="D":
            total+=9
        elif opc=="E":
            total+=6.5
        elif opc=="F":
            total+=3
        elif opc=="G":
            total+=5
        elif opc=="H":
            total+=6
        elif opc=="I":
            total+=13
        elif opc=="J":
            total+=9.4
        elif opc=="K":
            total+=2.9
        elif opc=="L":
            total+=3
        elif opc=="M":
            break
        else:
            print("OPCION INCORRECTA")
    return total
#####################################################################     
#####################################################################     
         

 

total=0
LIMP=0
ABA=0
PCP=0
BEBI=0
FYV=0
GOL=0
while True:
    print("""BIENVENIDO AL SUPERMERCADO LOTTUS
|=============================================|
|                CATALOGO                     |    
|=============================================|
| A |PRODUCTOS DE LIMPIEZA                    |
| B |ABARROTES                                |
| C |POLLO , CARNES Y PESCADOS                |
| D |BEBIDAS                                  |
| E |FRUTAS Y VERDURAS                        |
| F |GOLOSINAS                                |
| G |================= SALIR =================|
|=============================================|""")
    opm=input("|OPCION:..:").upper()
    if opm=="A":
        LIMP=PRODUCTOSDELIMPIEZA(total)        
    elif opm=="B":
        ABA=ABARROTES(total)
    elif opm=="C":
        PCP=POLLOCARNESPESCADOS(total)
    elif opm=="D":
        BEBI=BEBIDAS(total)
    elif opm=="E":
        FYV=FRUTASYVERDURAS(total)
    elif opm=="F":
        GOL=GOLOSINAS(total)
    elif opm=="G":
        break
    else:
        print("OPCION INCORRECTA")


 

print("|=============================|")
print(LIMP);print(ABA);print(PCP);print(BEBI);print(FYV);print(GOL)
neto=LIMP+ABA+PCP+BEBI+FYV+GOL
print("|===TOTAL A PAGAR: S/","{0:.2f}".format(neto),"===|")
print("|==GRACIAS POR SU PREFERENCIA=|")

