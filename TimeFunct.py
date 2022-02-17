class Time():
    def __init__(self, nome):
        self.objectName = nome
        self.resultado = [0, 0, 0]

    def ApplyPontos(self,):
        
        #self.resultado[0] += v * 3
        #self.resultado[1] += d * 0
        #self.resultado[2] += e * 1

        self.pontos = (int(self.resultado[0]) * 3) + (int(self.resultado[1]) * 0) + (int(self.resultado[2]) * 1) 


##Time1 = Time("Santos")
##Time1.resultado[0] = input("tem quantas Vitórias? ")
##Time1.resultado[1] = input("tem quantas Derrotas? ")
##Time1.resultado[2] = input("tem quantos Empates? ")
##
##Time1.ApplyPontos()
##
##print(Time1.objectName)
##print(Time1.pontos,"pts")
##print("vitorias, derrotas, empates:",Time1.resultado)
##
##Time2 = Time("Corinthians")
##Time2.resultado[0] = input("tem quantas Vitórias? ")
##Time2.resultado[1] = input("tem quantas Derrotas? ")
##Time2.resultado[2] = input("tem quantos Empates? ")
##
##Time2.ApplyPontos()
##
##print(Time2.objectName)
##print(Time2.pontos,"pts")
##print("vitorias, derrotas, empates:",Time2.resultado)
##
##
##input("ok?")
##
##quero = input("quer add um novo time?")
##Time3 = ""
##
##if quero == "nao":
##   input("vai dar erro!, saia do codigo") 
##
##if quero == "sim":
##    Time3 = Time(input("nome do time "))
##    print(Time3.objectName)
##
##    Time3.resultado[0] = input("tem quantas Vitórias? ")
##    Time3.resultado[1] = input("tem quantas Derrotas? ")
##    Time3.resultado[2] = input("tem quantos Empates? ")
##
##    Time3.ApplyPontos()
##
##    print(Time3.objectName)
##    print(Time3.pontos,"pts")
##    print("vitorias, derrotas, empates:",Time3.resultado)
##
##if Time1.pontos > Time2.pontos:
##    x = Time1
##    y = Time2
##    if Time3.pontos > x.pontos:
##        c = Time3
##        print(c.objectName,"Campeão Merda")
##        if x.pontos < y.pontos:
##            print(c.objectName,"Campeão Merda e", y.objectName,"Vice-Campeão putzz")
##            print("1o",c.objectName," com ",c.pontos,"pts")
##            print("2o",y.objectName," com ",y.pontos,"pts")
##            print("3o",x.objectName," com ",x.pontos,"pts")
##        else:
##            print(c.objectName,"Campeão Merda e", x.objectName,"Vice-Campeão putzz")
##            print("1o",c.objectName," com ",c.pontos,"pts")
##            print("2o",x.objectName," com ",x.pontos,"pts")
##            print("3o",y.objectName," com ",y.pontos,"pts")                
##    else:
##        c = Time3
##        print(x.objectName,"Campeão Merda")
##        if c.pontos < y.pontos:
##            print(x.objectName,"Campeão Merda e", y.objectName,"Vice-Campeão putzz")
##            print("1o",x.objectName," com ",x.pontos,"pts")
##            print("2o",y.objectName," com ",y.pontos,"pts")
##            print("3o",c.objectName," com ",c.pontos,"pts")
##        else:
##            print(x.objectName,"Campeão Merda e", c.objectName,"Vice-Campeão putzz")
##            print("1o",x.objectName," com ",x.pontos,"pts")
##            print("2o",c.objectName," com ",c.pontos,"pts")
##            print("3o",y.objectName," com ",y.pontos,"pts")
##            
##if Time1.pontos < Time2.pontos:
##    x = Time2
##    y = Time1
##    if Time3.pontos > x.pontos:
##        c = Time3
##        print(c.objectName,"Campeão Merda")
##        if x.pontos < y.pontos:
##            print(c.objectName,"Campeão e", y.objectName,"Vice-Campeão putzz")
##            print("1o",c.objectName," com ",c.pontos,"pts")
##            print("2o",y.objectName," com ",y.pontos,"pts")
##            print("3o",x.objectName," com ",x.pontos,"pts")
##        else:
##            print(c.objectName,"Campeão e", x.objectName,"Vice-Campeão putzz")
##            print("1o",c.objectName," com ",c.pontos,"pts")
##            print("2o",x.objectName," com ",x.pontos,"pts")
##            print("3o",y.objectName," com ",y.pontos,"pts")                
##    else:
##        print(x.objectName,"Campeão Merda")
##        if c.pontos < y.pontos:
##            print(x.objectName,"Campeão e", y.objectName,"Vice-Campeão putzz")
##            print("1o",x.objectName," com ",x.pontos,"pts")
##            print("2o",y.objectName," com ",y.pontos,"pts")
##            print("3o",c.objectName," com ",c.pontos,"pts")
##        else:
##            print(x.objectName,"Campeão e", c.objectName,"Vice-Campeão putzz")
##            print("1o",x.objectName," com ",x.pontos,"pts")
##            print("2o",c.objectName," com ",c.pontos,"pts")
##            print("3o",y.objectName," com ",y.pontos,"pts")
##            
Equipe = []
Team = []
c = 0
p = 1

