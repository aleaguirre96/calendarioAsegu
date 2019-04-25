from Estructuras import *


#Esta funcion se encarga de verificar que los elementos
#de una tupla sean solo enteros mayores a 0
def tupla_int_valida(tuplaFecha):
    resultado = True
    for i in tuplaFecha:
        if not isinstance(i, int) or i <= 0:
            resultado = False
            break
    return resultado

#R0 Verfica que sea una tupla de tres elementos
def fecha_es_tupla(tuplaFecha):
    if isinstance(tuplaFecha, tuple) and len(tuplaFecha) == 3:
        return tupla_int_valida(tuplaFecha)
    else:
        return False

#R1 Verufuca que el año introducido sea bisiesto
def bisiesto (ano):
    if type (ano) != int or ano < 1583:
        return False
    elif((ano%4 == 0 and ano%100 != 0) or ano%400 == 0):
        return True
    else:
        return False
    
#R2 Verifica que una tupla tenga sentido
#en relacion a los años, meses y días que posee
def fecha_es_valida(tuplaFecha):
    resultado = False
    meses31 = {1,3,5,7,8,10,12}
    meses30 = {4,6,9,11}
    if fecha_es_tupla(tuplaFecha) and tuplaFecha[0] >= 1582: #Verifica que sea un año valido
        if(tuplaFecha[1] in meses31) and (tuplaFecha[2] >= 1 and tuplaFecha[2] <= 31): #tiene 31 dias
            resultado = True 
        elif(tuplaFecha[1] in meses30) and (tuplaFecha[2] >= 1 and tuplaFecha[2] <= 30): #tiene 30 dias
            resultado = True
        elif(tuplaFecha[1] == 2): # es febrero
            if bisiesto(tuplaFecha[0]) and  (tuplaFecha[2] >= 1 and tuplaFecha[2] <= 29): #es bisiesto
                resultado = True
            elif(tuplaFecha[2] >= 1 and tuplaFecha[2] <= 28): #no es bisiesto
                resultado = True

    return resultado

#R3
def dia_siguiente(fecha):
    fecha_lista = [] # Aqui se agregan los elementos anho, mes y dia para posteriormente convertirse en una tupla (para la salida)
    fecha_final = () # Aqui se guarda la respuesta final luego de aplicado el algoritmo de dia_siguiente
    validar_fecha = fecha_es_valida(fecha) #Se verifica que la fecha sea valida
    if validar_fecha:
        dias_mes = 0 # variable que guarda el largo de un dia
        meses_30 = [3,6,9,11] #lista de meses que poseen 30 dias
        anho = fecha[0]# se extrae el anho de la tupla ingresada
        mes = fecha[1]# se extrae el mes de la tupla ingresada
        dia = fecha[2]# se extrae el dia de la tupla ingresada
        verif_bisiesto = bisiesto(anho) # Se verifica si el anho ingresado es bisiesto 
        if mes == 2:# caso en que sea febrero
            if verif_bisiesto == True: # De ser bisiesto, el mes posee 29 dias
                dias_mes = 29
            else:   # De no serlo, tiene 28
                dias_mes = 28
        elif mes in meses_30: # Si el mes ingresado se encuentra dentro de la lista anteriormente escrita, el mes posee 30 dias
            dias_mes = 30
        else:  # De lo contrario posee 31
            dias_mes = 31
        
        if dia < dias_mes: # Caso en que no sea el ultimo dia del mes, se suma 1 al dia
            dia +=1
        else: # Si es el ultimo dia, el dia se setea en 1 
            dia = 1
            if mes == 12: # Acto seguido se verifica si el mes corresponde a diciembre, de serlo el mes se setea en 1 y se suma 1 al anho
                mes = 1
                anho +=1
            else: # De lo contrario, se suma 1 al mes
                mes +=1

        #---------------------- En esta seccion se procede a ingresar los datos de las variables a la lista inicial de fecha-----------------
        fecha_lista.append(anho)
        fecha_lista.append(mes)
        fecha_lista.append(dia)
        #------------------------------------------------------------------------------------------------------------------------------------
        fecha_final = tuple(fecha_lista) # Se convierte la lista anterior en una tupla para la salida
        #print("el dia siguiente de la fecha " + str(fecha) + " es " + str(fecha_final)) # Se imprime resultado
    return fecha_final



#R4

def dias_desde_primero_enero(fecha):
    validar_fecha = fecha_es_valida(fecha) #Se verifica que la fecha sea valida
    if validar_fecha == False: # Mensaje de error en caso de que fecha no sea valida
        return -1#"la fecha ingresada no es valida"
    else:
        anho_normal = [31,59,90,120,151,181,212,243,273,304,334,365] # Total de suma de dias de un anho normal
        anho_bisiesto = [31,60,91,121,152,182,213,244,274,305,335,366]# Total de suma de dias de un anho bisiesto
        anho = fecha[0] # Se extrae anho de tupla ingresada
        mes = fecha[1] # Se extrae mes de tupla ingresada
        dia = fecha[2] # Se extrae dia de tupla ingresada
        dias_totales = 0
        verif_bisiesto = bisiesto(anho) # verifica si el anho es bisiesto
        if mes == 1: # Si el mes es enero, se toma el dia ingresado -1 (debido a la diferencia con respecto al primero de enero)
            dias_totales = dia -1
        elif mes == 2:# caso en que sea febrero
                if verif_bisiesto == True: # De ser bisiesto, el mes posee 29 dias
                    dias_totales = (anho_bisiesto[0] + dia) - 1
                else:   # De no serlo, tiene 28
                    dias_totales = (anho_normal[0] + dia) - 1 
        else: # De ingresar cualquier otro mes que no sea enero ni febrero 
            if verif_bisiesto == True:
                dias_totales = (anho_bisiesto[mes-2] + dia) - 1 # De ser un anho bisiesto, se toma el mes-2 (debido a que el indice de la lista de sumas de dias inicia en 0 y no se debe tomar en cuenta la totalidad de los dias del mes ingresado, sino solamente los dias ingresados en la tupla)
            else:
                dias_totales = (anho_normal[mes-2] + dia) - 1# De no ser bisiesto, se toma la otra lista
    return dias_totales


