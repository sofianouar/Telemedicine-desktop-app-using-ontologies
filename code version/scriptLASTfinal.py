from PyQt5 import QtWidgets
from PyQt5 import QtGui
import re
from PyQt5.QtCore import Qt, QSize,QDate,QProcess
import pandas as pd
from pandas import DataFrame
import os
import sys
import wsjdid, wilaya
class geste(QtWidgets.QScrollArea):
    def __init__(self):
        super(geste, self).__init__()

        self.wid = QtWidgets.QWidget()
        self.setWidgetResizable(True)
        self.layoute = QtWidgets.QGridLayout()
        self.wid.setLayout(self.layoute)
        self.page=QtWidgets.QLabel()
        self.page.setPixmap(QtGui.QPixmap("animation\\geste.png"))
        self.setStyleSheet('background-color: rgb(221,0,25);')
        self.layoute.addWidget(self.page,0,0,10,10)
        self.setWidget(self.wid)
        self.setWidgetResizable(True)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.commencer=QtWidgets.QPushButton("  COMMENCER  ")
        #self.commencer.setFlat(True)
        font=QtGui.QFont()
        font.setBold(True)
        font.setPointSize(15)
        self.commencer.setFont(font)
        self.commencer.setStyleSheet('color:black ;background-color: yellow;')
        self.layoute.addWidget(self.commencer, 10,7)
    # self.setFixedSize(500,400)

class chargment(QtWidgets.QLabel):
    def __init__(self):
        super(chargment, self).__init__()
        self.anim=QtGui.QMovie("animation\\a.gif")
        self.setMovie(self.anim)
        self.anim.start()
        self.msg=QtWidgets.QLabel("veuillez patienter..",self)
        self.msg.setGeometry(90,122,120,100)
        font=QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.msg.setFont(font)
        self.setWindowFlag(Qt.FramelessWindowHint)
        self.setWindowFlag(Qt.WindowStaysOnTopHint)
        self.show()

class carte(QtWidgets.QWidget):
    def __init__(self,nom,adr,num,spec):
        super(carte, self).__init__()
        self.layoute=QtWidgets.QGridLayout()
        self.setLayout(self.layoute)
        self.patient=None
        self.tabib=None
        nom = nom.replace("_"," ")
        self.nom=QtWidgets.QLabel(nom)
        adr = adr.replace("_", " ")
        self.adresse=QtWidgets.QLabel(adr)
        self.spec = QtWidgets.QLabel("spécialité : "+spec)
        self.numero=QtWidgets.QLabel("0"+num)
        self.layoute.addWidget(self.spec,0,0)
        self.layoute.addWidget(self.nom, 1, 0)
        self.layoute.addWidget(self.adresse,2,0)
        self.layoute.addWidget(self.numero,3,0)
        self.rdv=QtWidgets.QPushButton("prendre un rendez vous!")
        self.layoute.addWidget(self.rdv,4,1)
        font=QtGui.QFont()
        font.setPointSize(10)
        self.nom.setFont(font)
        self.adresse.setFont(font)
        self.numero.setFont(font)
        self.rdv.setFont(font)

        self.rdv.clicked.connect(self.prendre_rdv)

        self.show()

    def prendre_rdv(self):


       for i in wsjdid.ontologie.individuals():

           if str(i.iri)==str(self.patient):
               p=i
           if str(i.iri)==str(self.toubib):
               m=i

       with wsjdid.ontologie:

         p.a_pris_rdv.append(m)
       self.s = QtWidgets.QMessageBox()
       msg="votre demande de rendez-vous a été éffectuer.\nappelez votre médecin ultérieurement pour avoir la date de votre rendez-vous."
       self.s.setText(msg)
       self.s.show()
       wsjdid.ontologie.save(file="PROJET.owl", format="ntriples")
       wsjdid.default_world.save()

class fiche(QtWidgets.QScrollArea):
    def __init__(self):
        super(fiche, self).__init__()
        self.wid=QtWidgets.QWidget()
        self.setWidgetResizable(True)
        self.layoute=QtWidgets.QGridLayout()
        self.wid.setLayout(self.layoute)

        self.setWidget(self.wid)
        self.setWidgetResizable(True)
        self.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        #self.setFixedSize(500,400)
        self.show()

class comptemed(QtWidgets.QWidget):
    def __init__(self,nom,adr,numtel):
        super(comptemed, self).__init__()
        self.objet=QtWidgets.QGridLayout()
        self.setLayout(self.objet)
        self.info1=QtWidgets.QLabel("Session de : "+nom+"")
        font=QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.info1.setFont(font)
        self.info2=QtWidgets.QLabel("adresse:"+adr)
        self.info3=QtWidgets.QLabel("numero de telephone : 0"+str(numtel))
        self.tswira=QtWidgets.QLabel()
        self.tswira.setPixmap(QtGui.QPixmap("animation\\user-6.png"))
        self.objet.addWidget(self.tswira,0,0,3,1)
        self.objet.addWidget(self.info1,0,1)
        self.objet.addWidget(self.info2,1,1)
        self.objet.addWidget(self.info3,2,1)
        self.sollicitation=QtWidgets.QLabel("Les patients qui vous ont sollicitez:")
        self.sollicitation.setFont(font)
        self.objet.addWidget(self.sollicitation,5,0,1,50)
        self.scroll=QtWidgets.QScrollArea()

        self.wid=QtWidgets.QWidget()
        self.scroll.setWidgetResizable(True)
        self.layoutte=QtWidgets.QGridLayout()
        self.wid.setLayout(self.layoutte)

        self.scroll.setWidget(self.wid)
        self.scroll.setWidgetResizable(True)
        self.scroll.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.scroll.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.objet.addWidget(self.scroll,6,0,1,50)
        self.show()

class cartep(QtWidgets.QWidget):
    def __init__(self):
        super(cartep, self).__init__()
        self.layoute=QtWidgets.QGridLayout()
        self.setLayout(self.layoute)
        self.p=None
        self.m=None
        self.sv=QtWidgets.QPushButton("save")
        self.date=QtWidgets.QDateTimeEdit() #.setMinimumDate(QDate.currentDate())
        self.date.setMinimumDate(QDate.currentDate())
        self.sv.clicked.connect(self.consult)
    def consult(self):
        #print(self.p)
        for i in wsjdid.ontologie.individuals():

            if str(i.iri) == str(self.p):
                p = i
            if str(i.iri) == str(self.m):
                m = i
        with wsjdid.ontologie:
            c= wsjdid.Consultation()
            c.DateC=self.date.text()
            p.consultant.append(c)
            m.practicien.append(c)
            wsjdid.ontologie.save(file="PROJET.owl", format="ntriples")
            wsjdid.default_world.save()
            self.msg=QtWidgets.QMessageBox()
            self.msg.setText("rdv attribué pour le "+str(self.date.text()))
            self.msg.show()
class seconnecter(QtWidgets.QWidget):
    def __init__(self):
        super(seconnecter, self).__init__()
        # self.ss=QtWidgets.QStackedLayout()
        self.name = QtWidgets.QLabel("Nom:")
        self.password = QtWidgets.QLabel("Mot de passe:")

        self.nametexte = QtWidgets.QLineEdit()
        self.passwordtexte = QtWidgets.QLineEdit()
        self.passwordtexte.setEchoMode(QtWidgets.QLineEdit.Password)

        self.layoute = QtWidgets.QGridLayout()
        #self.layoute=QtWidgets.QStackedLayout()
        self.layoute.addWidget(self.name, 0, 0)
        self.layoute.addWidget(self.password, 2, 0)
        self.layoute.addWidget(self.nametexte, 0, 1)
        self.layoute.addWidget(self.passwordtexte, 2, 1)

        self.entrer = QtWidgets.QPushButton("ENTRER")
        self.entrer.setStyleSheet("color: white;background-color: rgb(0,105,204);")

        self.layoute.addWidget(self.entrer, 4, 3)

        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.entrer.setFont(font)
        self.setLayout(self.layoute)
        #self.entrer.clicked.connect(self.bdd)


        self.show()
        self.entrer.clicked.connect(self.bdd)
    def bdd(self):
        wsjdid.sauvegarde()
        graph = wsjdid.default_world.as_rdflib_graph()
        prefixe = "prefix ns1: <http://www.w3.org/2002/07/owl#> \nprefix ns2: <file://PROJET.owl#> \nprefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \nprefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> \nprefix xml: <http://www.w3.org/XML/1998/namespace> \nprefix xsd: <http://www.w3.org/2001/XMLSchema#>\n "
        select = "SELECT DISTINCT ?name ?prenom ?tel ?age ?sexe ?nmed ?adrmed ?telmed ?y ?x\n WHERE{"
        cmd="?x a ns2:Medecin."
        cmd1="?x ns2:NomMed "+'"'+str(self.nametexte.text())+'"^^xsd:string.'
        cmd2="?x ns2:mdp "+'"'+str(self.passwordtexte.text())+'"^^xsd:string.'
        cmd11="?x ns2:NomMed ?nmed. ?x ns2:adressemed ?adrmed. ?x ns2:numtelmed ?telmed."

        cmd3="OPTIONAL {?y ns2:a_pris_rdv ?x."
        cmd4="?y ns2:Nom ?name."
        cmd5="?y ns2:Prenom ?prenom."
        cmd6="?y ns2:NumTel ?tel."
        cmd7="?y ns2:Age ?age."
        cmd8="?y ns2:Sexe ?sexe.}"
        cmd9="OPTIONAL{?y ns2:a_Pour_Maladies ?maladies}}"

        requete = prefixe + select + cmd + cmd1 +cmd2 + cmd11+cmd3+cmd4+cmd5+cmd6+cmd7+cmd8+cmd9

        res = graph.query(requete)
        res1=list(res)
        if len(res1) > 0:
            n1=str(res1[0][5])

            n2 = str(res1[0][6])
            n3 = str(res1[0][7])
            cmpt=comptemed(n1,n2,n3)
            for i in res:
                #print(i)
                p=cartep()
                if(i[0]!=None):
                    p.layoute.addWidget(QtWidgets.QLabel("NOM: "+str(i[0])),0,0)
                    p.layoute.addWidget(QtWidgets.QLabel("PRENOM: "+str(i[1])), 0, 1)
                    p.layoute.addWidget(QtWidgets.QLabel("AGE: "+str(i[3])), 1, 0)
                    p.layoute.addWidget(QtWidgets.QLabel("NUMÉRO DE TELEPHONE: " + str(i[2])), 1, 1)
                    p.layoute.addWidget(QtWidgets.QLabel("SEXE: " + str(i[4])), 0, 2)

                sel="SELECT DISTINCT ?mal\n WHERE{"
                c1="<"+str(i[8])+">"+" ns2:a_Pour_Maladies ?mal}"
                requete2=prefixe +sel+c1

                res2 = graph.query(requete2)
                x=list(res2)

                e=""
                for k in res2:
                   x=str(k)
                   x=x.split("#")
                   r=x[1].split("'")
                   e=e+"-"+r[0]+"\n"

                selt = "SELECT DISTINCT ?t\n WHERE{"
                c1t = "<" + str(i[8]) + ">" + " ns2:prend_traitement ?t}"
                requete2t = prefixe + selt + c1t

                res2t = graph.query(requete2t)
                et = ""
                for kt in res2t:
                    xt = str(kt)
                    xt = xt.split("#")
                    rt = xt[1].split("'")
                    et = et + "-" + rt[0] + "\n"
                if (i[0] != None):
                    p.layoute.addWidget(QtWidgets.QLabel("MALADIES: "),2,0)
                    p.layoute.addWidget(QtWidgets.QLabel(e),3,0)

                    p.layoute.addWidget(QtWidgets.QLabel("TRAITEMENT: "),2,2)
                    p.layoute.addWidget(QtWidgets.QLabel(et), 3, 2)
                    p.p = str(i[8])
                    p.m = str(i[9])
                    p.layoute.addWidget(p.sv,5,1)
                    p.layoute.addWidget(p.date,4,1)


                cmpt.layoutte.addWidget(p)
                line=QtWidgets.QFrame()
                line.setFrameShape(QtWidgets.QFrame.HLine)
                line.setFrameShadow(QtWidgets.QFrame.Sunken)
                cmpt.layoutte.addWidget(line)
        else:
            self.r=QtWidgets.QMessageBox()
            msg="nom d'utilisateur ou mdp erroné. veuillez réessayer."
            self.r.setText(msg)
            self.r.show()
    def rdv(self):
      #print("donner rdv")
        pass