for x in range(0,20):
    print(p)
    quero = input("quer add algum time? ")
    if not quero == "sim":
        while quero != "sim":
            print("Preciso de 20 times! Se não ira dar erro")
            print("Se quiser que de certo responda sim")
            quero = input("quer add algum time?")
            
    if quero == "sim" or quero == "Sim":
        Equipe.append(input("o nome do time: "))
        Team.append(Time(Equipe[c]))
        Team[c].resultado[0] = input("tem quantas Vitórias? ")
        Team[c].resultado[1] = input("tem quantas Derrotas? ")
        Team[c].resultado[2] = input("tem quantos Empates? ")
        
        Team[c].ApplyPontos()
        print(Team[c].objectName)
        print(Team[c].pontos,"pts")
        print("vitorias, derrotas, empates:",Team[c].resultado)
        c += 1
        p += 1


    #if Team[p].pontos > Team[b].pontos:
        #P = Team[p]
        #S = Team[b]
        
    #else:
        #P = Team[b]
        #S = Team[p]

    
    #b += 1

    #print(P.objectName," com ",P.pontos,"pts")
    #print(S.objectName," com ",S.pontos,"pts")

    

c = 0
b = 0

P = Team[0]
S = Team[1]
T = Team[2]
Q = Team[3]
QN = Team[4]
ST = Team[5]
SE = Team[6]
OI = Team[7]
NV = Team[8]
DZ = Team[9]
ON = Team[10]
DO = Team[11]
TZ = Team[12]
QZ = Team[13]
QE = Team[14]
DS = Team[15]
DT = Team[16]
DI = Team[17]
DN = Team[18]
VT = Team[19]

ps = Team[0]
ss = Team[1]
ts = Team[2]
qs = Team[3]
qn = Team[4]
st = Team[5]
se = Team[6]
oi = Team[7]
nv = Team[8]
dz = Team[9]
on = Team[10]
do = Team[11]
tz = Team[12]
qz = Team[13]
qe = Team[14]
ds = Team[15]
dt = Team[16]
di = Team[17]
dn = Team[18]
vt = Team[19]