#R5 Indica cual dia de la semana es el primero de enero
#0 = Domingo, 1 = Lunes, 2= Martes, 3= Miercoles. 4= Jueves
#5 = Viernes, 6= Sabado
def dia_primero_enero(ano):
    if type (ano) != int or ano < 1583:
        return -1
    else:
        a = (14 - 1) // 12
        y = ano - a
        m = 1 + 12 * a - 2
        d = (1 + y + (y//4) - (y//100) + (y//400) + ((31 * m)//12)) % 7
    return d

#R6
def imprimir_3x4(anno): ##
    calend= crearCalendario(anno) ##Se crea la estructura de un calendario
    calend.imprimirCalendarioInfo()
    calend.imprimirMes(0,4)
    calend.imprimirMes(4,8)
    calend.imprimirMes(8,12)

    
#Crear Calendario
#Dado un anno se crea los meses y dias que este posee
#Para esto se usan las clasesx Día, Semana, Mes
def crearCalendario(anno):
    nuevoCalen = Calendario(anno)
    ##Se procede a crear los meses
    ##Se tiene una lista de los mese
    mesesNom = ["Enero","Febrero","Marzo", "Abril", "Mayo", "Junio",
                "Julio", "Agosto","Septiembre", "Octubre", "Noviembre", "Diciembre"]
    contadorDiaSemana = dia_primero_enero(nuevoCalen.anno)
    for i in range(0, len(mesesNom)):
        contadorDiaSemana = crearMes(mesesNom[i],i+1,nuevoCalen, contadorDiaSemana) #Se pasa el calendario para trabajar por refernecia
    return nuevoCalen

#Se crea un Mes, para ser agregado al Calendario
def crearMes(nombreMes, numeroMes, calendario, diaSemana):
    nuevoMes = Mes(nombreMes, numeroMes)
    ##Se procede a crear las semanas del mes nuevo

    diaSemana = crearSemanasMes(nuevoMes, calendario.anno, diaSemana)
        
    ##Se agrega el mes al Calendario
    calendario.addMes(nuevoMes)
    return diaSemana #Contador de que dia sigue para el siguiente Mes

def crearSemanasMes(mesAct, anno, diaSemanaAct):
    contadorDiasMes = cantidadDiasMes(mesAct.numMes, anno)
    semana = Semana()
    for diaActFecha in range(1, contadorDiasMes+1): #Se crean los dias de ese mes
        #Se crea un nuevo Dia
        nuevoDia = Dia(diaSemanaAct, (anno,mesAct.numMes,diaActFecha))
        semana.addDia(nuevoDia) #Se agrega el dia a la semana
        if(diaSemanaAct == 6): #Si ya el dia es 6, se crea una nueva semana
            diaSemanaAct = 0 #Se vuelve el día lunes
            mesAct.addSemana(semana)#Se agrega la semana al mes
            semana = Semana() #Se crea una nueva semana
        else:
            diaSemanaAct += 1 #Si es otro dia solo se suma el contador
    if(diaSemanaAct <= 6):
        mesAct.addSemana(semana)
    return diaSemanaAct
            
    

#Esta funcion me da el contador de dias, dependiendo del mes y anno dado
def cantidadDiasMes(numMes, anno):
    meses31 = {1,3,5,7,8,10,12} ##Meses que poseen 31 dias
    meses30 = {4,6,9,11} ##Meses que poseen 30 dias
    dias = 0 
    if(numMes in meses31):
        dias = 31  
    elif(numMes in meses30):
        dias = 30
    elif(numMes == 2): # es febrero
            if bisiesto(anno): #es bisiesto
                dias = 29
            else:
                dias = 28
    return dias
    

#===============================================================================================================
#= 
#= De aqui en adelante se agregan los requerimientos de la parte 3b
#=
#===============================================================================================================

#Esta funcion es necesaria para el calculo del primer
#dia de un mes en especifico
def moduloMes(mes, anno):
    resultado = 0
    if(mes >= 1 and mes <= 12):
        for i in range(1,mes):
            resultado = resultado + cantidadDiasMes(i, anno)%7
        resultado = resultado % 7
    return resultado

#R9
#Dada una fecha se espera que retorne un dia 0 = Domingo, 1 = Lunes, ...
def dia_semana(fecha):
    resultado = -1 #Si retorna -1 hay un error
    if(fecha_es_valida(fecha)): #Verifica que sea (dia,mes,anno)
        modMes = moduloMes(fecha[1], fecha[0])
        annodecre = fecha[0] - 1
        resultado = ((annodecre % 7)+(((annodecre//4) -(3 * (((annodecre//100) + 1) // 4)))%7) + modMes + (fecha[2] % 7)) % 7
    return resultado

#R10
#Dado un anno y mes, esta funcion nos retorna el primer dia del mes dado
def dia_inicio_mes (anno, mes):
    resultado = 0
    if(anno >= 1582 and mes >= 1 and mes <= 12):
        resultado = dia_semana((anno,mes,1))
    else:
        resultado = -1
    return resultado #Si no es un mes y anno valido retorna -1
        

