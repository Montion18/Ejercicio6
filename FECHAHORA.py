class FechaHora:
    __dia=''
    __mes=''
    __anio=''
    __hora=''
    __minuto=''
    __segundos=''
    

    def __init__(self,dia,mes,anio,hora,min,seg):
       self.__dia=dia
       self.__mes=mes
       self.__anio=anio
       self.__hora=hora
       self.__minuto=min
       self.__segundos=seg


    def Mostrar(self):
        print("\nDia: {} Mes: {} Año: {} Hora: {} Min: {} Seg: {} \n".format(self.__dia,self.__mes,self.__anio,self.__hora,self.__minuto,self.__segundos))

    def PonerEnHora(self,h=0,m=0,s=0):
        self.__hora=h
        self.__minuto=m
        self.__segundos=s

    def AdelantarHora(self,h=0,m=0):
        self.__hora+=h
        self.__minuto+=m
        if self.__hora<0:
            self.__dia-=1
            self.__hora=24+h
        if self.__dia==0:
            self.__mes-=1
        if self.__mes==0:
            self.__mes=12
            self.__dia=31
            self.__anio-=1
        if self.__segundos>60:
            self.__minuto+=1
        if self.__minuto>60:
            self.__hora+=1
        if self.__hora>24:
            self.__hora=h-24
            self.__dia+=1
        if self.__anio%4 == 0:
            if self.__anio%100 == 0:
                if self.__anio%400 == 0:
                    if self.__mes==2 and self.__dia>29:
                        self.__dia=1
                        self.__mes+=1
                    else:
                        if self.__mes==2 and self.__dia<29:
                            self.__dia+=1
            else:
                if self.__mes==2 and self.__dia>29:
                    self.__dia=1
                    self.__mes+=1
                else:
                    if self.__mes==2 and self.__dia<29:
                        self.__dia+=1
                
        else:
            if self.__mes == 2 and self.__dia>28:
                self.__dia=1
                self.__mes+=1
            else:
                if (self.__mes == 4 or self.__mes==6 or self.__mes==9 or self.__mes==11) and self.__dia>30:
                    self.__dia=1
                    self.__mes+=1
       
                else:
                    if self.__mes==1 or self.__mes==3 or self.__mes==5 or self.__mes==7 or self.__mes==8 or self.__mes==10 or self.__mes==12 and self.__dia>31:
                        self.__dia=1
                        self.__mes+=1
                        if self.__mes>12:
                            self.__mes=1
                            self.__anio+=1

    def __add__(self,otro):
        return self.__hora+otro.__hora

    def __sub__(self,otro):
        return self.__hora-otro.__hora
    def __gt__(self,otro):
        return self.__hora>otro.__hora
        