class MenuMed(QtWidgets.QWidget):
    def __init__(self):
        super(MenuMed, self).__init__()
        self.ss = QtWidgets.QStackedLayout()

        self.Lnom = QtWidgets.QLabel("Nom:")
        self.Lnum = QtWidgets.QLabel("numero de telephone:")
        self.Ladresse = QtWidgets.QLabel("Adresse:")
        self.Lwilaya = QtWidgets.QLabel("Wilaya:")
        self.Lspecia = QtWidgets.QLabel("Specialité:")
        self.Lmdp = QtWidgets.QLabel("Mot de passe:")
        self.Ld= QtWidgets.QLabel("Domaine:")

        self.nom = QtWidgets.QLineEdit()
        self.mdp = QtWidgets.QLineEdit()
        self.mdp.setEchoMode(QtWidgets.QLineEdit.Password)
        self.adresse = QtWidgets.QLineEdit()
        self.numero = QtWidgets.QLineEdit()
        self.wilaya = QtWidgets.QComboBox()
        self.domaine=QtWidgets.QLineEdit()

        self.wilaya.addItems(
            ["", "1 - ADRAR", "2 - CHLEF", "3 - LAGHOUAT", "4 - OUM BOUAGHI", "5 - BATNA", "6 - BEJAIA", "7 - BISKRA",
             "8 - BECHAR", "9 - BLIDA", "10 - BOUIRA", "11 - TAMANRASSET", "12 - TEBESSA", "13 - TLEMCEN",
             "14 - TIARET", "15 - TIZI OUZOU", "16 - ALGER", "17 - DJELFA", "18 - JIJEL", "19 - SETIF", "20 - SAIDA",
             "21 - SKIKDA", "22 - SIDI BEL ABBES", "23 - ANNABA", "24 - GUELMA", "25 - CONSTANTINE", "26 - MEDEA",
             "27 - MOSTAGANEM", "28 - M'SILA", "29 - MASCARA", "30 - OUARGLA", "31 - ORAN", "32 - EL BAYDH",
             "33 - ILLIZI", "34 - BORDJ BOU ARRERIDJ", "35 - BOUMERDES", "36 - EL TAREF", "37 - TINDOUF",
             "38 - TISSEMSILT", "39 - EL OUED", "40 - KHENCHLA", "41 - SOUK AHRASS", "42 - TIPAZA", "43 - MILA",
             "44 - AÏN DEFLA", "45 - NÂAMA", "46 - AÏN TEMOUCHENT", "47 - GHARDAÏA", "48 - RELIZANE",
             "49-Bordj Badji Mokhtar", "50-In Salah", "51-Djanet", "52-In Guezzem", "53-El Mghaier", "54-Touggourt",
             "55-Béni Abbes", "56-Tmiminoune", "57-Ould Djelel", "58-El Menia"])

        self.specia = QtWidgets.QComboBox()
        self.specia.addItems(
            ["", "Maladies cardiovasculaires", "maladies endocriniennes", "maladies respiratoires et ORL",
             "maladies de la peau", "maladies du système digestif", "maladies rhumatologiques", "maladies des yeux",
             "maladies neurologiques et musculaires", "maladies psychiatriques et psychologiques",
             "maladies rénales, génitales et urinaires", "maladies du sang", "maladie cancéreuse"])

        self.layoute = QtWidgets.QGridLayout()

        self.layoute.addWidget(self.Lnom, 0, 0)
        self.layoute.addWidget(self.Lnum, 0, 3)
        self.layoute.addWidget(self.Ld, 0, 2)
        self.layoute.addWidget(self.domaine, 1, 2)
        self.layoute.addWidget(self.Ladresse, 2, 1)
        self.layoute.addWidget(self.Lspecia, 0, 1)
        self.layoute.addWidget(self.Lwilaya, 2, 0)
        self.layoute.addWidget(self.Lmdp, 2, 2)
        self.layoute.addWidget(self.nom, 1, 0)
        self.layoute.addWidget(self.numero, 1, 3)
        self.layoute.addWidget(self.adresse, 3, 1)
        self.layoute.addWidget(self.specia, 1, 1)
        self.layoute.addWidget(self.wilaya, 3, 0)
        self.layoute.addWidget(self.mdp, 3, 2)
        self.save = QtWidgets.QPushButton("ENREGISTRER")
        self.connecter = QtWidgets.QPushButton("SE CONNECTER")
        self.layoute.addWidget(self.save, 4, 3)
        self.layoute.addWidget(self.connecter, 5, 3)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        self.Ld.setFont(font)
        self.Lnom.setFont(font)
        self.Lnum.setFont(font)
        self.Ladresse.setFont(font)
        self.Lwilaya.setFont(font)
        self.Lspecia.setFont(font)
        self.Lmdp.setFont(font)
        self.save.setFont(font)
        self.connecter.setFont(font)
        self.save.setStyleSheet("color: white;background-color: rgb(0,105,204);")
        self.connecter.setStyleSheet("color: white;background-color: rgb(44,186,39);")
        self.save.clicked.connect(self.toubib)
        self.connecter.clicked.connect(self.pp)
        self.v = QtWidgets.QLabel("Vous etes deja inscrit? cliquez sur \'se connecter\' \n pour acceder a votre compte")

        font = QtGui.QFont()
        font.setPointSize(8)
        self.v.setFont(font)
        self.layoute.addWidget(self.v, 4, 4)
        self.setLayout(self.layoute)

        self.fen = QtWidgets.QWidget()
        self.fen.setLayout(self.ss)
        neww = seconnecter()
        self.ss.addWidget(neww)
        self.fen.setLayout(self.ss)

        self.show()

    def toubib(self):
        self.test = QtWidgets.QMessageBox()
        bool1 = re.match("\w+", self.nom.text())

        bool2 = re.match("0\d{8,9}", self.numero.text())
        bool3 = re.match("\w+", self.adresse.text())
        bool4 = re.match("\w+", self.specia.currentText())
        bool5 = re.match("\w+", self.wilaya.currentText())
        bool6 = re.match("\w{3,}", self.mdp.text())
        if (bool1 and bool2 and bool3 and bool4 and bool5 and bool6):
            path = 'medecin.xlsx'
            if (not os.path.exists(path)):
                tab = DataFrame(columns=['nom', 'specialité', 'adresse', 'tel', 'wilaya', 'mot de passe'])
                tab.to_excel(path, index=False)

            tab = pd.read_excel("medecin.xlsx", "Sheet1")
            n = tab.shape[0]
            tab.loc[n, 'nom'] = self.nom.text()
            tab.loc[n, 'specialité'] = self.specia.currentText()
            tab.loc[n, 'adresse'] = self.adresse.text()
            tab.loc[n, 'tel'] = int(self.numero.text())
            tab.loc[n, 'wilaya'] = self.wilaya.currentText()
            tab.loc[n, 'mot de passe'] = self.mdp.text()
            tab.loc[n, 'domaine'] = self.domaine.text()
            tab.drop_duplicates(keep="last", inplace=False)
            tab.to_excel(path, index=False)
            wsjdid.sauvegarde()
            namme = self.nom.text()
            namme = namme.replace(" ", "_")
            xx=namme
            str="ENREGISTREMENT AVEC SUCCÉS!!!!\nVOUS POUVEZ MAINTEMENT VOUS CONNECTER\n-nom d'utilisateur :"+xx+"\n-mot de passe :"+self.mdp.text()



        else:

            str = ""
            if (not bool1):
                str = str + "-donner un nom valide\n"
            if (not bool3):
                str = str + "-donner une adresse valide\n"
            if (not bool2):
                str = str + "-donner un numero de telephone valide\n"
            if (not bool4):
                str = str + "-indiquer une specialité\n"
            if (not bool5):
                str = str + "-indiquer la wilaya\n"
            if (not bool6):
                str = str + "-veuillez saisir un mdp d\'aumoins 3 caracteres\n"
        self.test.setText(str)
        self.test.show()

    def pp(self):

            self.objet = seconnecter()
            self.ss.setCurrentWidget(self.objet)