for t in range(0,len(Team)):
    if not Team[c].objectName == Team[b].objectName:    
        if Team[c].pontos > Team[b].pontos:
            TimeP = Team[c]
            TimeS = Team[b]
            
        else:
            TimeP = Team[b]
            TimeS = Team[c]

        if TimeP.pontos > P.pontos:
            ps = P
            P = TimeP

        if TimeS.pontos > S.pontos:
            ss = S
            S = TimeS

        if Team[b].pontos < P.pontos and Team[b].pontos < S.pontos:
            TimeT = Team[b]
            if TimeT.pontos > T.pontos:
                ts = T
                T = TimeT

        if Team[b].pontos < S.pontos and Team[b].pontos < T.pontos:
            TimeQ = Team[b]
            if TimeQ.pontos > Q.pontos:
                qs = Q
                Q = TimeQ

        if Team[b].pontos < T.pontos and Team[b].pontos < Q.pontos:
            TimeQN = Team[b]
            if TimeQN.pontos > QN.pontos:
                qn = QN
                QN = TimeQN

        if Team[b].pontos < Q.pontos and Team[b].pontos < QN.pontos:
            TimeST = Team[b]
            if TimeST.pontos > ST.pontos:
                st = ST
                ST = TimeST

        if Team[b].pontos < QN.pontos and Team[b].pontos < ST.pontos:
            TimeSE = Team[b]
            if TimeSE.pontos > SE.pontos:
                se = SE
                SE = TimeSE

        if Team[b].pontos < ST.pontos and Team[b].pontos < SE.pontos:
            TimeOI = Team[b]
            if TimeOI.pontos > OI.pontos:
                oi = OI
                OI = TimeOI

        if Team[b].pontos < SE.pontos and Team[b].pontos < OI.pontos:
            TimeNV = Team[b]
            if TimeNV.pontos > NV.pontos:
                nv = NV
                NV = TimeNV

        if Team[b].pontos < OI.pontos and Team[b].pontos < NV.pontos:
            TimeDZ = Team[b]
            if TimeDZ.pontos > DZ.pontos:
                dz = DZ
                DZ = TimeDZ

        if Team[b].pontos < NV.pontos and Team[b].pontos < DZ.pontos:
            TimeON = Team[b]
            if TimeON.pontos > ON.pontos:
                on = ON
                ON = TimeON

        if Team[b].pontos < DZ.pontos and Team[b].pontos < ON.pontos:
            TimeDO = Team[b]
            if TimeDO.pontos > DO.pontos:
                do = DO
                DO = TimeDO

        if Team[b].pontos < ON.pontos and Team[b].pontos < DO.pontos:
            TimeTZ = Team[b]
            if TimeTZ.pontos > TZ.pontos:
                tz = TZ
                TZ = TimeTZ

        if Team[b].pontos < DO.pontos and Team[b].pontos < TZ.pontos:
            TimeQZ = Team[b]
            if TimeQZ.pontos > QZ.pontos:
                qz = QZ
                QZ = TimeQZ

        if Team[b].pontos < TZ.pontos and Team[b].pontos < QZ.pontos:
            TimeQE = Team[b]
            if TimeQE.pontos > QE.pontos:
                qe = QE
                QE = TimeQE

        if Team[b].pontos < QZ.pontos and Team[b].pontos < QE.pontos:
            TimeDS = Team[b]
            if TimeDS.pontos > DS.pontos:
                ds = DS
                DS = TimeDS

        if Team[b].pontos < QE.pontos and Team[b].pontos < DS.pontos:
            TimeDT = Team[b]
            if TimeDT.pontos > DT.pontos:
                dt = DT
                DT = TimeDT

        if Team[b].pontos < DS.pontos and Team[b].pontos < DT.pontos:
            TimeDI = Team[b]
            if TimeDI.pontos > DI.pontos:
                di = DI
                DI = TimeDI
                
        if Team[b].pontos < DT.pontos and Team[b].pontos < DI.pontos:
            TimeDN = Team[b]
            if TimeDN.pontos > DN.pontos:
                dn = DN
                DN = TimeDN

        if Team[b].pontos < DI.pontos and Team[b].pontos < DN.pontos:
            TimeVT = Team[b]
            if TimeVT.pontos > VT.pontos:
                vt = VT
                VT = TimeVT
        

        if T.pontos > S.pontos:
            ss = S
            S = T
            T = ss

        if P.objectName == S.objectName:
            S = ps

        if P.objectName == T.objectName:
            T = ps

        if S.objectName == T.objectName:
            T = ss

        if Q.pontos > T.pontos:
            ts = T
            T = Q
            Q = ts
            
        if P.objectName == Q.objectName:
            Q = ps

        if S.objectName == Q.objectName:
            Q = ss

        if T.objectName == Q.objectName:
            Q = ts

        if QN.pontos > Q.pontos:
            qs = Q
            Q = QN
            QN = qs

        if P.objectName == QN.objectName:
            QN = ps

        if S.objectName == QN.objectName:
            QN = ss

        if T.objectName == QN.objectName:
            QN = ts

        if Q.objectName == QN.objectName:
            QN = qs

        if ST.pontos > QN.pontos:
            qn = QN
            QN = ST
            ST = qn

        if P.objectName == ST.objectName:
            ST = ps

        if S.objectName == ST.objectName:
            ST = ss

        if T.objectName == ST.objectName:
            ST = ts

        if Q.objectName == ST.objectName:
            ST = qs

        if QN.objectName == ST.objectName:
            ST = qn

        if SE.pontos > ST.pontos:
            st = ST
            ST = SE
            SE = st

        if P.objectName == SE.objectName:
            SE = ps

        if S.objectName == SE.objectName:
            SE = ss

        if T.objectName == SE.objectName:
            ST = ts

        if Q.objectName == SE.objectName:
            SE = qs

        if QN.objectName == SE.objectName:
            SE = qn

        if ST.objectName == SE.objectName:
            SE = st

        if OI.pontos > SE.pontos:
            se = SE
            SE = OI
            OI = se

        if P.objectName == OI.objectName:
            OI = ps

        if S.objectName == OI.objectName:
            OI = ss

        if T.objectName == OI.objectName:
            OI = ts

        if Q.objectName == OI.objectName:
            OI = qs

        if QN.objectName == OI.objectName:
            OI = qn

        if ST.objectName == OI.objectName:
            OI = st

        if SE.objectName == OI.objectName:
            OI = se

        if NV.pontos > OI.pontos:
            oi = OI
            OI = NV
            NV = oi

        if P.objectName == NV.objectName:
            NV = ps

        if S.objectName == NV.objectName:
            NV = ss

        if T.objectName == NV.objectName:
            NV = ts

        if Q.objectName == NV.objectName:
            NV = qs

        if QN.objectName == NV.objectName:
            NV = qn

        if ST.objectName == NV.objectName:
            NV = st

        if SE.objectName == NV.objectName:
            NV = se

        if OI.objectName == NV.objectName:
            NV = oi

        if DZ.pontos > NV.pontos:
            nv = NV
            NV = DZ
            DZ = nv

        if P.objectName == DZ.objectName:
            DZ = ps

        if S.objectName == DZ.objectName:
            DZ = ss

        if T.objectName == DZ.objectName:
            DZ = ts

        if Q.objectName == DZ.objectName:
            DZ = qs

        if QN.objectName == DZ.objectName:
            DZ = qn

        if ST.objectName == DZ.objectName:
            DZ = st

        if SE.objectName == DZ.objectName:
            DZ = se

        if OI.objectName == DZ.objectName:
            DZ = oi

        if NV.objectName == DZ.objectName:
            DZ = nv

        if ON.pontos > DZ.pontos:
            dz = DZ
            DZ = ON
            ON = dz

        if P.objectName == ON.objectName:
            ON = ps

        if S.objectName == ON.objectName:
            ON = ss

        if T.objectName == ON.objectName:
            ON = ts

        if Q.objectName == ON.objectName:
            ON = qs

        if QN.objectName == ON.objectName:
            ON = qn

        if ST.objectName == ON.objectName:
            ON = st

        if SE.objectName == ON.objectName:
            ON = se

        if OI.objectName == ON.objectName:
            ON = oi

        if NV.objectName == ON.objectName:
            ON = nv

        if DZ.objectName == ON.objectName:
            ON = dz

        if DO.pontos > ON.pontos:
            on = ON
            ON = DO
            DO = on

        if P.objectName == DO.objectName:
            DO = ps

        if S.objectName == DO.objectName:
            DO = ss

        if T.objectName == DO.objectName:
            DO = ts

        if Q.objectName == DO.objectName:
            DO = qs

        if QN.objectName == DO.objectName:
            DO = qn

        if ST.objectName == DO.objectName:
            DO = st

        if SE.objectName == DO.objectName:
            DO = se

        if OI.objectName == DO.objectName:
            DO = oi

        if NV.objectName == DO.objectName:
            DO = nv

        if DZ.objectName == DO.objectName:
            DO = dz

        if ON.objectName == DO.objectName:
            DO = on

        if TZ.pontos > DO.pontos:
            do = DO
            DO = TZ
            TZ = do

        if P.objectName == TZ.objectName:
            TZ = ps

        if S.objectName == TZ.objectName:
            TZ = ss

        if T.objectName == TZ.objectName:
            TZ = ts

        if Q.objectName == TZ.objectName:
            TZ = qs

        if QN.objectName == TZ.objectName:
            TZ = qn

        if ST.objectName == TZ.objectName:
            TZ = st

        if SE.objectName == TZ.objectName:
            TZ = se

        if OI.objectName == TZ.objectName:
            TZ = oi

        if NV.objectName == TZ.objectName:
            TZ = nv

        if DZ.objectName == TZ.objectName:
            TZ = dz

        if ON.objectName == TZ.objectName:
            TZ = on

        if DO.objectName == TZ.objectName:
            TZ = do

        if QZ.pontos > TZ.pontos:
            tz = TZ
            TZ = QZ
            QZ = tz

        if P.objectName == QZ.objectName:
            QZ = ps

        if S.objectName == QZ.objectName:
            QZ = ss

        if T.objectName == QZ.objectName:
            QZ = ts

        if Q.objectName == QZ.objectName:
            QZ = qs

        if QN.objectName == QZ.objectName:
            QZ = qn

        if ST.objectName == QZ.objectName:
            QZ = st

        if SE.objectName == QZ.objectName:
            QZ = se

        if OI.objectName == QZ.objectName:
            QZ = oi

        if NV.objectName == QZ.objectName:
            QZ = nv

        if DZ.objectName == QZ.objectName:
            QZ = dz

        if ON.objectName == QZ.objectName:
            QZ = on

        if DO.objectName == QZ.objectName:
            QZ = do

        if TZ.objectName == QZ.objectName:
            QZ = tz

        if QE.pontos > QZ.pontos:
            qz = QZ
            QZ = QE
            QE = qz

        if P.objectName == QE.objectName:
            QE = ps

        if S.objectName == QE.objectName:
            QE = ss

        if T.objectName == QE.objectName:
            QE = ts

        if Q.objectName == QE.objectName:
            QE = qs

        if QN.objectName == QE.objectName:
            QE = qn

        if ST.objectName == QE.objectName:
            QE = st

        if SE.objectName == QE.objectName:
            QE = se

        if OI.objectName == QE.objectName:
            QE = oi

        if NV.objectName == QE.objectName:
            QE = nv

        if DZ.objectName == QE.objectName:
            QE = dz

        if ON.objectName == QE.objectName:
            QE = on

        if DO.objectName == QE.objectName:
            QE = do

        if TZ.objectName == QE.objectName:
            QE = tz

        if QZ.objectName == QE.objectName:
            QE = qz

        if DS.pontos > QE.pontos:
            qe = QE
            QE = DS
            DS = qe

        if P.objectName == DS.objectName:
            DS = ps

        if S.objectName == DS.objectName:
            DS = ss

        if T.objectName == DS.objectName:
            DS = ts

        if Q.objectName == DS.objectName:
            DS = qs

        if QN.objectName == DS.objectName:
            DS = qn

        if ST.objectName == DS.objectName:
            DS = st

        if SE.objectName == DS.objectName:
            DS = se

        if OI.objectName == DS.objectName:
            DS = oi

        if NV.objectName == DS.objectName:
            DS = nv

        if DZ.objectName == DS.objectName:
            DS = dz

        if ON.objectName == DS.objectName:
            DS = on

        if DO.objectName == DS.objectName:
            DS = do

        if TZ.objectName == DS.objectName:
            DS = tz

        if QZ.objectName == DS.objectName:
            DS = qz

        if QE.objectName == DS.objectName:
            DS = qe

        if DT.pontos > DS.pontos:
            ds = DS
            DS = DT
            DT = ds

        if P.objectName == DT.objectName:
            DT = ps

        if S.objectName == DT.objectName:
            DT = ss

        if T.objectName == DT.objectName:
            DT = ts

        if Q.objectName == DT.objectName:
            DT = qs

        if QN.objectName == DT.objectName:
            DT = qn

        if ST.objectName == DT.objectName:
            DT = st

        if SE.objectName == DT.objectName:
            DT = se

        if OI.objectName == DT.objectName:
            DT = oi

        if NV.objectName == DT.objectName:
            DT = nv

        if DZ.objectName == DT.objectName:
            DT = dz

        if ON.objectName == DT.objectName:
            DT = on

        if DO.objectName == DT.objectName:
            DT = do

        if TZ.objectName == DT.objectName:
            DT = tz

        if QZ.objectName == DT.objectName:
            DT = qz

        if QE.objectName == DT.objectName:
            DT = qe

        if DS.objectName == DT.objectName:
            DT = ds

        if DI.pontos > DT.pontos:
            dt = DT
            DT = DI
            DI = dt

        if P.objectName == DI.objectName:
            DI = ps

        if S.objectName == DI.objectName:
            DI = ss

        if T.objectName == DI.objectName:
            DI = ts

        if Q.objectName == DI.objectName:
            DI = qs

        if QN.objectName == DI.objectName:
            DI = qn

        if ST.objectName == DI.objectName:
            DI = st

        if SE.objectName == DI.objectName:
            DI = se

        if OI.objectName == DI.objectName:
            DI = oi

        if NV.objectName == DI.objectName:
            DI = nv

        if DZ.objectName == DI.objectName:
            DI = dz

        if ON.objectName == DI.objectName:
            DI = on

        if DO.objectName == DI.objectName:
            DI = do

        if TZ.objectName == DI.objectName:
            DI = tz

        if QZ.objectName == DI.objectName:
            DI = qz

        if QE.objectName == DI.objectName:
            DI = qe

        if DS.objectName == DI.objectName:
            DI = ds

        if DT.objectName == DI.objectName:
            DI = dt

        if DN.pontos > DI.pontos:
            di = DI
            DI = DN
            DN = di

        if P.objectName == DN.objectName:
            DN = ps

        if S.objectName == DN.objectName:
            DN = ss

        if T.objectName == DN.objectName:
            DN = ts

        if Q.objectName == DN.objectName:
            DN = qs

        if QN.objectName == DN.objectName:
            DN = qn

        if ST.objectName == DN.objectName:
            DN = st

        if SE.objectName == DN.objectName:
            DN = se

        if OI.objectName == DN.objectName:
            DN = oi

        if NV.objectName == DN.objectName:
            DN = nv

        if DZ.objectName == DN.objectName:
            DN = dz

        if ON.objectName == DN.objectName:
            DN = on

        if DO.objectName == DN.objectName:
            DN = do

        if TZ.objectName == DN.objectName:
            DN = tz

        if QZ.objectName == DN.objectName:
            DN = qz

        if QE.objectName == DN.objectName:
            DN = qe

        if DS.objectName == DN.objectName:
            DN = ds

        if DT.objectName == DN.objectName:
            DN = dt

        if DI.objectName == DN.objectName:
            DN = di

        if VT.pontos > DN.pontos:
            dn = DN
            DI = VT
            VT = dn

        if P.objectName == VT.objectName:
            VT = ps

        if S.objectName == VT.objectName:
            VT = ss

        if T.objectName == VT.objectName:
            VT = ts

        if Q.objectName == VT.objectName:
            VT = qs

        if QN.objectName == VT.objectName:
            VT = qn

        if ST.objectName == VT.objectName:
            VT = st

        if SE.objectName == VT.objectName:
            VT = se

        if OI.objectName == VT.objectName:
            VT = oi

        if NV.objectName == VT.objectName:
            VT = nv

        if DZ.objectName == VT.objectName:
            VT = dz

        if ON.objectName == VT.objectName:
            VT = on

        if DO.objectName == VT.objectName:
            VT = do

        if TZ.objectName == VT.objectName:
            VT = tz

        if QZ.objectName == VT.objectName:
            VT = qz

        if QE.objectName == VT.objectName:
            VT = qe

        if DS.objectName == VT.objectName:
            VT = ds

        if DT.objectName == VT.objectName:
            VT = dt

        if DI.objectName == VT.objectName:
            VT = di

        if DN.objectName == VT.objectName:
            VT = dn
            
    if b == len(Team):
        c += 1
        b = 0

    b += 1

