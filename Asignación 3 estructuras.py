class Dia: #clase para guardar los datos de un dia
    def __init__(self, dia, fecha):
        self.dia = dia #numero del dia (0 Domingo, 1 Lunes, ...)
        self.fecha = fecha
    def diaFecha(self):
        return str(self.fecha[2]) #String del dia

class Semana: #clase para guardar los datos de una seman
    def __init__(self):
        self.diasSemana = []
    def addDia(self,diaNuevo):
        self.diasSemana.append(diaNuevo)
    def imprimirSemana(self): #Metodo que da el formato a los dias de la semana
        strSemana = ""   
        if(len(self.diasSemana) < 7 and len(self.diasSemana) > 0 and  self.diasSemana[0].dia > 0): #Cuantos espacios adelante se ocupan
            numEspacio = self.diasSemana[0].dia#Cantidadde espacios que se deja
            for i in range(0,numEspacio):
                strSemana += '{:>3}'.format("")
        for dia in self.diasSemana: #dias de la semana
                strSemana += '{:>3}'.format(str(dia.diaFecha()))
        
        return '{:<21}'.format(strSemana)+" |"

            

class Mes: #clase que representa a un mes del calendario
    def __init__(self,nombre,numeroMes):
        self.nombre = nombre #nombre del mes
        self.numMes = numeroMes #numero que representa ese mes
        self.semanas = [] #Lista de sus respectivas semanas
    def addSemana(self,semanaNueva):
        self.semanas.append(semanaNueva)
    def imprimirSemanaMes(self,semana):
        strSemana = ""
        if(semana < len(self.semanas)):
            strSemana = self.semanas[semana].imprimirSemana()
        elif(semana >= len(self.semanas)):
            strSemana = '{:<21}'.format(strSemana)+" |"
        return strSemana
    def imprimirInfoMes(self): #Retornar un string con el formato de los días
        return '{:>3}'.format("D")+'{:>3}'.format("L")+'{:>3}'.format("K")+'{:>3}'.format("M")+'{:>3}'.format("J")+'{:>3}'.format("V")+'{:>3}'.format("S")+" |"
    def imprimirNombre(self): #Retorna el nombre del mes 
        return '{:^21}'.format(str(self.nombre))+" |"

class Calendario: #clase que representa a un calendario
    def __init__(self,anno):
        self.anno = anno #posee un anno y una lista de meses
        self.meses = []
    def addMes(self, mesNuevo):
        self.meses.append(mesNuevo)
    def imprimirCalendarioInfo(self): #Titulo del claendario
        print('{:^87}'.format("Calendario del año "+str(self.anno)))
    def imprimirMes(self, ini, fin): #inicio debe ser menor que fin y debe de ser menor a 12 y mayo a 1
        linea = ""                   #Se busca que se imprima los meses que desee el usuario
        for i in range(ini, fin):
            linea += self.meses[i].imprimirNombre() 
        print(linea)
        linea = ""
        for i in range(ini, fin):
            linea += self.meses[i].imprimirInfoMes() 
        print(linea)
        linea = ""
        for j in range(0,6):
            for i in range(ini,fin):    
                linea += self.meses[i].imprimirSemanaMes(j)
            print(linea)
            linea = ""
            
        