class maladies(QtWidgets.QWidget):
    def __init__(self):
        super(maladies, self).__init__()
        self.m = QtWidgets.QGridLayout()
        font=QtGui.QFont()
        font.setPointSize(15)
        self.l1 = QtWidgets.QLabel('Maladies Cardiovasculaires')
        self.l2 = QtWidgets.QLabel('Maladies Endocriniennes')
        self.l3 = QtWidgets.QLabel('Maladies Respiratoires et ORL')
        self.l4 = QtWidgets.QLabel('Cancers')
        self.l5 = QtWidgets.QLabel('Maladies du Sang')
        self.l6 = QtWidgets.QLabel('Maladies Rénales, génitales et Urinaires')
        self.l1.setStyleSheet("color: rgb(221,0,25); ; background-color: white")
        self.l2.setStyleSheet("color: rgb(221,0,25); ; background-color: white")
        self.l3.setStyleSheet("color: rgb(221,0,25); ; background-color: white")
        self.l4.setStyleSheet("color: rgb(221,0,25); ; background-color: white")
        self.l5.setStyleSheet("color: rgb(221,0,25); ; background-color: white")
        self.l6.setStyleSheet("color: rgb(221,0,25); ; background-color: white")
        self.l1.setFont(font)
        self.l2.setFont(font)
        self.l3.setFont(font)
        self.l4.setFont(font)
        self.l5.setFont(font)
        self.l6.setFont(font)
        self.c1 = QtWidgets.QCheckBox("")
        self.c2 = QtWidgets.QCheckBox("")
        self.c3 = QtWidgets.QCheckBox("")
        self.c4 = QtWidgets.QCheckBox("")
        self.c5 = QtWidgets.QCheckBox("")
        self.c6 = QtWidgets.QCheckBox("")
        self.t1 = QtWidgets.QLabel("Traitement:")
        self.t2 = QtWidgets.QLabel("Traitement:")
        self.t3 = QtWidgets.QLabel("Traitement:")
        self.t4 = QtWidgets.QLabel("Traitement:")
        self.t5 = QtWidgets.QLabel("Traitement:")
        self.t6 = QtWidgets.QLabel("Traitement:")
        self.texte1 = QtWidgets.QTextEdit()
        self.texte2 = QtWidgets.QTextEdit()
        self.texte3 = QtWidgets.QTextEdit()
        self.texte4 = QtWidgets.QTextEdit()
        self.texte5 = QtWidgets.QTextEdit()
        self.texte6 = QtWidgets.QTextEdit()
        self.texte7 = QtWidgets.QTextEdit()
        self.texte8 = QtWidgets.QTextEdit()
        self.texte9 = QtWidgets.QTextEdit()
        self.texte10 = QtWidgets.QTextEdit()
        self.texte11 = QtWidgets.QTextEdit()
        self.texte12 = QtWidgets.QTextEdit()

        self.m.addWidget(self.l1,0,1)
        self.m.addWidget(self.l2,0,3)
        self.m.addWidget(self.l3,0,5)
        self.m.addWidget(self.l4,4,1)
        self.m.addWidget(self.l5,4,3)
        self.m.addWidget(self.l6,4,5)
        self.m.addWidget(self.t1,2,1)
        self.m.addWidget(self.t2,2,3)
        self.m.addWidget(self.t3,2,5)
        self.m.addWidget(self.t4,6,1)
        self.m.addWidget(self.t5,6,3)
        self.m.addWidget(self.t6,6,5)
        self.m.addWidget(self.c1,0,0)
        self.m.addWidget(self.c2,0,2)
        self.m.addWidget(self.c3,0,4)
        self.m.addWidget(self.c4,4,0)
        self.m.addWidget(self.c5,4,2)
        self.m.addWidget(self.c6,4,4)
        self.m.addWidget(self.texte1,1,1)
        self.m.addWidget(self.texte2,1,3)
        self.m.addWidget(self.texte3,1,5)
        self.m.addWidget(self.texte4,3,1)
        self.m.addWidget(self.texte5,3,3)
        self.m.addWidget(self.texte6,3,5)
        self.m.addWidget(self.texte7,5,1)
        self.m.addWidget(self.texte8,5,3)
        self.m.addWidget(self.texte9,5,5)
        self.m.addWidget(self.texte10,7,1)
        self.m.addWidget(self.texte11,7,3)
        self.m.addWidget(self.texte12,7,5)
        self.c1.stateChanged.connect(self.check1)
        self.c2.stateChanged.connect(self.check2)
        self.c3.stateChanged.connect(self.check3)
        self.c4.stateChanged.connect(self.check4)
        self.c5.stateChanged.connect(self.check5)
        self.c6.stateChanged.connect(self.check6)
        self.check1()
        self.check2()
        self.check3()
        self.check4()
        self.check5()
        self.check6()
        self.setLayout(self.m)
    def check1(self):
        if (not self.c1.isChecked()):
            self.t1.hide()

            self.texte1.hide()
            self.texte4.hide()
        else:
            self.t1.show()

            self.texte1.show()
            self.texte4.show()

    def check2(self):
        if (not self.c2.isChecked()):
            self.t2.hide()

            self.texte2.hide()
            self.texte5.hide()
        else:
            self.t2.show()

            self.texte2.show()
            self.texte5.show()

    def check3(self):
        if (not self.c3.isChecked()):
            self.t3.hide()

            self.texte3.hide()
            self.texte6.hide()
        else:
            self.t3.show()

            self.texte3.show()
            self.texte6.show()

    def check4(self):
        if (not self.c4.isChecked()):
            self.t4.hide()

            self.texte7.hide()
            self.texte10.hide()
        else:
            self.t4.show()

            self.texte7.show()
            self.texte10.show()

    def check5(self):
        if (not self.c5.isChecked()):
            self.t5.hide()

            self.texte8.hide()
            self.texte11.hide()
        else:
            self.t5.show()

            self.texte8.show()
            self.texte11.show()

    def check6(self):
        if (not self.c6.isChecked()):
            self.t6.hide()

            self.texte9.hide()
            self.texte12.hide()
        else:
            self.t6.show()

            self.texte9.show()
            self.texte12.show()

class info(QtWidgets.QWidget):
    def __init__(self):
        super(info, self).__init__()
        font = QtGui.QFont()
        font.setPointSize(15)
        self.plan=QtWidgets.QGridLayout()
        self.nom=QtWidgets.QLineEdit()
        self.prenom=QtWidgets.QLineEdit()
        self.age=QtWidgets.QSpinBox()
        self.num=QtWidgets.QLineEdit()
        self.sexe=QtWidgets.QComboBox()
        self.sexe.addItems(["","Homme","Femme"])

        self.wilaya = QtWidgets.QComboBox()
        self.wilaya.addItems(["","1 - ADRAR","2 - CHLEF","3 - LAGHOUAT","4 - OUM BOUAGHI","5 - BATNA","6 - BEJAIA","7 - BISKRA","8 - BECHAR","9 - BLIDA","10 - BOUIRA","11 - TAMANRASSET","12 - TEBESSA","13 - TLEMCEN","14 - TIARET","15 - TIZI OUZOU","16 - ALGER","17 - DJELFA","18 - JIJEL","19 - SETIF","20 - SAIDA","21 - SKIKDA","22 - SIDI BEL ABBES","23 - ANNABA","24 - GUELMA","25 - CONSTANTINE","26 - MEDEA","27 - MOSTAGANEM","28 - M'SILA","29 - MASCARA","30 - OUARGLA","31 - ORAN","32 - EL BAYDH","33 - ILLIZI","34 - BORDJ BOU ARRERIDJ","35 - BOUMERDES","36 - EL TAREF","37 - TINDOUF","38 - TISSEMSILT","39 - EL OUED","40 - KHENCHLA","41 - SOUK AHRASS","42 - TIPAZA","43 - MILA","44 - AÏN DEFLA","45 - NÂAMA","46 - AÏN TEMOUCHENT","47 - GHARDAÏA","48 - RELIZANE", "49-Bordj Badji Mokhtar", "50-In Salah", "51-Djanet", "52-In Guezzem", "53-El Mghaier", "54-Touggourt", "55-Béni Abbes", "56-Tmiminoune", "57-Ould Djelel", "58-El Menia"])
        self.com = QtWidgets.QLineEdit()
        self.cnom=QtWidgets.QLabel("Nom:")
        self.cprenom=QtWidgets.QLabel("Prenom:")
        self.cage=QtWidgets.QLabel("Age:")
        self.cnum=QtWidgets.QLabel("Numero de telephone:")
        self.csexe=QtWidgets.QLabel("sexe:")
        self.cwilaya = QtWidgets.QLabel("Wilaya:")
        self.ccom = QtWidgets.QLabel("Commune:")
        self.plan.addWidget(self.cnom,0,0)
        self.plan.addWidget(self.cprenom, 0, 1)
        self.plan.addWidget(self.cage, 0, 2)
        self.plan.addWidget(self.cnum, 2, 0)
        self.plan.addWidget(self.csexe, 2, 1)
        self.plan.addWidget(self.cwilaya, 2, 2)
        self.plan.addWidget(self.ccom, 2, 3)

        self.plan.addWidget(self.nom, 1, 0)
        self.plan.addWidget(self.prenom, 1, 1)
        self.plan.addWidget(self.age, 1, 2)
        self.plan.addWidget(self.num, 3, 0)
        self.plan.addWidget(self.sexe, 3, 1)
        self.plan.addWidget(self.wilaya, 3, 2)
        self.plan.addWidget(self.com, 3, 3)
        self.cnom.setFont(font)
        self.cprenom.setFont(font)
        self.cage.setFont(font)
        self.cnum.setFont(font)
        self.csexe.setFont(font)
        self.cwilaya.setFont(font)
        self.ccom.setFont(font)
        self.setLayout(self.plan)