print("1o",P.objectName," com ",P.pontos,"pts")
print("2o",S.objectName," com ",S.pontos,"pts")
print("3o",T.objectName," com ",T.pontos,"pts")
print("4o",Q.objectName," com ",Q.pontos,"pts")
print("5o",QN.objectName," com ",QN.pontos,"pts")
print("6o",ST.objectName," com ",ST.pontos,"pts")
print("7o",SE.objectName," com ",SE.pontos,"pts")
print("8o",OI.objectName," com ",OI.pontos,"pts")
print("9o",NV.objectName," com ",NV.pontos,"pts")
print("10o",DZ.objectName," com ",DZ.pontos,"pts")
print("11o",ON.objectName," com ",ON.pontos,"pts")
print("12o",DO.objectName," com ",DO.pontos,"pts")
print("13o",TZ.objectName," com ",TZ.pontos,"pts")
print("14o",QZ.objectName," com ",QZ.pontos,"pts")
print("15o",QE.objectName," com ",QE.pontos,"pts")
print("16o",DS.objectName," com ",DS.pontos,"pts")
print("17o",DT.objectName," com ",DT.pontos,"pts")
print("18o",DI.objectName," com ",DI.pontos,"pts")
print("19o",DN.objectName," com ",DN.pontos,"pts")
print("20o",VT.objectName," com ",VT.pontos,"pts")

    