class jrs(QtWidgets.QWidget):
    def __init__(self):
        super(jrs, self).__init__()
        self.question=QtWidgets.QLabel('Depuis quand avez-vous ces symptomes?')
        self.question.setStyleSheet("color: rgb(221,0,25) ; background-color: white;")
        test=self.question.font()
        test.setPointSize(22)
        self.question.setFont(test)
        self.choix=QtWidgets.QComboBox()
        self.choix.addItems(["",'1-3 jrs','4-8 jrs','+8 jrs'])
        self.layoute=QtWidgets.QGridLayout()

        self.remplir=QtWidgets.QLabel('Sélectionnez une option :')
        test = self.remplir.font()
        test.setPointSize(15)
        self.remplir.setFont(test)
        self.layoute.addWidget(self.question, 0, 0)
        self.layoute.addWidget(self.choix, 2, 0)
        self.layoute.addWidget(self.remplir, 1, 0)
        self.setLayout(self.layoute)


class ouinon(QtWidgets.QWidget):
    def __init__(self,s,p=None):
        super(ouinon, self).__init__()
        self.question=QtWidgets.QLabel(s)
        self.question.setStyleSheet("color: rgb(221,0,25) ; background-color: white")

        test=self.question.font()
        test.setPointSize(22)
        self.question.setFont(test)
        self.remplir=QtWidgets.QLabel('Sélectionnez une option :')
        test = self.remplir.font()
        test.setPointSize(15)
        self.remplir.setFont(test)
        self.oui=QtWidgets.QRadioButton('Oui')

        self.oui.setFont(test)
        self.non=QtWidgets.QRadioButton('Non')
        self.non.setFont(test)
        self.layoute=QtWidgets.QGridLayout()
        self.setLayout(self.layoute)
        self.layoute.addWidget(self.question,0,0,1,3)
        self.layoute.addWidget(self.remplir,2,0)
        self.layoute.addWidget(self.oui,3,0)
        self.layoute.addWidget(self.non,3,1)
        if(p!=None):
            self.gif=QtWidgets.QLabel()
            test = QtGui.QMovie(p)
            test.start()
            self.gif.setMovie(test)
            self.layoute.addWidget(self.gif,1,0)


class maladieschron(QtWidgets.QWidget):
    def __init__(self):
        super(maladieschron, self).__init__()
        self.m = QtWidgets.QGridLayout()
        font=QtGui.QFont()
        font.setPointSize(15)
        self.l1 = QtWidgets.QLabel('Maladies Cardiovasculaires')
        self.l1.setStyleSheet("color:rgb(221,0,25);  background-color:white;")
        self.l2 = QtWidgets.QLabel('Maladies Endocriniennes')
        self.l2.setStyleSheet("color:rgb(221,0,25);  background-color:white;")

        self.l3 = QtWidgets.QLabel('Maladies Respiratoires et ORL')
        self.l3.setStyleSheet("color:rgb(221,0,25);  background-color:white;")

        self.l4 = QtWidgets.QLabel('Cancers')
        self.l4.setStyleSheet("color:rgb(221,0,25);  background-color:white;")

        self.l5 = QtWidgets.QLabel('Maladies du Sang')
        self.l5.setStyleSheet("color:rgb(221,0,25);  background-color:white;")

        self.l6 = QtWidgets.QLabel('Maladies Rénales, génitales et Urinaires')
        self.l6.setStyleSheet("color:rgb(221,0,25);  background-color:white;")

        self.l7 = QtWidgets.QLabel('Maladies Neurologiques et Musculaires')
        self.l7.setStyleSheet("color:rgb(221,0,25);  background-color:white;")

        self.l8 = QtWidgets.QLabel('Maladies Psychiatriques et Psychologiques')
        self.l8.setStyleSheet("color:rgb(221,0,25);  background-color:white;")

        self.l9 = QtWidgets.QLabel('Maladies des Yeux')
        self.l9.setStyleSheet("color:rgb(221,0,25);  background-color:white;")

        self.l10 = QtWidgets.QLabel('maladies du Système Digestif')
        self.l10.setStyleSheet("color:rgb(221,0,25);  background-color:white;")

        self.l11 = QtWidgets.QLabel('Maladies Rhumatologiques')
        self.l11.setStyleSheet("color:rgb(221,0,25);  background-color:white;")

        self.l12 = QtWidgets.QLabel('Maladies de la Peau')
        self.l12.setStyleSheet("color:rgb(221,0,25);  background-color:white;")

        self.l1.setFont(font)
        self.l2.setFont(font)
        self.l3.setFont(font)
        self.l4.setFont(font)
        self.l5.setFont(font)
        self.l6.setFont(font)
        self.l7.setFont(font)
        self.l8.setFont(font)
        self.l9.setFont(font)
        self.l10.setFont(font)
        self.l11.setFont(font)
        self.l12.setFont(font)
        self.c1 = QtWidgets.QCheckBox("")
        self.c2 = QtWidgets.QCheckBox("")
        self.c3 = QtWidgets.QCheckBox("")
        self.c4 = QtWidgets.QCheckBox("")
        self.c5 = QtWidgets.QCheckBox("")
        self.c6 = QtWidgets.QCheckBox("")
        self.c7 = QtWidgets.QCheckBox("")
        self.c8 = QtWidgets.QCheckBox("")
        self.c9 = QtWidgets.QCheckBox("")
        self.c10 = QtWidgets.QCheckBox("")
        self.c11 = QtWidgets.QCheckBox("")
        self.c12 = QtWidgets.QCheckBox("")
        self.t1 = QtWidgets.QLabel("Traitement:")
        self.t2 = QtWidgets.QLabel("Traitement:")
        self.t3 = QtWidgets.QLabel("Traitement:")
        self.t4 = QtWidgets.QLabel("Traitement:")
        self.t5 = QtWidgets.QLabel("Traitement:")
        self.t6 = QtWidgets.QLabel("Traitement:")
        self.t7 = QtWidgets.QLabel("Traitement:")
        self.t8 = QtWidgets.QLabel("Traitement:")
        self.t9 = QtWidgets.QLabel("Traitement:")
        self.t10 = QtWidgets.QLabel("Traitement:")
        self.t11 = QtWidgets.QLabel("Traitement:")
        self.t12 = QtWidgets.QLabel("Traitement:")
        self.texte1 = QtWidgets.QTextEdit()
        self.texte2 = QtWidgets.QTextEdit()
        self.texte3 = QtWidgets.QTextEdit()
        self.texte4 = QtWidgets.QTextEdit()
        self.texte5 = QtWidgets.QTextEdit()
        self.texte6 = QtWidgets.QTextEdit()
        self.texte7 = QtWidgets.QTextEdit()
        self.texte8 = QtWidgets.QTextEdit()
        self.texte9 = QtWidgets.QTextEdit()
        self.texte10 = QtWidgets.QTextEdit()
        self.texte11 = QtWidgets.QTextEdit()
        self.texte12 = QtWidgets.QTextEdit()
        self.texte13 = QtWidgets.QTextEdit()
        self.texte14 = QtWidgets.QTextEdit()
        self.texte15 = QtWidgets.QTextEdit()
        self.texte16 = QtWidgets.QTextEdit()
        self.texte17 = QtWidgets.QTextEdit()
        self.texte18 = QtWidgets.QTextEdit()
        self.texte19 = QtWidgets.QTextEdit()
        self.texte20 = QtWidgets.QTextEdit()
        self.texte21 = QtWidgets.QTextEdit()
        self.texte22 = QtWidgets.QTextEdit()
        self.texte23 = QtWidgets.QTextEdit()
        self.texte24 = QtWidgets.QTextEdit()


        self.m.addWidget(self.l1,0,1)
        self.m.addWidget(self.l2,0,3)
        self.m.addWidget(self.l3,0,5)
        self.m.addWidget(self.l4,4,1)
        self.m.addWidget(self.l5,4,3)
        self.m.addWidget(self.l6,4,5)
        self.m.addWidget(self.l7,8,1)
        self.m.addWidget(self.l8,8,3)
        self.m.addWidget(self.l9,8,5)
        self.m.addWidget(self.l10,12,1)
        self.m.addWidget(self.l11,12,3)
        self.m.addWidget(self.l12,12,5)

        self.m.addWidget(self.t1,2,1)
        self.m.addWidget(self.t2,2,3)
        self.m.addWidget(self.t3,2,5)
        self.m.addWidget(self.t4,6,1)
        self.m.addWidget(self.t5,6,3)
        self.m.addWidget(self.t6,6,5)
        self.m.addWidget(self.t7,10,1)
        self.m.addWidget(self.t8,10,3)
        self.m.addWidget(self.t9,10,5)
        self.m.addWidget(self.t10,14,1)
        self.m.addWidget(self.t11,14,3)
        self.m.addWidget(self.t12,14,5)

        self.m.addWidget(self.c1,0,0)
        self.m.addWidget(self.c2,0,2)
        self.m.addWidget(self.c3,0,4)
        self.m.addWidget(self.c4,4,0)
        self.m.addWidget(self.c5,4,2)
        self.m.addWidget(self.c6,4,4)
        self.m.addWidget(self.c7,8,0)
        self.m.addWidget(self.c8,8,2)
        self.m.addWidget(self.c9,8,4)
        self.m.addWidget(self.c10,12,0)
        self.m.addWidget(self.c11,12,2)
        self.m.addWidget(self.c12,12,4)

        self.m.addWidget(self.texte1,1,1)
        self.m.addWidget(self.texte2,1,3)
        self.m.addWidget(self.texte3,1,5)
        self.m.addWidget(self.texte4,3,1)
        self.m.addWidget(self.texte5,3,3)
        self.m.addWidget(self.texte6,3,5)
        self.m.addWidget(self.texte7,5,1)
        self.m.addWidget(self.texte8,5,3)
        self.m.addWidget(self.texte9,5,5)
        self.m.addWidget(self.texte10,7,1)
        self.m.addWidget(self.texte11,7,3)
        self.m.addWidget(self.texte12,7,5)
        self.m.addWidget(self.texte13,9,1)
        self.m.addWidget(self.texte14,9,3)
        self.m.addWidget(self.texte15,9,5)
        self.m.addWidget(self.texte16,11,1)
        self.m.addWidget(self.texte17,11,3)
        self.m.addWidget(self.texte18,11,5)
        self.m.addWidget(self.texte19,13,1)
        self.m.addWidget(self.texte20,13,3)
        self.m.addWidget(self.texte21,13,5)
        self.m.addWidget(self.texte22,15,1)
        self.m.addWidget(self.texte23,15,3)
        self.m.addWidget(self.texte24,15,5)

        self.c1.stateChanged.connect(self.check1)
        self.c2.stateChanged.connect(self.check2)
        self.c3.stateChanged.connect(self.check3)
        self.c4.stateChanged.connect(self.check4)
        self.c5.stateChanged.connect(self.check5)
        self.c6.stateChanged.connect(self.check6)
        self.c7.stateChanged.connect(self.check7)
        self.c8.stateChanged.connect(self.check8)
        self.c9.stateChanged.connect(self.check9)
        self.c10.stateChanged.connect(self.check10)
        self.c11.stateChanged.connect(self.check11)
        self.c12.stateChanged.connect(self.check12)

        self.check1()
        self.check2()
        self.check3()
        self.check4()
        self.check5()
        self.check6()
        self.check7()
        self.check8()
        self.check9()
        self.check10()
        self.check11()
        self.check12()
        self.setLayout(self.m)
        self.show()
    def check1(self):
        if (not self.c1.isChecked()):
            self.t1.hide()

            self.texte1.hide()
            self.texte4.hide()
        else:
            self.t1.show()

            self.texte1.show()
            self.texte4.show()

    def check2(self):
        if (not self.c2.isChecked()):
            self.t2.hide()

            self.texte2.hide()
            self.texte5.hide()
        else:
            self.t2.show()

            self.texte2.show()
            self.texte5.show()

    def check3(self):
        if (not self.c3.isChecked()):
            self.t3.hide()

            self.texte3.hide()
            self.texte6.hide()
        else:
            self.t3.show()

            self.texte3.show()
            self.texte6.show()

    def check4(self):
        if (not self.c4.isChecked()):
            self.t4.hide()

            self.texte7.hide()
            self.texte10.hide()
        else:
            self.t4.show()

            self.texte7.show()
            self.texte10.show()

    def check5(self):
        if (not self.c5.isChecked()):
            self.t5.hide()

            self.texte8.hide()
            self.texte11.hide()
        else:
            self.t5.show()

            self.texte8.show()
            self.texte11.show()

    def check6(self):
        if (not self.c6.isChecked()):
            self.t6.hide()

            self.texte9.hide()
            self.texte12.hide()
        else:
            self.t6.show()

            self.texte9.show()
            self.texte12.show()

    def check7(self):
        if (not self.c7.isChecked()):
            self.t7.hide()

            self.texte13.hide()
            self.texte16.hide()
        else:
            self.t7.show()

            self.texte13.show()
            self.texte16.show()

    def check8(self):
        if (not self.c8.isChecked()):
            self.t8.hide()

            self.texte14.hide()
            self.texte17.hide()
        else:
            self.t8.show()

            self.texte14.show()
            self.texte17.show()

    def check9(self):
        if (not self.c9.isChecked()):
            self.t9.hide()

            self.texte15.hide()
            self.texte18.hide()
        else:
            self.t9.show()

            self.texte15.show()
            self.texte18.show()

    def check10(self):
        if (not self.c10.isChecked()):
            self.t10.hide()

            self.texte19.hide()
            self.texte22.hide()
        else:
            self.t10.show()

            self.texte19.show()
            self.texte22.show()

    def check11(self):
        if (not self.c11.isChecked()):
            self.t11.hide()

            self.texte20.hide()
            self.texte23.hide()
        else:
            self.t11.show()

            self.texte20.show()
            self.texte23.show()

    def check12(self):
        if (not self.c12.isChecked()):
            self.t12.hide()

            self.texte21.hide()
            self.texte24.hide()
        else:
            self.t12.show()

            self.texte21.show()
            self.texte24.show()


x=['Avez-vous une forte fievre?',
  'Ces derniers jours, avez-vous une toux ou une augmentation\n de votre toux habituelle ?',
  'Ces derniers jours, avez-vous noté une forte diminution \nou perte de votre goût ou de votre odorat ?',
  'Ces derniers jours, avez-vous eu un mal de gorge?',
  'Ces derniers jours, avez-vous des douleurs musculaires \net/ou des courbatures inhabituelles ?',
  'Avez-vous de la diarrhée ? ',
  'Ces derniers jours, avez-vous une fatigue inhabituelle ?',
  'Avez-vous eu un mal de tete?',
  'Avez-vous noté un manque de souffle inhabituel \nlorsque vous parlez ou faites un petit effort ?',
   'Avez-vous des douleurs au niveau de la poitrine?',
   'Etes-vous enceinte?',"Avez-vous une obésité de classe lll (morbide, IMC ≥ 40 kg/m2)? \n (L'indice de masse corporelle est calculé en divisant\nle poids par la taille au carré)"
   ]

class regrouper(QtWidgets.QWidget):
    def __init__(self):
        super(regrouper, self).__init__()
        self.groupe=QtWidgets.QStackedLayout()

        self.liste=[]
        self.chronique=maladieschron()
        self.chronique.setStyleSheet("background-color: white;")
        self.suivant=QtWidgets.QPushButton("TEST COVID-19")
        self.enceinte=QtWidgets.QPushButton("Suivi Grossesse")
        self.chron = QtWidgets.QPushButton("MALADIES CHRONIQUES")
        self.suivant.setStyleSheet("color:white;  background-color:rgb(221,0,25);")
        self.chron.setStyleSheet("color:white;  background-color:rgb(221,0,25);")
        self.enceinte.setStyleSheet("color:white;  background-color:rgb(221,0,25);")
        self.setStyleSheet("background-color: white;")
        #self.suivant.setStyleSheet("color: white; background-color: blue")
        font=QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        #font.setPointSize(13)
        #font.setBold(False)
        #self.prambule.setFont(font)
        self.suivant.setFont(font)
        self.chron.setFont(font)

        self.enceinte.setFont(font)
        self.boite=QtWidgets.QWidget()
        self.boite.setLayout(self.groupe)
        #self.setStyleSheet("background-color: yellow")
        var = info()
        var.setStyleSheet("background-color: white;")
        self.liste.append(var)
        self.groupe.addWidget(var)
        #var.styleSheet("background-color: white;")
        for i in range(len(x)):

         var = ouinon(x[i])
         var.setStyleSheet("background-color: white;")
         var.oui.toggled.connect(self.enable)
         var.non.toggled.connect(self.enable)
         self.liste.append(var)
         self.groupe.addWidget(var)
         self.layoute=QtWidgets.QGridLayout()
        self.suivant.clicked.connect(self.qs)
        self.chron.clicked.connect(self.Mchron)
        self.enceinte.clicked.connect(self.fe)
        self.liste[0].sexe.currentTextChanged.connect(self.changement)



        #self.layoute.addWidget(self.prambule,0,0,1,3)
        self.layoute.addWidget(self.boite,1,0,1,2)
        self.layoute.addWidget(self.suivant,2,2)
        self.layoute.addWidget(self.chron, 2, 0)
        self.layoute.addWidget(self.enceinte,2,1)
        self.setLayout(self.layoute)
        #self.suivant.setEnabled(False)

        var=jrs()
        self.liste.append(var)
        self.groupe.addWidget(var)
        self.index=0
        var.setStyleSheet("background-color: white;")
        var = maladies()
        var.setStyleSheet("background-color: white;")
        self.liste.append(var)
        self.groupe.addWidget(var)
        self.groupe.setCurrentWidget(self.liste[self.index])
        self.groupe.addWidget(self.chronique)
        #self.attente = chargment()
        self.show()
    def changement(self):
        if(self.liste[0].sexe.currentText()=="Homme"):
            self.enceinte.setStyleSheet("color: rgb(120,120,120); background-color: rgb(204,204,204);")


            self.enceinte.setEnabled(False)

        else:
            self.enceinte.setStyleSheet("color:white;  background-color:rgb(221,0,25);")

            self.enceinte.setEnabled(True)
    def Mchron(self):
        if(self.verifierInfo()):
            self.index=len(self.liste)-1
            self.groupe.setCurrentWidget(self.chronique)#self.liste[len(self.liste)-1])
            #self.chron.hide()
            self.chron.setText("ENREGISTRER")
            self.suivant.hide()
            self.enceinte.hide()
            self.chron.clicked.connect(self.enrem)
    def enrem(self):
        path = 'test.xlsx'
        if (not os.path.exists(path)):
            df = DataFrame(columns=['nom', 'prenom', 'sexe', 'age', 'tel', 'wilaya', 'commune', 'symptomes',
                                    'Symptômes graves', 'depuis quand avez-vous ces symptomes?',
                                    'Maladie chronique', 'femme enceinte',"soumna"])
            df.to_excel("test.xlsx", index=False)

        df = pd.read_excel("test.xlsx", "Sheet1")
        n5 = df.shape[0]
        df.loc[n5, 'nom'] = self.liste[0].nom.text()
        df.loc[n5, 'prenom'] = self.liste[0].prenom.text()
        df.loc[n5, 'sexe'] = self.liste[0].sexe.currentText()
        df.loc[n5, 'age'] = int(self.liste[0].age.text())
        df.loc[n5, 'tel'] = int(self.liste[0].num.text())
        df.loc[n5, 'wilaya'] = self.liste[0].wilaya.currentText()
        df.loc[n5, 'commune'] = self.liste[0].com.text()
        df.loc[n5, 'soumna'] = "///"
        maladie = ""
        if (self.chronique.c1.isChecked()):
            g = self.chronique.texte1
            u = self.chronique.texte4
            maladie = maladie + "{Maladies cardiovasculaires:" + g.toPlainText() + ",traitement:" + u.toPlainText() + "}"
        if (self.chronique.c2.isChecked()):
            g = self.chronique.texte2
            u = self.chronique.texte5
            maladie = maladie + "{maladies endocriniennes:" + g.toPlainText() + ",traitement:" + u.toPlainText() + "}"
        if (self.chronique.c3.isChecked()):
            g = self.chronique.texte3
            u = self.chronique.texte6
            maladie = maladie + "{maladies respiratoires et ORL:" + g.toPlainText() + ",traitement:" + u.toPlainText() + "}"
        if (self.chronique.c4.isChecked()):
            g = self.chronique.texte7
            u = self.chronique.texte10
            maladie = maladie + "{maladie cancéreuse:" + g.toPlainText() + ",traitement:" + u.toPlainText() + "}"
        if (self.chronique.c5.isChecked()):
            g = self.chronique.texte8
            u = self.chronique.texte11
            maladie = maladie + "{maladies du sang:" + g.toPlainText() + ",traitement:" + u.toPlainText() + "}"
        if (self.chronique.c6.isChecked()):
            g = self.chronique.texte9
            u = self.chronique.texte12
            maladie = maladie + "{maladies rénales, génitales et urinaires:" + g.toPlainText() + ",traitement:" + u.toPlainText() + "}"
        if (self.chronique.c7.isChecked()):
            g = self.chronique.texte13
            u = self.chronique.texte16
            maladie = maladie + "{maladies neurologiques et musculaires:" + g.toPlainText() + ",traitement:" + u.toPlainText() + "}"
        if (self.chronique.c8.isChecked()):
            g = self.chronique.texte14
            u = self.chronique.texte17
            maladie = maladie + "{maladies psychiatriques et psychologiques:" + g.toPlainText() + ",traitement:" + u.toPlainText() + "}"
        if (self.chronique.c9.isChecked()):
            g = self.chronique.texte15
            u = self.chronique.texte18
            maladie = maladie + "{maladies des yeux:" + g.toPlainText() + ",traitement:" + u.toPlainText() + "}"
        if (self.chronique.c10.isChecked()):
            g = self.chronique.texte19
            u = self.chronique.texte22
            maladie = maladie + "{maladies système digestif:" + g.toPlainText() + ",traitement:" + u.toPlainText() + "}"
        if (self.chronique.c11.isChecked()):
            g = self.chronique.texte20
            u = self.chronique.texte23
            maladie = maladie + "{maladies rhumatologiques:" + g.toPlainText() + ",traitement:" + u.toPlainText() + "}"
        if (self.chronique.c12.isChecked()):
            g = self.chronique.texte21
            u = self.chronique.texte24
            maladie = maladie + "{maladies de la peau:" + g.toPlainText() + ",traitement:" + u.toPlainText() + "}"

        df.loc[n5, 'Maladie chronique'] = maladie
        df.to_excel("test.xlsx",index=False)
        wsjdid.sauvegarde()
        graph = wsjdid.default_world.as_rdflib_graph()
        prefixe = "prefix ns1: <http://www.w3.org/2002/07/owl#> \nprefix ns2: <file://PROJET.owl#> \nprefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \nprefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> \nprefix xml: <http://www.w3.org/XML/1998/namespace> \nprefix xsd: <http://www.w3.org/2001/XMLSchema#>\n "
        select = "SELECT DISTINCT ?nom ?adr ?num ?dm ?x ?y\n WHERE{"
        cmd = "?x a ns2:Medecin ."
        cmd1 = "?y ns2:Nom " + '"' + str(self.liste[0].nom.text()) + '"^^xsd:string.'
        cmd2 = "?y ns2:Prenom " + '"' + str(self.liste[0].prenom.text()) + '"^^xsd:string .'
        cmd3 ="?x ns2:habite_a ?z."
        cmd4 ="?y a ns2:MaladeChronique."

        cmd5="?y ns2:habite_a ?z."
        cmd6="?y ns2:a_Pour_Maladies ?t.?t ns2:typemaladie ?v.?x ns2:specialité ?v."
        cmd61="?x ns2:domaine ?dm."
        cmd7="?x ns2:NomMed ?nom.?x ns2:adressemed ?adr.?x ns2:numtelmed ?num}"
        cmd8="ORDER BY DESC(?dm)"
        requete = prefixe + select + cmd + cmd1 + cmd2+cmd3 +cmd4+cmd5+cmd6+cmd61+cmd7 +cmd8
        #print(requete)
        res = graph.query(requete)
        print("batata")
        prediction = []
        for i in res:
            x=[]
            x.append(str(i[0]))
            x.append(str(i[1]))
            x.append(str(i[2]))
            x.append(str(i[3]))
            x.append(i[4])
            x.append(i[5])
            prediction.append(x)
        men=fiche()
        for i in range(0,len(prediction)):
            afficher = carte(prediction[i][0], prediction[i][1], prediction[i][2],prediction[i][3])
            afficher.toubib=prediction[i][4]
            afficher.patient = prediction[i][5]
            men.layoute.addWidget(afficher,i,0)
            men.setWindowTitle("liste de medecin de la wilaya "+str(self.liste[0].wilaya.currentText()))
        print("fin")

    def enable(self):
        var=self.groupe.currentWidget()
        if(var.oui.isChecked() or var.non.isChecked()):
            self.suivant.setEnabled(True)
            self.suivant.setText('Suivant  →')

            self.suivant.setStyleSheet ("color:white;  background-color:rgb(221,0,25);")
    def verifierInfo(self):
        x = self.liste[0].nom
        bool1 = re.match("\w+", x.text())
        y = self.liste[0].prenom
        bool2 = re.match("\w+", y.text())
        z = self.liste[0].num
        bool3 = re.match("0\d{9,9}", z.text())
        a = self.liste[0].age
        bool4 = int(a.text()) > 0
        b =self.liste[0].sexe
        bool5 = re.match("Homme|Femme", b.currentText())
        c = self.liste[0].wilaya
        bool6 = re.match("\w+", c.currentText())
        if (bool1 and bool2 and bool3 and bool4 and bool5 and bool6):
            return True
        else:
            self.test = QtWidgets.QMessageBox()
            str = ""
            if (not bool1):
                str = str + "-donner un nom valide\n"
            if (not bool2):
                str = str + "-donner un prenom valide\n"
            if (not bool3):
                str = str + "-donner un numero de telephone valide\n"
            if (not bool4):
                str = str + "-donner un age valide\n"
            if (not bool5):
                str = str + "-indiquer le sexe\n"
            if (not bool6):
                str = str + "-indiquer votre wilaya\n"
            self.test.setWindowTitle("erreur")
            self.test.setText(str)
            self.test.show()
            return False
    def qs(self):


        if self.index==0:
            if self.verifierInfo():
                self.groupe.setCurrentWidget(self.liste[self.index])
                if self.index < len(self.liste) - 1:
                    self.suivant.setEnabled(False)
                    self.suivant.setText('Suivant  →')
                    self.suivant.setStyleSheet("color: rgb(120,120,120);background-color: rgb(204,204,204);")
                    self.chron.hide()
                    self.enceinte.hide()
                    self.index = self.index + 1

        if self.index<len(self.liste)-1:
           if self.index != 0:

            self.index = self.index + 1
            if(self.liste[0].sexe.currentText()=='Femme'):
             self.groupe.setCurrentWidget(self.liste[self.index])
            else:
                if(self.index==len(self.liste)-4):
                    self.index = self.index + 1
                    self.groupe.setCurrentWidget(self.liste[self.index])
                else:
                    self.groupe.setCurrentWidget(self.liste[self.index])
            if self.index < len(self.liste)-2:

                self.suivant.setEnabled(False)
                self.suivant.setText('Suivant  →')

                self.suivant.setStyleSheet("color: rgb(120,120,120);background-color: rgb(204,204,204);")

           if self.index == len(self.liste)-1:
               self.suivant.setText('Enregistrer')
        else:

            #attente=chargment()
            #attente.show()

            self.suivant.setText('Enregistrer')
            path = 'test.xlsx'
            if (not os.path.exists(path)):
                df = DataFrame(columns=['nom', 'prenom', 'sexe', 'age', 'tel', 'wilaya', 'commune', 'symptomes',
                                        'Symptômes graves', 'depuis quand avez-vous ces symptomes?',
                                        'Maladie chronique','femme enceinte',"soumna"])
                df.to_excel("test.xlsx", index=False)

            df = pd.read_excel("test.xlsx", "Sheet1")
            n = df.shape[0]
            chaine=""
            symptomes=["","fièvre|","toux sèche|","perte odorat ou goût|","maux de gorge|","courbatures|",
                       "diarrhée|","fatigue|","maux de tête|","difficultés à respirer ou essoufflement|",
                       "sensation d oppression ou douleur au niveau de la poitrine|"]

            for i in range(1,9):
                if self.liste[i].oui.isChecked():
                    chaine=chaine + symptomes[i]
            df.loc[n,'symptomes']=chaine
            chaineg=""
            for i in range(9,11):
                if self.liste[i].oui.isChecked():
                    chaineg = chaineg + symptomes[i]

            df.loc[n,'Symptômes graves']=chaineg

            if(self.liste[11].oui.isChecked()):
                df.loc[n,'femme enceinte']='oui'
            else:
                if(self.liste[11].non.isChecked()):
                 df.loc[n, 'femme enceinte']='non'
            if (self.liste[12].oui.isChecked()):
                df.loc[n, 'soumna'] = 'oui'
            else:
                if(self.liste[12].non.isChecked()):
                 df.loc[n, 'soumna']='non'
            df.loc[n, 'nom'] = self.liste[0].nom.text()
            df.loc[n, 'prenom'] = self.liste[0].prenom.text()
            df.loc[n, 'sexe'] =self.liste[0].sexe.currentText()
            df.loc[n, 'age'] = int(self.liste[0].age.text())
            df.loc[n, 'tel'] =int(self.liste[0].num.text())
            df.loc[n, 'wilaya'] = self.liste[0].wilaya.currentText()
            df.loc[n, 'commune'] = self.liste[0].com.text()

            maladie = ""
            if (self.liste[self.index].c1.isChecked()):
                g = self.liste[self.index].texte1
                u = self.liste[self.index].texte4
                maladie = maladie + "{Maladies cardiovasculaires:" + g.toPlainText() + ",traitement:" + u.toPlainText() + "}"
            if (self.liste[self.index].c2.isChecked()):
                g = self.liste[self.index].texte2
                u = self.liste[self.index].texte5
                maladie = maladie + "{Maladies Endocriniennes:" + g.toPlainText() + ",traitement:" + u.toPlainText() + "}"
            if (self.liste[self.index].c3.isChecked()):
                g = self.liste[self.index].texte3
                u = self.liste[self.index].texte6
                maladie = maladie + "{Maladies Respiratoires et ORL:" + g.toPlainText() + ",traitement:" + u.toPlainText() + "}"
            if (self.liste[self.index].c4.isChecked()):
                g = self.liste[self.index].texte7
                u = self.liste[self.index].texte10
                maladie = maladie + "{Cancers:" + g.toPlainText() + ",traitement:" + u.toPlainText() + "}"
            if (self.liste[self.index].c5.isChecked()):
                g = self.liste[self.index].texte8
                u = self.liste[self.index].texte11
                maladie = maladie + "{Maladies du Sang:" + g.toPlainText() + ",traitement:" + u.toPlainText() + "}"
            if (self.liste[self.index].c6.isChecked()):
                g = self.liste[self.index].texte9
                u = self.liste[self.index].texte12
                maladie = maladie + "{Maladies Rénales, génitales et Urinaires:" + g.toPlainText() + ",traitement:" + u.toPlainText() + "}"


            df.loc[n,'Maladie chronique']=maladie

            df.loc[n,'depuis quand avez-vous ces symptomes?']=self.liste[13].choix.currentText()
            df.to_excel("test.xlsx", index=False)
            test = QProcess()
            test.start("python process.py")
            wsjdid.sauvegarde()
            graph = wsjdid.default_world.as_rdflib_graph()
            prefixe = "prefix ns1: <http://www.w3.org/2002/07/owl#> \nprefix ns2: <file://PROJET.owl#> \nprefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \nprefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> \nprefix xml: <http://www.w3.org/XML/1998/namespace> \nprefix xsd: <http://www.w3.org/2001/XMLSchema#>\n "
            select = "SELECT DISTINCT ?diag ?y \n WHERE{"
            cmd = "?x a ?diag .\n"
            cmd3 = "?x ns2:habite_a ?y."
            cmd1 = "?x ns2:Nom " + '"' + str(self.liste[0].nom.text()) + '"^^xsd:string .'
            cmd2 = "?x ns2:Prenom " + '"' + str(self.liste[0].prenom.text()) + '"^^xsd:string}'

            requete = prefixe + select + cmd + cmd3 + cmd1 + cmd2
            # print(requete)

            res = graph.query(requete)
            prediction = []
            # print(res)
            for i in res:
                #   print(i)
                x = str(i[0])
                x = x.split("#")
                prediction.append(x[1])
                y = str(i[1])
                #print(y)
                prediction.append(y)
            #print(prediction)
            self.message = QtWidgets.QMessageBox()
            self.message.setWindowTitle("Diagnostic")
            if "pCovid_grave" in prediction:
                chaine = "Cher(e) " + self.liste[0].nom.text() + " " + self.liste[
                    0].prenom.text() + "\nD\'apres vos reponses a ce questionnaire, vous semblez etre atteint du Covid-19. \nVous devez etre hospitaliser en urgence, veuillez vous dirigez vers l\'un des hopitaux de la wilaya de " + \
                         self.liste[0].wilaya.currentText()+" ou l'un des établissements de santé à proximité."
                # chaine=chaine+
                select1 = "SELECT ?h\nWHERE{ <" + y + "> ns2:contient_hopital ?h}"
                #print(select1)
                requete1 = prefixe + select1
                res1 = graph.query(requete1)
                p = "\n"
                for i in res1:
                    x = str(i[0])
                    x = x.split("#")

                    p = p + "-" + x[1] + "\n"
                chaine = chaine + p +"\nNB: veuillez prévenir les gens avec lesquels vous étiez en contact derniérement" \
                                     "\nveuillez leurs demander d'aller se faire dépister. "

            else :

                    if"pCovid_Depistage" in prediction:
                        chaine = "Cher(e) " + self.liste[0].nom.text() + " " + self.liste[
                            0].prenom.text() + "\nD\'apres vos reponses a ce questionnaire, vous semblez avoir des symptomes qui peuvent etre relier au Covid.\nNous ne pouvons malheureusement pas vous le confirmer, nous vous recommandons donc d\'effectuer un test PCR¹ dans les laboratoires les plus proches " + \
                                 "\nNB: veuillez prévenir les gens avec lesquels vous étiez en contact derniérement."+"\n\n\nLe test PCR¹ permet de détecter la présence du virus au moment où le patient effectue le test."
                    else:
                        chaine = "Cher(e) " + self.liste[0].nom.text() + " " + self.liste[
                            0].prenom.text() + "\nD\'apres vos reponses a ce questionnaire,vous semblez ne pas avoir de symptomes relier au Covid,néanmoins vous pouvez toujours etre un porteur_saint¹ ,c'est pour quoi vous devez appliquer les gestes barrieres et le port du masque reste obligatoire.\n\n\nun porteur_saint¹est une personne dont l'organisme est infecté par un agent infectieux (virus, bactérie, parasite) mais qui ne présente pas de signes cliniques de cette infection. On dit que cette personne est asymptomatique,autrement dit, qu'elle ne présente aucun symptôme."


            self.message.setText(chaine)
            font=QtGui.QFont()
            font.setPointSize(11)
            self.message.setFont(font)

            test.close()
            self.message.show()


    def fe(self):

          if(self.verifierInfo()):
                path = 'test.xlsx'
                if (not os.path.exists(path)):
                    df = DataFrame(columns=['nom', 'prenom', 'sexe', 'age', 'tel', 'wilaya', 'commune', 'symptomes',
                                            'Symptômes graves', 'depuis quand avez-vous ces symptomes?',
                                            'Maladie chronique', 'femme enceinte',"soumna"])
                    df.to_excel("test.xlsx", index=False)

                df = pd.read_excel("test.xlsx", "Sheet1")
                n = df.shape[0]


                df.loc[n, 'nom'] = self.liste[0].nom.text()


                df.loc[n, 'prenom'] = self.liste[0].prenom.text()
                df.loc[n, 'sexe'] =self.liste[0].sexe.currentText()
                df.loc[n, 'age'] = int(self.liste[0].age.text())
                df.loc[n, 'tel'] =int(self.liste[0].num.text())
                df.loc[n, 'wilaya'] = self.liste[0].wilaya.currentText()
                df.loc[n, 'commune'] = self.liste[0].com.text()
                df.loc[n,'femme enceinte']='oui'

                df.to_excel("test.xlsx", index=False)

                wsjdid.sauvegarde()
                graph = wsjdid.default_world.as_rdflib_graph()
                prefixe = "prefix ns1: <http://www.w3.org/2002/07/owl#> \nprefix ns2: <file://PROJET.owl#> \nprefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \nprefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> \nprefix xml: <http://www.w3.org/XML/1998/namespace> \nprefix xsd: <http://www.w3.org/2001/XMLSchema#>\n "
                select = "SELECT DISTINCT ?nom ?adr ?num ?x ?y\n WHERE{"
                cmd = "?x a ns2:Medecin ."
                cmd1 = "?y ns2:Nom " + '"' + str(self.liste[0].nom.text()) + '"^^xsd:string.'
                cmd2 = "?y ns2:Prenom " + '"' + str(self.liste[0].prenom.text()) + '"^^xsd:string .'
                cmd3 = "?x ns2:habite_a ?z."
                cmd4 = "?y a ns2:FemmeEnceinte."

                cmd5 = "?y ns2:habite_a ?z."
                #cmd6 = "?y ns2:a_Pour_Maladies ?t.?t ns2:typemaladie ?v.?x ns2:specialité ?v."
                cmd61 = '?x ns2:domaine "Gyneco Obstetrique"^^xsd:string.'
                cmd7 = "?x ns2:NomMed ?nom.?x ns2:adressemed ?adr.?x ns2:numtelmed ?num}"
                #cmd8 = "ORDER BY DESC(?dm)"
                requete = prefixe + select + cmd + cmd1 + cmd2 + cmd3 + cmd4 + cmd5 + cmd61 + cmd7
                #print(requete)
                res = graph.query(requete)
                print("batata")
                prediction = []
                for i in res:
                    x = []
                    x.append(str(i[0]))
                    x.append(str(i[1]))
                    x.append(str(i[2]))
                    x.append("Gyneco Obstetrique")
                    x.append(i[3])
                    x.append(i[4])
                    prediction.append(x)
                men = fiche()
                for i in range(0, len(prediction)):
                    afficher = carte(prediction[i][0], prediction[i][1], prediction[i][2], prediction[i][3])
                    afficher.toubib = prediction[i][4]
                    afficher.patient = prediction[i][5]
                    men.layoute.addWidget(afficher, i, 0)
                print("fin")
                #self.close()
                #ws.sauvegarde()



class MenuSparql(QtWidgets.QWidget):
    def __init__(self):

        super(MenuSparql,self).__init__()
        self.setStyleSheet("background-color: white;")
        self.editeur=QtWidgets.QPlainTextEdit()
        self.resultat=QtWidgets.QScrollArea()
        prefixe = "prefix ns1: <http://www.w3.org/2002/07/owl#> \nprefix ns2: <file://PROJET.owl#> \nprefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \nprefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> \nprefix xml: <http://www.w3.org/XML/1998/namespace> \nprefix xsd: <http://www.w3.org/2001/XMLSchema#>\n "
        self.editeur.setPlainText(prefixe)
        self.layout=QtWidgets.QGridLayout()
        self.layout.addWidget(self.editeur,0,0,1,3)
        self.layout.addWidget(self.resultat,2,0,1,6)
        self.exec=QtWidgets.QPushButton("executer")
        self.exec.setStyleSheet("color:white ;background-color: rgb(221,0,25);")

        self.layout.addWidget(self.exec, 1, 2, 1, 2)
        self.setLayout(self.layout)
        self.aide=QtWidgets.QScrollArea()
        self.aide.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.aide.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.resultat.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.resultat.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOn)
        self.resultat.setStyleSheet("background-color: rgb(240,240,240);")
        self.aide.setStyleSheet("background-color: rgb(240,240,240);")
        self.resultat.setWidgetResizable(True)
        self.Lresultat=QtWidgets.QLabel()
        self.resultat.setWidget(self.Lresultat)
        self.aide.setWidgetResizable(True)
        self.textaide=QtWidgets.QLabel()
        x=open("aide.txt","r")
        text=x.read()
        font=QtGui.QFont()
        font.setPointSize(10)
        font.setBold(True)
        self.textaide.setText(text)
        self.Lresultat.setFont(font)
        self.aide.setWidget(self.textaide)
        self.layout.addWidget(self.aide,0,3,1,3)
        self.exec.clicked.connect(self.query)
        self.exec.setFont(font)
        self.show()
    def query(self):

        wsjdid.sauvegarde()
        graph= wsjdid.default_world.as_rdflib_graph()
        print(self.editeur.toPlainText())
        try:
            requete=self.editeur.toPlainText()
            res=graph.query(requete)
            x=""
            for i in res:
                x=x+str(i)+"\n"
            self.Lresultat.setText(x)


        except Exception as e:
            print("An exception occurred")
            self.Lresultat.setText(str(e))

class menuprincipale(QtWidgets.QWidget):
    def __init__(self):
        super(menuprincipale,self).__init__()
        #self.groupe=QtWidgets.QStackedLayout()
        self.setStyleSheet("background-color:white;")
        self.bouton=QtWidgets.QPushButton("MEDECIN")
        self.bouton.setStyleSheet("color: white;background-color: rgb(5,2,152);")

        self.bouton2=QtWidgets.QPushButton("PATIENT")
        self.bouton2.setStyleSheet("color: white;background-color: rgb(5,2,152);")

        self.bt=QtWidgets.QPushButton("MENU")


        self.arriere=QtWidgets.QPushButton("")
        #self.arriere.setStyleSheet("color: white;background-color: rgb(0,105,204);")
        self.arriere.setIcon(QtGui.QIcon("animation\\previous.png"))
        self.arriere.setIconSize(QSize(100, 100))
        self.arriere.setFlat(True)
        #self.bt.setStyleSheet("color: white;background-color: rgb(225,195,255);")

        font=QtGui.QFont()
        font.setPointSize(20)
        font.setBold(True)
        self.bouton.setFont(font)
        self.bouton2.setFont(font)
        self.bt.setFont(font)
        self.wilayete=QtWidgets.QPushButton()
        self.wilayete.setText("خريطة الجزائر")
        self.wilayete.setFont(font)
        self.sparql = QtWidgets.QPushButton("SPARQL")
        self.sparql.setFont(font)
        self.sparql.clicked.connect(self.fsparql)
        self.bt.setIcon(QtGui.QIcon("animation\\file.png"))
        self.bt.setIconSize(QSize(50, 50))
        self.bt.setStyleSheet("color: white;background-color: rgb(221,0,25);")
        #self.bt.setFlat(True)

        self.groupe = QtWidgets.QStackedLayout()
        self.boite=QtWidgets.QWidget()
        self.boite.setLayout(self.groupe)

        #var =MenuMed()
        #self.groupe.addWidget(var)
        #var2=regrouper()
        #self.groupe.addWidget(var2)
        self.bouton.clicked.connect(self.medecinn)
        self.bouton2.clicked.connect(self.fcoco)

        #self.l = QtWidgets.QLabel('Presentation:')
        self.l = QtWidgets.QLabel()
        self.l.setPixmap(QtGui.QPixmap("animation\\stopcovid.png"))
        '''self.ll=QtWidgets.QLabel('Bienvenue dans votre polyclinique mobile, \n'
                                 ' Votre sante nous importe c\'est pour cela que nous avons mis en place \n'
                                 'ce service qui rapproche les patients a leurs medecins.\n'
                                 ' Nous avons pensez a tous, nous mettons a votre dispositions les meilleures conseillers en terme de sante \n'
                                 'qui vous guiderons pendant votre enregistrement sur notre plateforme. ')'''
        self.ll=QtWidgets.QLabel()
        self.ll.setPixmap(QtGui.QPixmap("animation\\stopcovid2.png"))
        font=QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        self.l.setFont(font)
        font=QtGui.QFont()
        font.setPointSize(12)
        #font.setBold(True)
        self.ll.setFont(font)

        self.layoute = QtWidgets.QGridLayout()
        self.layoute.addWidget(self.arriere,0,0)
        self.layoute.addWidget(self.l,1,0)
        self.layoute.addWidget(self.ll,1,1)
        self.layoute.addWidget(self.boite,0,1,2,1)
        self.layoute.addWidget(self.bouton, 6, 0,1,2)
        self.layoute.addWidget(self.bouton2,7,0,1,2)
        self.layoute.addWidget(self.wilayete,8,0,1,2)
        self.layoute.addWidget(self.sparql, 9,0,1,2)
        self.layoute.addWidget(self.bt,5,0,1,2)
        self.setLayout(self.layoute)
        self.bouton.hide()
        self.bouton2.hide()
        self.arriere.hide()
        self.wilayete.hide()
        self.sparql.hide()
        self.bt.clicked.connect(self.clic)
        self.arriere.clicked.connect(self.retour)
        self.layoute.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.groupe.setSizeConstraint(QtWidgets.QLayout.SetMaximumSize)
        self.wilayete.clicked.connect(self.dz)
        self.showMaximized()
        self.d=wilaya.wilaya()
        self.groupe.addWidget(self.d)
        self.boite.hide()
        self.coco=geste()
        #self.coco.setStyleSheet('background-color: rgb(221,0,25);')
        self.coco.commencer.clicked.connect(self.patientt)

        self.groupe.addWidget(self.coco)
        self.aff=False
    def fcoco(self):
        self.wilayete.hide()
        self.arriere.show()
        self.bt.hide()
        self.sparql.hide()
        self.l.hide()
        self.ll.hide()
        self.bouton.hide()
        self.bouton2.hide()
        self.setStyleSheet('background-color: rgb(221,0,25);')
        self.groupe.setCurrentWidget(self.coco)
        self.boite.show()
    def dz(self):
        print("dz")

        self.groupe.setCurrentWidget(self.d)
        self.wilayete.hide()
        self.sparql.hide()
        self.arriere.show()
        self.bt.hide()
        self.l.hide()
        self.ll.hide()
        self.bouton.hide()
        self.bouton2.hide()
        self.boite.show()
        print("fin dz")
    def medecinn(self):
        self.bt.hide()
        self.wilayete.hide()
        self.l.hide()
        self.sparql.hide()
        self.ll.hide()
        self.bouton.hide()
        self.bouton2.hide()
        self.arriere.show()
        self.g=MenuMed()
        self.groupe.addWidget(self.g)
        self.groupe.setCurrentWidget(self.g)
        self.boite.show()
    def patientt(self):
        self.setStyleSheet('background-color: rgb(255,255,255);')
        self.wilayete.hide()
        self.arriere.show()
        self.bt.hide()
        self.sparql.hide()
        self.l.hide()
        self.ll.hide()
        self.bouton.hide()
        self.bouton2.hide()
        self.g = regrouper()
        self.groupe.addWidget(self.g)
        self.groupe.setCurrentWidget(self.g)
        self.boite.show()
    def clic(self):
        #self.bt.hide()
        if not self.aff:
            self.bouton.show()
            self.bouton2.show()
            self.wilayete.show()
            self.sparql.show()
            self.aff=True
        else:
            self.bouton.hide()
            self.bouton2.hide()
            self.wilayete.hide()
            self.sparql.hide()
            self.aff=False
    def retour(self):
        self.setStyleSheet('background-color: rgb(255,255,255);')
        self.arriere.hide()
        self.bt.show()
        self.l.show()
        self.ll.show()
        self.boite.hide()
        self.wilayete.hide()
    def fsparql(self):
        self.bt.hide()
        self.wilayete.hide()
        self.l.hide()
        self.sparql.hide()
        self.ll.hide()
        self.bouton.hide()
        self.bouton2.hide()
        self.arriere.show()
        self.g = MenuSparql()
        self.groupe.addWidget(self.g)
        self.groupe.setCurrentWidget(self.g)
        self.boite.show()


app = QtWidgets.QApplication(sys.argv)

test=menuprincipale()

app.exec_()




