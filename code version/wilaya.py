from PyQt5 import QtWidgets
from PyQt5 import QtGui
import wsjdid


class wilaya(QtWidgets.QWidget):
    def __init__(self):
        super(wilaya, self).__init__()
        self.carte = QtWidgets.QLabel(self)
        self.w1 = QtWidgets.QPushButton("1",self)

        self.w1.setGeometry(170,280,50,20)

        self.w2 = QtWidgets.QPushButton("2",self)

        self.w2.setGeometry(230,35,17,17)
        self.w3 = QtWidgets.QPushButton("3",self)
        self.w3.setGeometry(268, 105, 17, 17)
        self.w4 = QtWidgets.QPushButton("4",self)
        self.w4.setGeometry(355,45,17,17)
        self.w5 = QtWidgets.QPushButton("5",self)
        self.w5.setGeometry(333,53,17,17)
        self.w6 = QtWidgets.QPushButton("6",self)
        self.w6.setGeometry(310,20,17,17)
        self.w7 = QtWidgets.QPushButton("7",self)
        self.w7.setGeometry(333,72,17,17)
        self.w8 = QtWidgets.QPushButton("8",self)
        self.w8.setGeometry(163,154,17,17)
        self.w9 = QtWidgets.QPushButton("9",self)
        self.w9.setGeometry(273,32,15,15)
        self.w10 = QtWidgets.QPushButton("10",self)
        self.w10.setGeometry(286,38,16,16)
        self.w11 = QtWidgets.QPushButton("11",self)
        self.w11.setGeometry(300,358,30,30)
        self.w12 = QtWidgets.QPushButton("12",self)
        self.w12.setGeometry(375,64,17,17)
        self.w13 = QtWidgets.QPushButton("13",self)
        self.w13.setGeometry(179,75,17,17)
        self.w14 = QtWidgets.QPushButton("14",self)
        self.w14.setGeometry(242,70,17,17)
        self.w15 = QtWidgets.QPushButton("15",self)
        self.w15.setGeometry(299,27,15,15)
        self.w16 = QtWidgets.QPushButton("16",self)
        self.w16.setGeometry(272,15,17,17)
        self.w17 = QtWidgets.QPushButton("17",self)
        self.w17.setGeometry(274,78,20,20)
        self.w18 = QtWidgets.QPushButton("18",self)
        self.w18.setGeometry(333,13,17,17)
        self.w19 = QtWidgets.QPushButton("19",self)
        self.w19.setGeometry(324,41,17,17)
        self.w20 = QtWidgets.QPushButton("20",self)
        self.w20.setGeometry(214,76,17,17)
        self.w21 = QtWidgets.QPushButton("21",self)
        self.w21.setGeometry(354,23,17,17)
        self.w22 = QtWidgets.QPushButton("22",self)
        self.w22.setGeometry(196,80,18,18)
        self.w23 = QtWidgets.QPushButton("23",self)
        self.w23.setGeometry(366,7,18,18)
        self.w24 = QtWidgets.QPushButton("24",self)
        self.w24.setGeometry(365,32,16,16)
        self.w25 = QtWidgets.QPushButton("25",self)
        self.w25.setGeometry(350,35,15,15)
        self.w26 = QtWidgets.QPushButton("26",self)
        self.w26.setGeometry(270,45,16,16)
        self.w27 = QtWidgets.QPushButton("27",self)
        self.w27.setGeometry(210,35,16,16)
        self.w28 = QtWidgets.QPushButton("28",self)
        self.w28.setGeometry(300,60,17,17)
        self.w29 = QtWidgets.QPushButton("29",self)
        self.w29.setGeometry(213,62,17,17)
        self.w30 = QtWidgets.QPushButton("30",self)
        self.w30.setGeometry(337,161,19,19)
        self.w31 = QtWidgets.QPushButton("31",self)
        self.w31.setGeometry(194,41,17,17)
        self.w32 = QtWidgets.QPushButton("32",self)
        self.w32.setGeometry(230,130,19,19)
        self.w33 = QtWidgets.QPushButton("33",self)
        self.w33.setGeometry(380,240,19,19)
        self.w34 = QtWidgets.QPushButton("34",self)
        self.w34.setGeometry(310,42,17,17)
        self.w35 = QtWidgets.QPushButton("35",self)
        self.w35.setGeometry(287,14,17,17)
        self.w36 = QtWidgets.QPushButton("36",self)
        self.w36.setGeometry(378,24,17,17)
        self.w37 = QtWidgets.QPushButton("37",self)
        self.w37.setGeometry(62,250,18,18)
        self.w38 = QtWidgets.QPushButton("38",self)
        self.w38.setGeometry(250,51,17,17)
        self.w39 = QtWidgets.QPushButton("39",self)
        self.w39.setGeometry(364,110,17,17)
        self.w40 = QtWidgets.QPushButton('40',self)
        self.w40.setGeometry(355,64,18,18)
        self.w41 = QtWidgets.QPushButton("41",self)
        self.w41.setGeometry(379,39,18,18)
        self.w42 = QtWidgets.QPushButton("42",self)
        self.w42.setGeometry(254,21,17,17)
        self.w43 = QtWidgets.QPushButton("43",self)
        self.w43.setGeometry(338,38,17,17)
        self.w44 = QtWidgets.QPushButton("44",self)
        self.w44.setGeometry(254,41,17,17)
        self.w45 = QtWidgets.QPushButton("45",self)
        self.w45.setGeometry(193,112,18,18)
        self.w46 = QtWidgets.QPushButton("46",self)
        self.w46.setGeometry(173,50,18,18)
        self.w47 = QtWidgets.QPushButton("47",self)
        self.w47.setGeometry(288,133,18,18)
        self.w48 = QtWidgets.QPushButton('48',self)
        self.w48.setGeometry(227,49,17,17)
        self.w49 = QtWidgets.QPushButton("49",self)
        self.w49.setGeometry(330,95,18,18)
        self.w50 = QtWidgets.QPushButton('50',self)
        self.w50.setGeometry(270,175,19,19)
        self.w51 = QtWidgets.QPushButton('51',self)
        self.w51.setGeometry(311,88,19,19)
        self.w52 = QtWidgets.QPushButton('52',self)
        self.w52.setGeometry(182,360,21,21)
        self.w53 = QtWidgets.QPushButton('53',self)
        self.w53.setGeometry(146,204,20,20)
        self.w54 = QtWidgets.QPushButton('54',self)
        self.w54.setGeometry(224,204,19,19)
        self.w55 = QtWidgets.QPushButton('55',self)
        self.w55.setGeometry(340,115,19,19)
        self.w56 = QtWidgets.QPushButton('56',self)
        self.w56.setGeometry(420,336,18,18)
        self.w57 = QtWidgets.QPushButton('57',self)
        self.w57.setGeometry(286,261,20,20)
        self.w58 = QtWidgets.QPushButton('58',self)
        self.w58.setGeometry(315,457,20,20)
        self.carte.setPixmap(QtGui.QPixmap("animation\\algerie.jpg"))
        self.w1.clicked.connect(self.f1)
        self.w2.clicked.connect(self.f2)
        self.w3.clicked.connect(self.f3)
        self.w4.clicked.connect(self.f4)
        self.w5.clicked.connect(self.f5)
        self.w6.clicked.connect(self.f6)
        self.w7.clicked.connect(self.f7)
        self.w8.clicked.connect(self.f8)
        self.w9.clicked.connect(self.f9)
        self.w10.clicked.connect(self.f10)
        self.w11.clicked.connect(self.f11)
        self.w12.clicked.connect(self.f12)
        self.w13.clicked.connect(self.f13)
        self.w14.clicked.connect(self.f14)
        self.w15.clicked.connect(self.f15)
        self.w16.clicked.connect(self.f16)
        self.w17.clicked.connect(self.f17)
        self.w18.clicked.connect(self.f18)
        self.w19.clicked.connect(self.f19)
        self.w20.clicked.connect(self.f20)
        self.w21.clicked.connect(self.f21)
        self.w22.clicked.connect(self.f22)
        self.w23.clicked.connect(self.f23)
        self.w24.clicked.connect(self.f24)
        self.w25.clicked.connect(self.f25)
        self.w26.clicked.connect(self.f26)
        self.w28.clicked.connect(self.f27)
        self.w28.clicked.connect(self.f28)
        self.w29.clicked.connect(self.f29)
        self.w30.clicked.connect(self.f30)
        self.w31.clicked.connect(self.f31)
        self.w32.clicked.connect(self.f32)
        self.w33.clicked.connect(self.f33)
        self.w34.clicked.connect(self.f34)
        self.w35.clicked.connect(self.f35)
        self.w36.clicked.connect(self.f36)
        self.w37.clicked.connect(self.f37)
        self.w38.clicked.connect(self.f38)
        self.w39.clicked.connect(self.f39)
        self.w40.clicked.connect(self.f40)
        self.w41.clicked.connect(self.f41)
        self.w42.clicked.connect(self.f42)
        self.w43.clicked.connect(self.f43)
        self.w44.clicked.connect(self.f44)
        self.w45.clicked.connect(self.f45)
        self.w46.clicked.connect(self.f46)
        self.w47.clicked.connect(self.f47)
        self.w48.clicked.connect(self.f48)
        self.w49.clicked.connect(self.f49)
        self.w50.clicked.connect(self.f50)
        self.w51.clicked.connect(self.f51)
        self.w52.clicked.connect(self.f52)
        self.w53.clicked.connect(self.f53)
        self.w54.clicked.connect(self.f54)
        self.w55.clicked.connect(self.f55)
        self.w56.clicked.connect(self.f56)
        self.w57.clicked.connect(self.f57)
        self.w58.clicked.connect(self.f58)
        #self.show()

    def f1(self):

            print("debut")
            wsjdid.sauvegarde()
            graph = wsjdid.default_world.as_rdflib_graph()
            prefixe = "prefix ns1: <http://www.w3.org/2002/07/owl#> \nprefix ns2: <file://PROJET.owl#> \nprefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \nprefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> \nprefix xml: <http://www.w3.org/XML/1998/namespace> \nprefix xsd: <http://www.w3.org/2001/XMLSchema#>\n "
            select1 = "SELECT (COUNT( ?x) AS ?nbpatteints)  \n WHERE{"
            select2 = "SELECT  (COUNT( ?z) AS ?nbhabitants) \n WHERE{"
            select3 = "SELECT (COUNT( ?w) AS ?nbhop) \n WHERE{"
            select4 = "SELECT (COUNT(?e) AS ?nbmed ) \n WHERE{"
            cmd = "OPTIONAL{?x a ns2:pCovid_grave."
            cmd1 = "?x ns2:habite_a <file://PROJET.owl#1.ADRAR>.}}"
            cmd11 = "OPTIONAL{?e a ns2:Medecin."
            cmd12 = "?e ns2:habite_a <file://PROJET.owl#1.ADRAR>.}}"
            cmd2 = "OPTIONAL{<file://PROJET.owl#1.ADRAR> ns2:a_pour_habitant ?z.}}"
            cmd3 = "OPTIONAL{<file://PROJET.owl#1.ADRAR> ns2:contient_hopital ?w}}"

            requete = prefixe + select1 + cmd + cmd1
            x = []
            res = graph.query(requete)

            for i in res:
                x.append(str(i[0]))

            requete = prefixe + select2 + cmd2

            res = graph.query(requete)

            for i in res:
                x.append(str(i[0]))
            requete = prefixe + select3 + cmd3

            res = graph.query(requete)

            for i in res:
                x.append(str(i[0]))
            requete = prefixe + select4 + cmd11 + cmd12

            res = graph.query(requete)

            for i in res:
                x.append(str(i[0]))
            print(requete)
            self.msg = QtWidgets.QMessageBox()
            self.msg.setText(
                "WILAYA D'ADRAR:\nNombre d'habitants:" + x[1] + "\nNombre de personne atteintes de covid: " + x[
                    0] + "\nNombre d'hopitaux: " + x[2] + "\nNombre de medecins: " + x[3])
            self.msg.show()
            print("fin")

    def f2(self):
        print("debut")
        wsjdid.sauvegarde()
        graph = wsjdid.default_world.as_rdflib_graph()
        prefixe = "prefix ns1: <http://www.w3.org/2002/07/owl#> \nprefix ns2: <file://PROJET.owl#> \nprefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \nprefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> \nprefix xml: <http://www.w3.org/XML/1998/namespace> \nprefix xsd: <http://www.w3.org/2001/XMLSchema#>\n "
        select1 = "SELECT (COUNT( ?x) AS ?nbpatteints)  \n WHERE{"
        select2 = "SELECT  (COUNT( ?z) AS ?nbhabitants) \n WHERE{"
        select3 = "SELECT (COUNT( ?w) AS ?nbhop) \n WHERE{"
        select4 = "SELECT (COUNT(?e) AS ?nbmed ) \n WHERE{"
        cmd = "OPTIONAL{?x a ns2:pCovid_grave."
        cmd1 = "?x ns2:habite_a <file://PROJET.owl#2.CHLEF>.}}"
        cmd11 = "OPTIONAL{?e a ns2:Medecin."
        cmd12 = "?e ns2:habite_a <file://PROJET.owl#2.CHLEF>.}}"
        cmd2 = "OPTIONAL{<file://PROJET.owl#2.CHLEF> ns2:a_pour_habitant ?z.}}"
        cmd3 = "OPTIONAL{<file://PROJET.owl#2.CHLEF> ns2:contient_hopital ?w}}"

        requete = prefixe + select1 + cmd + cmd1
        x = []
        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))

        requete = prefixe + select2 + cmd2

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        requete = prefixe + select3 + cmd3

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        requete = prefixe + select4 + cmd11 + cmd12

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        print(requete)
        self.msg = QtWidgets.QMessageBox()
        self.msg.setText(
            "WILAYA DE CHLEF:\nNombre d'habitants:" + x[1] + "\nNombre de personne atteintes de covid: " + x[
                0] + "\nNombre d'hopitaux: " + x[2] + "\nNombre de medecins: " + x[3])
        self.msg.show()
        print("fin")

    def f3(self):
        print("debut")
        wsjdid.sauvegarde()
        graph = wsjdid.default_world.as_rdflib_graph()
        prefixe = "prefix ns1: <http://www.w3.org/2002/07/owl#> \nprefix ns2: <file://PROJET.owl#> \nprefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \nprefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> \nprefix xml: <http://www.w3.org/XML/1998/namespace> \nprefix xsd: <http://www.w3.org/2001/XMLSchema#>\n "
        select1 = "SELECT (COUNT( ?x) AS ?nbpatteints)  \n WHERE{"
        select2 = "SELECT  (COUNT( ?z) AS ?nbhabitants) \n WHERE{"
        select3 = "SELECT (COUNT( ?w) AS ?nbhop) \n WHERE{"
        select4 = "SELECT (COUNT(?e) AS ?nbmed ) \n WHERE{"
        cmd = "OPTIONAL{?x a ns2:pCovid_grave."
        cmd1 = "?x ns2:habite_a <file://PROJET.owl#3.LAGHOUAT>.}}"
        cmd11 = "OPTIONAL{?e a ns2:Medecin."
        cmd12 = "?e ns2:habite_a <file://PROJET.owl#3.LAGHOUAT>.}}"
        cmd2 = "OPTIONAL{<file://PROJET.owl#3.LAGHOUAT> ns2:a_pour_habitant ?z.}}"
        cmd3 = "OPTIONAL{<file://PROJET.owl#3.LAGHOUAT> ns2:contient_hopital ?w}}"

        requete = prefixe + select1 + cmd + cmd1
        x = []
        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))

        requete = prefixe + select2 + cmd2

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        requete = prefixe + select3 + cmd3

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        requete = prefixe + select4 + cmd11 + cmd12

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        print(requete)
        self.msg = QtWidgets.QMessageBox()
        self.msg.setText(
            "WILAYA DE LAGHOUAT:\nNombre d'habitants:" + x[1] + "\nNombre de personne atteintes de covid: " + x[
                0] + "\nNombre d'hopitaux: " + x[2] + "\nNombre de medecins: " + x[3])
        self.msg.show()
        print("fin")

    def f4(self):
        print("debut")
        wsjdid.sauvegarde()
        graph = wsjdid.default_world.as_rdflib_graph()
        prefixe = "prefix ns1: <http://www.w3.org/2002/07/owl#> \nprefix ns2: <file://PROJET.owl#> \nprefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \nprefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> \nprefix xml: <http://www.w3.org/XML/1998/namespace> \nprefix xsd: <http://www.w3.org/2001/XMLSchema#>\n "
        select1 = "SELECT (COUNT( ?x) AS ?nbpatteints)  \n WHERE{"
        select2 = "SELECT  (COUNT( ?z) AS ?nbhabitants) \n WHERE{"
        select3 = "SELECT (COUNT( ?w) AS ?nbhop) \n WHERE{"
        select4 = "SELECT (COUNT(?e) AS ?nbmed ) \n WHERE{"
        cmd = "OPTIONAL{?x a ns2:pCovid_grave."
        cmd1 = "?x ns2:habite_a <file://PROJET.owl#4.OUMBOUAGHI>.}}"
        cmd11 = "OPTIONAL{?e a ns2:Medecin."
        cmd12 = "?e ns2:habite_a <file://PROJET.owl#4.OUMBOUAGHI>.}}"
        cmd2 = "OPTIONAL{<file://PROJET.owl#4.OUMBOUAGHI> ns2:a_pour_habitant ?z.}}"
        cmd3 = "OPTIONAL{<file://PROJET.owl#4.OUMBOUAGHI> ns2:contient_hopital ?w}}"

        requete = prefixe + select1 + cmd + cmd1
        x = []
        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))

        requete = prefixe + select2 + cmd2

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        requete = prefixe + select3 + cmd3

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        requete = prefixe + select4 + cmd11 + cmd12

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        print(requete)
        self.msg = QtWidgets.QMessageBox()
        self.msg.setText(
            "WILAYA DE OUMBOUAGHI:\nNombre d'habitants:" + x[1] + "\nNombre de personne atteintes de covid: " + x[
                0] + "\nNombre d'hopitaux: " + x[2] + "\nNombre de medecins: " + x[3])
        self.msg.show()
        print("fin")

    def f5(self):
        print("debut")
        wsjdid.sauvegarde()
        graph = wsjdid.default_world.as_rdflib_graph()
        prefixe = "prefix ns1: <http://www.w3.org/2002/07/owl#> \nprefix ns2: <file://PROJET.owl#> \nprefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \nprefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> \nprefix xml: <http://www.w3.org/XML/1998/namespace> \nprefix xsd: <http://www.w3.org/2001/XMLSchema#>\n "
        select1 = "SELECT (COUNT( ?x) AS ?nbpatteints)  \n WHERE{"
        select2 = "SELECT  (COUNT( ?z) AS ?nbhabitants) \n WHERE{"
        select3 = "SELECT (COUNT( ?w) AS ?nbhop) \n WHERE{"
        select4 = "SELECT (COUNT(?e) AS ?nbmed ) \n WHERE{"
        cmd = "OPTIONAL{?x a ns2:pCovid_grave."
        cmd1 = "?x ns2:habite_a <file://PROJET.owl#5.BATNA>.}}"
        cmd11 = "OPTIONAL{?e a ns2:Medecin."
        cmd12 = "?e ns2:habite_a <file://PROJET.owl#5.BATNA>.}}"
        cmd2 = "OPTIONAL{<file://PROJET.owl#5.BATNA> ns2:a_pour_habitant ?z.}}"
        cmd3 = "OPTIONAL{<file://PROJET.owl#5.BATNA> ns2:contient_hopital ?w}}"

        requete = prefixe + select1 + cmd + cmd1
        x = []
        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))

        requete = prefixe + select2 + cmd2

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        requete = prefixe + select3 + cmd3

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        requete = prefixe + select4 + cmd11 + cmd12

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        print(requete)
        self.msg = QtWidgets.QMessageBox()
        self.msg.setText(
            "WILAYA DE BATNA:\nNombre d'habitants:" + x[1] + "\nNombre de personne atteintes de covid: " + x[
                0] + "\nNombre d'hopitaux: " + x[2] + "\nNombre de medecins: " + x[3])
        self.msg.show()
        print("fin")

    def f6(self):
        print("debut")
        wsjdid.sauvegarde()
        graph = wsjdid.default_world.as_rdflib_graph()
        prefixe = "prefix ns1: <http://www.w3.org/2002/07/owl#> \nprefix ns2: <file://PROJET.owl#> \nprefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \nprefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> \nprefix xml: <http://www.w3.org/XML/1998/namespace> \nprefix xsd: <http://www.w3.org/2001/XMLSchema#>\n "
        select1 = "SELECT (COUNT( ?x) AS ?nbpatteints)  \n WHERE{"
        select2 = "SELECT  (COUNT( ?z) AS ?nbhabitants) \n WHERE{"
        select3 = "SELECT (COUNT( ?w) AS ?nbhop) \n WHERE{"
        select4 = "SELECT (COUNT(?e) AS ?nbmed ) \n WHERE{"
        cmd = "OPTIONAL{?x a ns2:pCovid_grave."
        cmd1 = "?x ns2:habite_a <file://PROJET.owl#6.BEJAIA>.}}"
        cmd11 = "OPTIONAL{?e a ns2:Medecin."
        cmd12 = "?e ns2:habite_a <file://PROJET.owl#6.BEJAIA>.}}"
        cmd2 = "OPTIONAL{<file://PROJET.owl#6.BEJAIA> ns2:a_pour_habitant ?z.}}"
        cmd3 = "OPTIONAL{<file://PROJET.owl#6.BEJAIA> ns2:contient_hopital ?w}}"

        requete = prefixe + select1 + cmd + cmd1
        x = []
        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))

        requete = prefixe + select2 + cmd2

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        requete = prefixe + select3 + cmd3

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        requete = prefixe + select4 + cmd11 + cmd12

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        print(requete)
        self.msg = QtWidgets.QMessageBox()
        self.msg.setText(
            "WILAYA DE BEJAIA:\nNombre d'habitants:" + x[1] + "\nNombre de personne atteintes de covid: " + x[
                0] + "\nNombre d'hopitaux: " + x[2] + "\nNombre de medecins: " + x[3])
        self.msg.show()
        print("fin")

    def f7(self):
        print("debut")
        wsjdid.sauvegarde()
        graph = wsjdid.default_world.as_rdflib_graph()
        prefixe = "prefix ns1: <http://www.w3.org/2002/07/owl#> \nprefix ns2: <file://PROJET.owl#> \nprefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \nprefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> \nprefix xml: <http://www.w3.org/XML/1998/namespace> \nprefix xsd: <http://www.w3.org/2001/XMLSchema#>\n "
        select1 = "SELECT (COUNT( ?x) AS ?nbpatteints)  \n WHERE{"
        select2 = "SELECT  (COUNT( ?z) AS ?nbhabitants) \n WHERE{"
        select3 = "SELECT (COUNT( ?w) AS ?nbhop) \n WHERE{"
        select4 = "SELECT (COUNT(?e) AS ?nbmed ) \n WHERE{"
        cmd = "OPTIONAL{?x a ns2:pCovid_grave."
        cmd1 = "?x ns2:habite_a <file://PROJET.owl#7.BISKRA> .}}"
        cmd11 = "OPTIONAL{?e a ns2:Medecin."
        cmd12 = "?e ns2:habite_a <file://PROJET.owl#7.BISKRA> .}}"
        cmd2 = "OPTIONAL{<file://PROJET.owl#7.BISKRA>  ns2:a_pour_habitant ?z.}}"
        cmd3 = "OPTIONAL{<file://PROJET.owl#7.BISKRA>  ns2:contient_hopital ?w}}"

        requete = prefixe + select1 + cmd + cmd1
        x = []
        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))

        requete = prefixe + select2 + cmd2

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        requete = prefixe + select3 + cmd3

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        requete = prefixe + select4 + cmd11 + cmd12

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        print(requete)
        self.msg = QtWidgets.QMessageBox()
        self.msg.setText(
            "WILAYA DE BISKRA:\nNombre d'habitants:" + x[1] + "\nNombre de personne atteintes de covid: " + x[
                0] + "\nNombre d'hopitaux: " + x[2] + "\nNombre de medecins: " + x[3])
        self.msg.show()
        print("fin")

    def f8(self):
        print("debut")
        wsjdid.sauvegarde()
        graph = wsjdid.default_world.as_rdflib_graph()
        prefixe = "prefix ns1: <http://www.w3.org/2002/07/owl#> \nprefix ns2: <file://PROJET.owl#> \nprefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \nprefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> \nprefix xml: <http://www.w3.org/XML/1998/namespace> \nprefix xsd: <http://www.w3.org/2001/XMLSchema#>\n "
        select1 = "SELECT (COUNT( ?x) AS ?nbpatteints)  \n WHERE{"
        select2 = "SELECT  (COUNT( ?z) AS ?nbhabitants) \n WHERE{"
        select3 = "SELECT (COUNT( ?w) AS ?nbhop) \n WHERE{"
        select4 = "SELECT (COUNT(?e) AS ?nbmed ) \n WHERE{"
        cmd = "OPTIONAL{?x a ns2:pCovid_grave."
        cmd1 = "?x ns2:habite_a <file://PROJET.owl#8.BECHAR>.}}"
        cmd11 = "OPTIONAL{?e a ns2:Medecin."
        cmd12 = "?e ns2:habite_a <file://PROJET.owl#8.BECHAR>.}}"
        cmd2 = "OPTIONAL{<file://PROJET.owl#8.BECHAR> ns2:a_pour_habitant ?z.}}"
        cmd3 = "OPTIONAL{<file://PROJET.owl#8.BECHAR> ns2:contient_hopital ?w}}"

        requete = prefixe + select1 + cmd + cmd1
        x = []
        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))

        requete = prefixe + select2 + cmd2

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        requete = prefixe + select3 + cmd3

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        requete = prefixe + select4 + cmd11 + cmd12

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        print(requete)
        self.msg = QtWidgets.QMessageBox()
        self.msg.setText(
            "WILAYA DE BECHAR:\nNombre d'habitants:" + x[1] + "\nNombre de personne atteintes de covid: " + x[
                0] + "\nNombre d'hopitaux: " + x[2] + "\nNombre de medecins: " + x[3])
        self.msg.show()
        print("fin")

    def f9(self):
        print("debut")
        wsjdid.sauvegarde()
        graph = wsjdid.default_world.as_rdflib_graph()
        prefixe = "prefix ns1: <http://www.w3.org/2002/07/owl#> \nprefix ns2: <file://PROJET.owl#> \nprefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \nprefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> \nprefix xml: <http://www.w3.org/XML/1998/namespace> \nprefix xsd: <http://www.w3.org/2001/XMLSchema#>\n "
        select1 = "SELECT (COUNT( ?x) AS ?nbpatteints)  \n WHERE{"
        select2 = "SELECT  (COUNT( ?z) AS ?nbhabitants) \n WHERE{"
        select3 = "SELECT (COUNT( ?w) AS ?nbhop) \n WHERE{"
        select4 = "SELECT (COUNT(?e) AS ?nbmed ) \n WHERE{"
        cmd = "OPTIONAL{?x a ns2:pCovid_grave."
        cmd1 = "?x ns2:habite_a <file://PROJET.owl#9.BLIDA>.}}"
        cmd11 = "OPTIONAL{?e a ns2:Medecin."
        cmd12 = "?e ns2:habite_a <file://PROJET.owl#9.BLIDA>.}}"
        cmd2 = "OPTIONAL{<file://PROJET.owl#9.BLIDA> ns2:a_pour_habitant ?z.}}"
        cmd3 = "OPTIONAL{<file://PROJET.owl#9.BLIDA> ns2:contient_hopital ?w}}"

        requete = prefixe + select1 + cmd + cmd1
        x = []
        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))

        requete = prefixe + select2 + cmd2

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        requete = prefixe + select3 + cmd3

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        requete = prefixe + select4 + cmd11 + cmd12

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        print(requete)
        self.msg = QtWidgets.QMessageBox()
        self.msg.setText(
            "WILAYA DE BLIDA:\nNombre d'habitants:" + x[1] + "\nNombre de personne atteintes de covid: " + x[
                0] + "\nNombre d'hopitaux: " + x[2] + "\nNombre de medecins: " + x[3])
        self.msg.show()
        print("fin")

    def f10(self):
        print("debut")
        wsjdid.sauvegarde()
        graph = wsjdid.default_world.as_rdflib_graph()
        prefixe = "prefix ns1: <http://www.w3.org/2002/07/owl#> \nprefix ns2: <file://PROJET.owl#> \nprefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \nprefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> \nprefix xml: <http://www.w3.org/XML/1998/namespace> \nprefix xsd: <http://www.w3.org/2001/XMLSchema#>\n "
        select1 = "SELECT (COUNT( ?x) AS ?nbpatteints)  \n WHERE{"
        select2 = "SELECT  (COUNT( ?z) AS ?nbhabitants) \n WHERE{"
        select3 = "SELECT (COUNT( ?w) AS ?nbhop) \n WHERE{"
        select4 = "SELECT (COUNT(?e) AS ?nbmed ) \n WHERE{"
        cmd = "OPTIONAL{?x a ns2:pCovid_grave."
        cmd1 = "?x ns2:habite_a <file://PROJET.owl#10.BOUIRA>.}}"
        cmd11 = "OPTIONAL{?e a ns2:Medecin."
        cmd12 = "?e ns2:habite_a <file://PROJET.owl#10.BOUIRA>.}}"
        cmd2 = "OPTIONAL{<file://PROJET.owl#10.BOUIRA> ns2:a_pour_habitant ?z.}}"
        cmd3 = "OPTIONAL{<file://PROJET.owl#10.BOUIRA> ns2:contient_hopital ?w}}"

        requete = prefixe + select1 + cmd + cmd1
        x = []
        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))

        requete = prefixe + select2 + cmd2

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        requete = prefixe + select3 + cmd3

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        requete = prefixe + select4 + cmd11 + cmd12

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        print(requete)
        self.msg = QtWidgets.QMessageBox()
        self.msg.setText(
            "WILAYA DE BOUIRA:\nNombre d'habitants:" + x[1] + "\nNombre de personne atteintes de covid: " + x[
                0] + "\nNombre d'hopitaux: " + x[2] + "\nNombre de medecins: " + x[3])
        self.msg.show()
        print("fin")

    def f11(self):
        print("debut")
        wsjdid.sauvegarde()
        graph = wsjdid.default_world.as_rdflib_graph()
        prefixe = "prefix ns1: <http://www.w3.org/2002/07/owl#> \nprefix ns2: <file://PROJET.owl#> \nprefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \nprefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> \nprefix xml: <http://www.w3.org/XML/1998/namespace> \nprefix xsd: <http://www.w3.org/2001/XMLSchema#>\n "
        select1 = "SELECT (COUNT( ?x) AS ?nbpatteints)  \n WHERE{"
        select2 = "SELECT  (COUNT( ?z) AS ?nbhabitants) \n WHERE{"
        select3 = "SELECT (COUNT( ?w) AS ?nbhop) \n WHERE{"
        select4 = "SELECT (COUNT(?e) AS ?nbmed ) \n WHERE{"
        cmd = "OPTIONAL{?x a ns2:pCovid_grave."
        cmd1 = "?x ns2:habite_a <file://PROJET.owl#11.TAMANRASSET>.}}"
        cmd11 = "OPTIONAL{?e a ns2:Medecin."
        cmd12 = "?e ns2:habite_a <file://PROJET.owl#11.TAMANRASSET>.}}"
        cmd2 = "OPTIONAL{<file://PROJET.owl#11.TAMANRASSET> ns2:a_pour_habitant ?z.}}"
        cmd3 = "OPTIONAL{<file://PROJET.owl#11.TAMANRASSET> ns2:contient_hopital ?w}}"

        requete = prefixe + select1 + cmd + cmd1
        x = []
        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))

        requete = prefixe + select2 + cmd2

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        requete = prefixe + select3 + cmd3

        res = graph.query(requete)
        print(list(res))

        for i in res:
            x.append(str(i[0]))
        requete = prefixe + select4 + cmd11 + cmd12

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        print(requete)
        print(x)
        self.msg = QtWidgets.QMessageBox()
        self.msg.setText(
            "WILAYA DE TAMANARASSET:\nNombre d'habitants:" + x[1] + "\nNombre de personne atteintes de covid: " + x[
                0] + "\nNombre d'hopitaux: " + x[2] + "\nNombre de medecins: " + x[3])
        self.msg.show()
        print("fin")

    def f12(self):
        print("debut")
        wsjdid.sauvegarde()
        graph = wsjdid.default_world.as_rdflib_graph()
        prefixe = "prefix ns1: <http://www.w3.org/2002/07/owl#> \nprefix ns2: <file://PROJET.owl#> \nprefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \nprefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> \nprefix xml: <http://www.w3.org/XML/1998/namespace> \nprefix xsd: <http://www.w3.org/2001/XMLSchema#>\n "
        select1 = "SELECT (COUNT( ?x) AS ?nbpatteints)  \n WHERE{"
        select2 = "SELECT  (COUNT( ?z) AS ?nbhabitants) \n WHERE{"
        select3 = "SELECT (COUNT( ?w) AS ?nbhop) \n WHERE{"
        select4 = "SELECT (COUNT(?e) AS ?nbmed ) \n WHERE{"
        cmd = "OPTIONAL{?x a ns2:pCovid_grave."
        cmd1 = "?x ns2:habite_a <file://PROJET.owl#12.TEBESSA>.}}"
        cmd11 = "OPTIONAL{?e a ns2:Medecin."
        cmd12 = "?e ns2:habite_a <file://PROJET.owl#12.TEBESSA>.}}"
        cmd2 = "OPTIONAL{<file://PROJET.owl#12.TEBESSA> ns2:a_pour_habitant ?z.}}"
        cmd3 = "OPTIONAL{<file://PROJET.owl#12.TEBESSA> ns2:contient_hopital ?w}}"

        requete = prefixe + select1 + cmd + cmd1
        x = []
        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))

        requete = prefixe + select2 + cmd2

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        requete = prefixe + select3 + cmd3

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        requete = prefixe + select4 + cmd11 + cmd12

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        print(requete)
        self.msg = QtWidgets.QMessageBox()
        self.msg.setText(
            "WILAYA DE TEBESSA:\nNombre d'habitants:" + x[1] + "\nNombre de personne atteintes de covid: " + x[
                0] + "\nNombre d'hopitaux: " + x[2] + "\nNombre de medecins: " + x[3])
        self.msg.show()
        print("fin")

    def f13(self):
        print("debut")
        wsjdid.sauvegarde()
        graph = wsjdid.default_world.as_rdflib_graph()
        prefixe = "prefix ns1: <http://www.w3.org/2002/07/owl#> \nprefix ns2: <file://PROJET.owl#> \nprefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \nprefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> \nprefix xml: <http://www.w3.org/XML/1998/namespace> \nprefix xsd: <http://www.w3.org/2001/XMLSchema#>\n "
        select1 = "SELECT (COUNT( ?x) AS ?nbpatteints)  \n WHERE{"
        select2 = "SELECT  (COUNT( ?z) AS ?nbhabitants) \n WHERE{"
        select3 = "SELECT (COUNT( ?w) AS ?nbhop) \n WHERE{"
        select4 = "SELECT (COUNT(?e) AS ?nbmed ) \n WHERE{"
        cmd = "OPTIONAL{?x a ns2:pCovid_grave."
        cmd1 = "?x ns2:habite_a <file://PROJET.owl#13.TLEMCEN>.}}"
        cmd11 = "OPTIONAL{?e a ns2:Medecin."
        cmd12 = "?e ns2:habite_a <file://PROJET.owl#13.TLEMCEN>.}}"
        cmd2 = "OPTIONAL{<file://PROJET.owl#13.TLEMCEN> ns2:a_pour_habitant ?z.}}"
        cmd3 = "OPTIONAL{<file://PROJET.owl#13.TLEMCEN> ns2:contient_hopital ?w}}"

        requete = prefixe + select1 + cmd + cmd1
        x = []
        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))

        requete = prefixe + select2 + cmd2

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        requete = prefixe + select3 + cmd3

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        requete = prefixe + select4 + cmd11 + cmd12

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        print(requete)
        self.msg = QtWidgets.QMessageBox()
        self.msg.setText(
            "WILAYA DE ALGER:\nNombre d'habitants:" + x[1] + "\nNombre de personne atteintes de covid: " + x[
                0] + "\nNombre d'hopitaux: " + x[2] + "\nNombre de medecins: " + x[3])
        self.msg.show()
        print("fin")

    def f14(self):
        print("debut")
        wsjdid.sauvegarde()
        graph = wsjdid.default_world.as_rdflib_graph()
        prefixe = "prefix ns1: <http://www.w3.org/2002/07/owl#> \nprefix ns2: <file://PROJET.owl#> \nprefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \nprefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> \nprefix xml: <http://www.w3.org/XML/1998/namespace> \nprefix xsd: <http://www.w3.org/2001/XMLSchema#>\n "
        select1 = "SELECT (COUNT( ?x) AS ?nbpatteints)  \n WHERE{"
        select2 = "SELECT  (COUNT( ?z) AS ?nbhabitants) \n WHERE{"
        select3 = "SELECT (COUNT( ?w) AS ?nbhop) \n WHERE{"
        select4 = "SELECT (COUNT(?e) AS ?nbmed ) \n WHERE{"
        cmd = "OPTIONAL{?x a ns2:pCovid_grave."
        cmd1 = "?x ns2:habite_a <file://PROJET.owl#14.TIARET>.}}"
        cmd11 = "OPTIONAL{?e a ns2:Medecin."
        cmd12 = "?e ns2:habite_a <file://PROJET.owl#14.TIARET>.}}"
        cmd2 = "OPTIONAL{<file://PROJET.owl#14.TIARET> ns2:a_pour_habitant ?z.}}"
        cmd3 = "OPTIONAL{<file://PROJET.owl#14.TIARET> ns2:contient_hopital ?w}}"

        requete = prefixe + select1 + cmd + cmd1
        x = []
        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))

        requete = prefixe + select2 + cmd2

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        requete = prefixe + select3 + cmd3

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        requete = prefixe + select4 + cmd11 + cmd12

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        print(requete)
        self.msg = QtWidgets.QMessageBox()
        self.msg.setText(
            "WILAYA DE TIARET:\nNombre d'habitants:" + x[1] + "\nNombre de personne atteintes de covid: " + x[
                0] + "\nNombre d'hopitaux: " + x[2] + "\nNombre de medecins: " + x[3])
        self.msg.show()
        print("fin")

    def f15(self):
        print("debut")
        wsjdid.sauvegarde()
        graph = wsjdid.default_world.as_rdflib_graph()
        prefixe = "prefix ns1: <http://www.w3.org/2002/07/owl#> \nprefix ns2: <file://PROJET.owl#> \nprefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \nprefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> \nprefix xml: <http://www.w3.org/XML/1998/namespace> \nprefix xsd: <http://www.w3.org/2001/XMLSchema#>\n "
        select1 = "SELECT (COUNT( ?x) AS ?nbpatteints)  \n WHERE{"
        select2 = "SELECT  (COUNT( ?z) AS ?nbhabitants) \n WHERE{"
        select3 = "SELECT (COUNT( ?w) AS ?nbhop) \n WHERE{"
        select4 = "SELECT (COUNT(?e) AS ?nbmed ) \n WHERE{"
        cmd = "OPTIONAL{?x a ns2:pCovid_grave."
        cmd1 = "?x ns2:habite_a <file://PROJET.owl#15.TIZIOUZOU>.}}"
        cmd11 = "OPTIONAL{?e a ns2:Medecin."
        cmd12 = "?e ns2:habite_a <file://PROJET.owl#15.TIZIOUZOU>.}}"
        cmd2 = "OPTIONAL{<file://PROJET.owl#15.TIZIOUZOU> ns2:a_pour_habitant ?z.}}"
        cmd3 = "OPTIONAL{<file://PROJET.owl#15.TIZIOUZOU> ns2:contient_hopital ?w}}"

        requete = prefixe + select1 + cmd + cmd1
        x = []
        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))

        requete = prefixe + select2 + cmd2

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        requete = prefixe + select3 + cmd3

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        requete = prefixe + select4 + cmd11 + cmd12

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        print(requete)
        self.msg = QtWidgets.QMessageBox()
        self.msg.setText(
            "WILAYA DE TIZI-OUZOU:\nNombre d'habitants:" + x[1] + "\nNombre de personne atteintes de covid: " + x[
                0] + "\nNombre d'hopitaux: " + x[2] + "\nNombre de medecins: " + x[3])
        self.msg.show()
        print("fin")

    def f16(self):
        print("debut")
        wsjdid.sauvegarde()
        graph = wsjdid.default_world.as_rdflib_graph()
        prefixe = "prefix ns1: <http://www.w3.org/2002/07/owl#> \nprefix ns2: <file://PROJET.owl#> \nprefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \nprefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> \nprefix xml: <http://www.w3.org/XML/1998/namespace> \nprefix xsd: <http://www.w3.org/2001/XMLSchema#>\n "
        select1 = "SELECT (COUNT( ?x) AS ?nbpatteints)  \n WHERE{"
        select2 = "SELECT  (COUNT( ?z) AS ?nbhabitants) \n WHERE{"
        select3 = "SELECT (COUNT( ?w) AS ?nbhop) \n WHERE{"
        select4 = "SELECT (COUNT(?e) AS ?nbmed ) \n WHERE{"
        cmd = "OPTIONAL{?x a ns2:pCovid_grave."
        cmd1 = "?x ns2:habite_a <file://PROJET.owl#16.ALGER>.}}"
        cmd11 = "OPTIONAL{?e a ns2:Medecin."
        cmd12 = "?e ns2:habite_a <file://PROJET.owl#16.ALGER>.}}"
        cmd2 = "OPTIONAL{<file://PROJET.owl#16.ALGER> ns2:a_pour_habitant ?z.}}"
        cmd3 = "OPTIONAL{<file://PROJET.owl#16.ALGER> ns2:contient_hopital ?w}}"

        requete = prefixe + select1 + cmd + cmd1
        x = []
        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))

        requete = prefixe + select2 + cmd2

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        requete = prefixe + select3 + cmd3

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        requete = prefixe + select4 + cmd11 + cmd12

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        print(requete)
        self.msg = QtWidgets.QMessageBox()
        self.msg.setText(
            "WILAYA DE ALGER:\nNombre d'habitants:" + x[1] + "\nNombre de personne atteintes de covid: " + x[
                0] + "\nNombre d'hopitaux: " + x[2] + "\nNombre de medecins: " + x[3])
        self.msg.show()
        print("fin")

    def f17(self):
        print("debut")
        wsjdid.sauvegarde()
        graph = wsjdid.default_world.as_rdflib_graph()
        prefixe = "prefix ns1: <http://www.w3.org/2002/07/owl#> \nprefix ns2: <file://PROJET.owl#> \nprefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \nprefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> \nprefix xml: <http://www.w3.org/XML/1998/namespace> \nprefix xsd: <http://www.w3.org/2001/XMLSchema#>\n "
        select1 = "SELECT (COUNT( ?x) AS ?nbpatteints)  \n WHERE{"
        select2 = "SELECT  (COUNT( ?z) AS ?nbhabitants) \n WHERE{"
        select3 = "SELECT (COUNT( ?w) AS ?nbhop) \n WHERE{"
        select4 = "SELECT (COUNT(?e) AS ?nbmed ) \n WHERE{"
        cmd = "OPTIONAL{?x a ns2:pCovid_grave."
        cmd1 = "?x ns2:habite_a <file://PROJET.owl#17.DJELFA>.}}"
        cmd11 = "OPTIONAL{?e a ns2:Medecin."
        cmd12 = "?e ns2:habite_a <file://PROJET.owl#17.DJELFA>.}}"
        cmd2 = "OPTIONAL{<file://PROJET.owl#17.DJELFA> ns2:a_pour_habitant ?z.}}"
        cmd3 = "OPTIONAL{<file://PROJET.owl#17.DJELFA> ns2:contient_hopital ?w}}"

        requete = prefixe + select1 + cmd + cmd1
        x = []
        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))

        requete = prefixe + select2 + cmd2

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        requete = prefixe + select3 + cmd3

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        requete = prefixe + select4 + cmd11 + cmd12

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        print(requete)
        self.msg = QtWidgets.QMessageBox()
        self.msg.setText(
            "WILAYA DE DJELFA:\nNombre d'habitants:" + x[1] + "\nNombre de personne atteintes de covid: " + x[
                0] + "\nNombre d'hopitaux: " + x[2] + "\nNombre de medecins: " + x[3])
        self.msg.show()
        print("fin")

    def f18(self):
        print("debut")
        wsjdid.sauvegarde()
        graph = wsjdid.default_world.as_rdflib_graph()
        prefixe = "prefix ns1: <http://www.w3.org/2002/07/owl#> \nprefix ns2: <file://PROJET.owl#> \nprefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \nprefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> \nprefix xml: <http://www.w3.org/XML/1998/namespace> \nprefix xsd: <http://www.w3.org/2001/XMLSchema#>\n "
        select1 = "SELECT (COUNT( ?x) AS ?nbpatteints)  \n WHERE{"
        select2 = "SELECT  (COUNT( ?z) AS ?nbhabitants) \n WHERE{"
        select3 = "SELECT (COUNT( ?w) AS ?nbhop) \n WHERE{"
        select4 = "SELECT (COUNT(?e) AS ?nbmed ) \n WHERE{"
        cmd = "OPTIONAL{?x a ns2:pCovid_grave."
        cmd1 = "?x ns2:habite_a <file://PROJET.owl#18.JIJEL>.}}"
        cmd11 = "OPTIONAL{?e a ns2:Medecin."
        cmd12 = "?e ns2:habite_a <file://PROJET.owl#18.JIJEL>.}}"
        cmd2 = "OPTIONAL{<file://PROJET.owl#18.JIJEL> ns2:a_pour_habitant ?z.}}"
        cmd3 = "OPTIONAL{<file://PROJET.owl#18.JIJEL> ns2:contient_hopital ?w}}"

        requete = prefixe + select1 + cmd + cmd1
        x = []
        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))

        requete = prefixe + select2 + cmd2

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        requete = prefixe + select3 + cmd3

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        requete = prefixe + select4 + cmd11 + cmd12

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        print(requete)
        self.msg = QtWidgets.QMessageBox()
        self.msg.setText(
            "WILAYA DE JIJEL:\nNombre d'habitants:" + x[1] + "\nNombre de personne atteintes de covid: " + x[
                0] + "\nNombre d'hopitaux: " + x[2] + "\nNombre de medecins: " + x[3])
        self.msg.show()
        print("fin")

    def f19(self):
        print("debut")
        wsjdid.sauvegarde()
        graph = wsjdid.default_world.as_rdflib_graph()
        prefixe = "prefix ns1: <http://www.w3.org/2002/07/owl#> \nprefix ns2: <file://PROJET.owl#> \nprefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \nprefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> \nprefix xml: <http://www.w3.org/XML/1998/namespace> \nprefix xsd: <http://www.w3.org/2001/XMLSchema#>\n "
        select1 = "SELECT (COUNT( ?x) AS ?nbpatteints)  \n WHERE{"
        select2 = "SELECT  (COUNT( ?z) AS ?nbhabitants) \n WHERE{"
        select3 = "SELECT (COUNT( ?w) AS ?nbhop) \n WHERE{"
        select4 = "SELECT (COUNT(?e) AS ?nbmed ) \n WHERE{"
        cmd = "OPTIONAL{?x a ns2:pCovid_grave."
        cmd1 = "?x ns2:habite_a <file://PROJET.owl#19.SETIF>.}}"
        cmd11 = "OPTIONAL{?e a ns2:Medecin."
        cmd12 = "?e ns2:habite_a <file://PROJET.owl#19.SETIF>.}}"
        cmd2 = "OPTIONAL{<file://PROJET.owl#19.SETIF> ns2:a_pour_habitant ?z.}}"
        cmd3 = "OPTIONAL{<file://PROJET.owl#19.SETIF> ns2:contient_hopital ?w}}"

        requete = prefixe + select1 + cmd + cmd1
        x = []
        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))

        requete = prefixe + select2 + cmd2

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        requete = prefixe + select3 + cmd3

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        requete = prefixe + select4 + cmd11 + cmd12

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        print(requete)
        self.msg = QtWidgets.QMessageBox()
        self.msg.setText(
            "WILAYA DE SETIF:\nNombre d'habitants:" + x[1] + "\nNombre de personne atteintes de covid: " + x[
                0] + "\nNombre d'hopitaux: " + x[2] + "\nNombre de medecins: " + x[3])
        self.msg.show()
        print("fin")

    def f20(self):
        print("debut")
        wsjdid.sauvegarde()
        graph = wsjdid.default_world.as_rdflib_graph()
        prefixe = "prefix ns1: <http://www.w3.org/2002/07/owl#> \nprefix ns2: <file://PROJET.owl#> \nprefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \nprefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> \nprefix xml: <http://www.w3.org/XML/1998/namespace> \nprefix xsd: <http://www.w3.org/2001/XMLSchema#>\n "
        select1 = "SELECT (COUNT( ?x) AS ?nbpatteints)  \n WHERE{"
        select2 = "SELECT  (COUNT( ?z) AS ?nbhabitants) \n WHERE{"
        select3 = "SELECT (COUNT( ?w) AS ?nbhop) \n WHERE{"
        select4 = "SELECT (COUNT(?e) AS ?nbmed ) \n WHERE{"
        cmd = "OPTIONAL{?x a ns2:pCovid_grave."
        cmd1 = "?x ns2:habite_a <file://PROJET.owl#20.SAIDA>.}}"
        cmd11 = "OPTIONAL{?e a ns2:Medecin."
        cmd12 = "?e ns2:habite_a <file://PROJET.owl#20.SAIDA>.}}"
        cmd2 = "OPTIONAL{<file://PROJET.owl#20.SAIDA> ns2:a_pour_habitant ?z.}}"
        cmd3 = "OPTIONAL{<file://PROJET.owl#20.SAIDA> ns2:contient_hopital ?w}}"

        requete = prefixe + select1 + cmd + cmd1
        x = []
        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))

        requete = prefixe + select2 + cmd2

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        requete = prefixe + select3 + cmd3

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        requete = prefixe + select4 + cmd11 + cmd12

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        print(requete)
        self.msg = QtWidgets.QMessageBox()
        self.msg.setText(
            "WILAYA DE SAIDA:\nNombre d'habitants:" + x[1] + "\nNombre de personne atteintes de covid: " + x[
                0] + "\nNombre d'hopitaux: " + x[2] + "\nNombre de medecins: " + x[3])
        self.msg.show()
        print("fin")

    def f21(self):
        print("debut")
        wsjdid.sauvegarde()
        graph = wsjdid.default_world.as_rdflib_graph()
        prefixe = "prefix ns1: <http://www.w3.org/2002/07/owl#> \nprefix ns2: <file://PROJET.owl#> \nprefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \nprefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> \nprefix xml: <http://www.w3.org/XML/1998/namespace> \nprefix xsd: <http://www.w3.org/2001/XMLSchema#>\n "
        select1 = "SELECT (COUNT( ?x) AS ?nbpatteints)  \n WHERE{"
        select2 = "SELECT  (COUNT( ?z) AS ?nbhabitants) \n WHERE{"
        select3 = "SELECT (COUNT( ?w) AS ?nbhop) \n WHERE{"
        select4 = "SELECT (COUNT(?e) AS ?nbmed ) \n WHERE{"
        cmd = "OPTIONAL{?x a ns2:pCovid_grave."
        cmd1 = "?x ns2:habite_a <file://PROJET.owl#21.SKIKDA>.}}"
        cmd11 = "OPTIONAL{?e a ns2:Medecin."
        cmd12 = "?e ns2:habite_a <file://PROJET.owl#21.SKIKDA>.}}"
        cmd2 = "OPTIONAL{<file://PROJET.owl#21.SKIKDA> ns2:a_pour_habitant ?z.}}"
        cmd3 = "OPTIONAL{<file://PROJET.owl#21.SKIKDA> ns2:contient_hopital ?w}}"

        requete = prefixe + select1 + cmd + cmd1
        x = []
        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))

        requete = prefixe + select2 + cmd2

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        requete = prefixe + select3 + cmd3

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        requete = prefixe + select4 + cmd11 + cmd12

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        print(requete)
        self.msg = QtWidgets.QMessageBox()
        self.msg.setText(
            "WILAYA DE ALGER:\nNombre d'habitants:" + x[1] + "\nNombre de personne atteintes de covid: " + x[
                0] + "\nNombre d'hopitaux: " + x[2] + "\nNombre de medecins: " + x[3])
        self.msg.show()
        print("fin")

    def f22(self):
        print("debut")
        wsjdid.sauvegarde()
        graph = wsjdid.default_world.as_rdflib_graph()
        prefixe = "prefix ns1: <http://www.w3.org/2002/07/owl#> \nprefix ns2: <file://PROJET.owl#> \nprefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \nprefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> \nprefix xml: <http://www.w3.org/XML/1998/namespace> \nprefix xsd: <http://www.w3.org/2001/XMLSchema#>\n "
        select1 = "SELECT (COUNT( ?x) AS ?nbpatteints)  \n WHERE{"
        select2 = "SELECT  (COUNT( ?z) AS ?nbhabitants) \n WHERE{"
        select3 = "SELECT (COUNT( ?w) AS ?nbhop) \n WHERE{"
        select4 = "SELECT (COUNT(?e) AS ?nbmed ) \n WHERE{"
        cmd = "OPTIONAL{?x a ns2:pCovid_grave."
        cmd1 = "?x ns2:habite_a <file://PROJET.owl#22.SIDIBELABBES>.}}"
        cmd11 = "OPTIONAL{?e a ns2:Medecin."
        cmd12 = "?e ns2:habite_a <file://PROJET.owl#22.SIDIBELABBES>.}}"
        cmd2 = "OPTIONAL{<file://PROJET.owl#22.SIDIBELABBES> ns2:a_pour_habitant ?z.}}"
        cmd3 = "OPTIONAL{<file://PROJET.owl#22.SIDIBELABBES> ns2:contient_hopital ?w}}"

        requete = prefixe + select1 + cmd + cmd1
        x = []
        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))

        requete = prefixe + select2 + cmd2

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        requete = prefixe + select3 + cmd3

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        requete = prefixe + select4 + cmd11 + cmd12

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        print(requete)
        self.msg = QtWidgets.QMessageBox()
        self.msg.setText(
            "WILAYA DE SIDIBELABBES>:\nNombre d'habitants:" + x[1] + "\nNombre de personne atteintes de covid: " + x[
                0] + "\nNombre d'hopitaux: " + x[2] + "\nNombre de medecins: " + x[3])
        self.msg.show()
        print("fin")

    def f23(self):
        print("debut")
        wsjdid.sauvegarde()
        graph = wsjdid.default_world.as_rdflib_graph()
        prefixe = "prefix ns1: <http://www.w3.org/2002/07/owl#> \nprefix ns2: <file://PROJET.owl#> \nprefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \nprefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> \nprefix xml: <http://www.w3.org/XML/1998/namespace> \nprefix xsd: <http://www.w3.org/2001/XMLSchema#>\n "
        select1 = "SELECT (COUNT( ?x) AS ?nbpatteints)  \n WHERE{"
        select2 = "SELECT  (COUNT( ?z) AS ?nbhabitants) \n WHERE{"
        select3 = "SELECT (COUNT( ?w) AS ?nbhop) \n WHERE{"
        select4 = "SELECT (COUNT(?e) AS ?nbmed ) \n WHERE{"
        cmd = "OPTIONAL{?x a ns2:pCovid_grave."
        cmd1 = "?x ns2:habite_a <file://PROJET.owl#23.ANNABA>.}}"
        cmd11 = "OPTIONAL{?e a ns2:Medecin."
        cmd12 = "?e ns2:habite_a <file://PROJET.owl#23.ANNABA>.}}"
        cmd2 = "OPTIONAL{<file://PROJET.owl#23.ANNABA> ns2:a_pour_habitant ?z.}}"
        cmd3 = "OPTIONAL{<file://PROJET.owl#23.ANNABA> ns2:contient_hopital ?w}}"

        requete = prefixe + select1 + cmd + cmd1
        x = []
        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))

        requete = prefixe + select2 + cmd2

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        requete = prefixe + select3 + cmd3

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        requete = prefixe + select4 + cmd11 + cmd12

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        print(requete)
        self.msg = QtWidgets.QMessageBox()
        self.msg.setText(
            "WILAYA DE ANNABA:\nNombre d'habitants:" + x[1] + "\nNombre de personne atteintes de covid: " + x[
                0] + "\nNombre d'hopitaux: " + x[2] + "\nNombre de medecins: " + x[3])
        self.msg.show()
        print("fin")

    def f24(self):
        print("debut")
        wsjdid.sauvegarde()
        graph = wsjdid.default_world.as_rdflib_graph()
        prefixe = "prefix ns1: <http://www.w3.org/2002/07/owl#> \nprefix ns2: <file://PROJET.owl#> \nprefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \nprefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> \nprefix xml: <http://www.w3.org/XML/1998/namespace> \nprefix xsd: <http://www.w3.org/2001/XMLSchema#>\n "
        select1 = "SELECT (COUNT( ?x) AS ?nbpatteints)  \n WHERE{"
        select2 = "SELECT  (COUNT( ?z) AS ?nbhabitants) \n WHERE{"
        select3 = "SELECT (COUNT( ?w) AS ?nbhop) \n WHERE{"
        select4 = "SELECT (COUNT(?e) AS ?nbmed ) \n WHERE{"
        cmd = "OPTIONAL{?x a ns2:pCovid_grave."
        cmd1 = "?x ns2:habite_a <file://PROJET.owl#24.GUELMA>.}}"
        cmd11 = "OPTIONAL{?e a ns2:Medecin."
        cmd12 = "?e ns2:habite_a <file://PROJET.owl#24.GUELMA>.}}"
        cmd2 = "OPTIONAL{<file://PROJET.owl#24.GUELMA> ns2:a_pour_habitant ?z.}}"
        cmd3 = "OPTIONAL{<file://PROJET.owl#24.GUELMA> ns2:contient_hopital ?w}}"

        requete = prefixe + select1 + cmd + cmd1
        x = []
        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))

        requete = prefixe + select2 + cmd2

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        requete = prefixe + select3 + cmd3

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        requete = prefixe + select4 + cmd11 + cmd12

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        print(requete)
        self.msg = QtWidgets.QMessageBox()
        self.msg.setText(
            "WILAYA DE GUELMA>:\nNombre d'habitants:" + x[1] + "\nNombre de personne atteintes de covid: " + x[
                0] + "\nNombre d'hopitaux: " + x[2] + "\nNombre de medecins: " + x[3])
        self.msg.show()
        print("fin")

    def f25(self):
        print("debut")
        wsjdid.sauvegarde()
        graph = wsjdid.default_world.as_rdflib_graph()
        prefixe = "prefix ns1: <http://www.w3.org/2002/07/owl#> \nprefix ns2: <file://PROJET.owl#> \nprefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \nprefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> \nprefix xml: <http://www.w3.org/XML/1998/namespace> \nprefix xsd: <http://www.w3.org/2001/XMLSchema#>\n "
        select1 = "SELECT (COUNT( ?x) AS ?nbpatteints)  \n WHERE{"
        select2 = "SELECT  (COUNT( ?z) AS ?nbhabitants) \n WHERE{"
        select3 = "SELECT (COUNT( ?w) AS ?nbhop) \n WHERE{"
        select4 = "SELECT (COUNT(?e) AS ?nbmed ) \n WHERE{"
        cmd = "OPTIONAL{?x a ns2:pCovid_grave."
        cmd1 = "?x ns2:habite_a <file://PROJET.owl#25.CONSTANTINE>.}}"
        cmd11 = "OPTIONAL{?e a ns2:Medecin."
        cmd12 = "?e ns2:habite_a <file://PROJET.owl#25.CONSTANTINE>.}}"
        cmd2 = "OPTIONAL{<file://PROJET.owl#25.CONSTANTINE> ns2:a_pour_habitant ?z.}}"
        cmd3 = "OPTIONAL{<file://PROJET.owl#25.CONSTANTINE> ns2:contient_hopital ?w}}"

        requete = prefixe + select1 + cmd + cmd1
        x = []
        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))

        requete = prefixe + select2 + cmd2

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        requete = prefixe + select3 + cmd3

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        requete = prefixe + select4 + cmd11 + cmd12

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        print(requete)
        self.msg = QtWidgets.QMessageBox()
        self.msg.setText(
            "WILAYA DE CONSTANTINE>:\nNombre d'habitants:" + x[1] + "\nNombre de personne atteintes de covid: " + x[
                0] + "\nNombre d'hopitaux: " + x[2] + "\nNombre de medecins: " + x[3])
        self.msg.show()
        print("fin")

    def f26(self):
        print("debut")
        wsjdid.sauvegarde()
        graph = wsjdid.default_world.as_rdflib_graph()
        prefixe = "prefix ns1: <http://www.w3.org/2002/07/owl#> \nprefix ns2: <file://PROJET.owl#> \nprefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \nprefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> \nprefix xml: <http://www.w3.org/XML/1998/namespace> \nprefix xsd: <http://www.w3.org/2001/XMLSchema#>\n "
        select1 = "SELECT (COUNT( ?x) AS ?nbpatteints)  \n WHERE{"
        select2 = "SELECT  (COUNT( ?z) AS ?nbhabitants) \n WHERE{"
        select3 = "SELECT (COUNT( ?w) AS ?nbhop) \n WHERE{"
        select4 = "SELECT (COUNT(?e) AS ?nbmed ) \n WHERE{"
        cmd = "OPTIONAL{?x a ns2:pCovid_grave."
        cmd1 = "?x ns2:habite_a <file://PROJET.owl#26.MEDEA>.}}"
        cmd11 = "OPTIONAL{?e a ns2:Medecin."
        cmd12 = "?e ns2:habite_a <file://PROJET.owl#26.MEDEA>.}}"
        cmd2 = "OPTIONAL{<file://PROJET.owl#26.MEDEA> ns2:a_pour_habitant ?z.}}"
        cmd3 = "OPTIONAL{<file://PROJET.owl#26.MEDEA> ns2:contient_hopital ?w}}"

        requete = prefixe + select1 + cmd + cmd1
        x = []
        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))

        requete = prefixe + select2 + cmd2

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        requete = prefixe + select3 + cmd3

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        requete = prefixe + select4 + cmd11 + cmd12

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        print(requete)
        self.msg = QtWidgets.QMessageBox()
        self.msg.setText(
            "WILAYA DE MEDEA>:\nNombre d'habitants:" + x[1] + "\nNombre de personne atteintes de covid: " + x[
                0] + "\nNombre d'hopitaux: " + x[2] + "\nNombre de medecins: " + x[3])
        self.msg.show()
        print("fin")

    def f27(self):
        print("debut")
        wsjdid.sauvegarde()
        graph = wsjdid.default_world.as_rdflib_graph()
        prefixe = "prefix ns1: <http://www.w3.org/2002/07/owl#> \nprefix ns2: <file://PROJET.owl#> \nprefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \nprefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> \nprefix xml: <http://www.w3.org/XML/1998/namespace> \nprefix xsd: <http://www.w3.org/2001/XMLSchema#>\n "
        select1 = "SELECT (COUNT( ?x) AS ?nbpatteints)  \n WHERE{"
        select2 = "SELECT  (COUNT( ?z) AS ?nbhabitants) \n WHERE{"
        select3 = "SELECT (COUNT( ?w) AS ?nbhop) \n WHERE{"
        select4 = "SELECT (COUNT(?e) AS ?nbmed ) \n WHERE{"
        cmd = "OPTIONAL{?x a ns2:pCovid_grave."
        cmd1 = "?x ns2:habite_a <file://PROJET.owl#27.MOSTAGANEM>.}}"
        cmd11 = "OPTIONAL{?e a ns2:Medecin."
        cmd12 = "?e ns2:habite_a <file://PROJET.owl#27.MOSTAGANEM>.}}"
        cmd2 = "OPTIONAL{<file://PROJET.owl#27.MOSTAGANEM> ns2:a_pour_habitant ?z.}}"
        cmd3 = "OPTIONAL{<file://PROJET.owl#27.MOSTAGANEM> ns2:contient_hopital ?w}}"

        requete = prefixe + select1 + cmd + cmd1
        x = []
        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))

        requete = prefixe + select2 + cmd2

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        requete = prefixe + select3 + cmd3

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        requete = prefixe + select4 + cmd11 + cmd12

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        print(requete)
        self.msg = QtWidgets.QMessageBox()
        self.msg.setText(
            "WILAYA DE MOSTAGANEM>:\nNombre d'habitants:" + x[1] + "\nNombre de personne atteintes de covid: " + x[
                0] + "\nNombre d'hopitaux: " + x[2] + "\nNombre de medecins: " + x[3])
        self.msg.show()
        print("fin")

    def f28(self):
        print("debut")
        wsjdid.sauvegarde()
        graph = wsjdid.default_world.as_rdflib_graph()
        prefixe = "prefix ns1: <http://www.w3.org/2002/07/owl#> \nprefix ns2: <file://PROJET.owl#> \nprefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \nprefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> \nprefix xml: <http://www.w3.org/XML/1998/namespace> \nprefix xsd: <http://www.w3.org/2001/XMLSchema#>\n "
        select1 = "SELECT (COUNT( ?x) AS ?nbpatteints)  \n WHERE{"
        select2 = "SELECT  (COUNT( ?z) AS ?nbhabitants) \n WHERE{"
        select3 = "SELECT (COUNT( ?w) AS ?nbhop) \n WHERE{"
        select4 = "SELECT (COUNT(?e) AS ?nbmed ) \n WHERE{"
        cmd = "OPTIONAL{?x a ns2:pCovid_grave."
        cmd1 = "?x ns2:habite_a <file://PROJET.owl#28.M'SILA>.}}"
        cmd11 = "OPTIONAL{?e a ns2:Medecin."
        cmd12 = "?e ns2:habite_a <file://PROJET.owl#28.M'SILA>.}}"
        cmd2 = "OPTIONAL{<file://PROJET.owl#28.M'SILA> ns2:a_pour_habitant ?z.}}"
        cmd3 = "OPTIONAL{<file://PROJET.owl#28.M'SILA> ns2:contient_hopital ?w}}"

        requete = prefixe + select1 + cmd + cmd1
        x = []
        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))

        requete = prefixe + select2 + cmd2

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        requete = prefixe + select3 + cmd3

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        requete = prefixe + select4 + cmd11 + cmd12

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        print(requete)
        self.msg = QtWidgets.QMessageBox()
        self.msg.setText(
            "WILAYA DE M'SILA>:\nNombre d'habitants:" + x[1] + "\nNombre de personne atteintes de covid: " + x[
                0] + "\nNombre d'hopitaux: " + x[2] + "\nNombre de medecins: " + x[3])
        self.msg.show()
        print("fin")

    def f29(self):
        print("debut")
        wsjdid.sauvegarde()
        graph = wsjdid.default_world.as_rdflib_graph()
        prefixe = "prefix ns1: <http://www.w3.org/2002/07/owl#> \nprefix ns2: <file://PROJET.owl#> \nprefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \nprefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> \nprefix xml: <http://www.w3.org/XML/1998/namespace> \nprefix xsd: <http://www.w3.org/2001/XMLSchema#>\n "
        select1 = "SELECT (COUNT( ?x) AS ?nbpatteints)  \n WHERE{"
        select2 = "SELECT  (COUNT( ?z) AS ?nbhabitants) \n WHERE{"
        select3 = "SELECT (COUNT( ?w) AS ?nbhop) \n WHERE{"
        select4 = "SELECT (COUNT(?e) AS ?nbmed ) \n WHERE{"
        cmd = "OPTIONAL{?x a ns2:pCovid_grave."
        cmd1 = "?x ns2:habite_a <file://PROJET.owl#29.MASCARA>.}}"
        cmd11 = "OPTIONAL{?e a ns2:Medecin."
        cmd12 = "?e ns2:habite_a <file://PROJET.owl#29.MASCARA>.}}"
        cmd2 = "OPTIONAL{<file://PROJET.owl#29.MASCARA> ns2:a_pour_habitant ?z.}}"
        cmd3 = "OPTIONAL{<file://PROJET.owl#29.MASCARA> ns2:contient_hopital ?w}}"

        requete = prefixe + select1 + cmd + cmd1
        x = []
        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))

        requete = prefixe + select2 + cmd2

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        requete = prefixe + select3 + cmd3

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        requete = prefixe + select4 + cmd11 + cmd12

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        print(requete)
        self.msg = QtWidgets.QMessageBox()
        self.msg.setText(
            "WILAYA DE MASCARA:\nNombre d'habitants:" + x[1] + "\nNombre de personne atteintes de covid: " + x[
                0] + "\nNombre d'hopitaux: " + x[2] + "\nNombre de medecins: " + x[3])
        self.msg.show()
        print("fin")
    def f30(self):

            print("debut")
            wsjdid.sauvegarde()
            graph = wsjdid.default_world.as_rdflib_graph()
            prefixe = "prefix ns1: <http://www.w3.org/2002/07/owl#> \nprefix ns2: <file://PROJET.owl#> \nprefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \nprefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> \nprefix xml: <http://www.w3.org/XML/1998/namespace> \nprefix xsd: <http://www.w3.org/2001/XMLSchema#>\n "
            select1 = "SELECT (COUNT( ?x) AS ?nbpatteints)  \n WHERE{"
            select2 = "SELECT  (COUNT( ?z) AS ?nbhabitants) \n WHERE{"
            select3 = "SELECT (COUNT( ?w) AS ?nbhop) \n WHERE{"
            select4 = "SELECT (COUNT(?e) AS ?nbmed ) \n WHERE{"
            cmd = "OPTIONAL{?x a ns2:pCovid_grave."
            cmd1 = "?x ns2:habite_a <file://PROJET.owl#30.OUARGLA>.}}"
            cmd11 = "OPTIONAL{?e a ns2:Medecin."
            cmd12 = "?e ns2:habite_a <file://PROJET.owl#30.OUARGLA>.}}"
            cmd2 = "OPTIONAL{<file://PROJET.owl#30.OUARGLA> ns2:a_pour_habitant ?z.}}"
            cmd3 = "OPTIONAL{<file://PROJET.owl#30.OUARGLA> ns2:contient_hopital ?w}}"

            requete = prefixe + select1 + cmd + cmd1
            x = []
            res = graph.query(requete)

            for i in res:
                x.append(str(i[0]))

            requete = prefixe + select2 + cmd2

            res = graph.query(requete)

            for i in res:
                x.append(str(i[0]))
            requete = prefixe + select3 + cmd3

            res = graph.query(requete)

            for i in res:
                x.append(str(i[0]))
            requete = prefixe + select4 + cmd11 + cmd12

            res = graph.query(requete)

            for i in res:
                x.append(str(i[0]))
            print(requete)
            self.msg = QtWidgets.QMessageBox()
            self.msg.setText(
                "WILAYA DE OUARGLA:\nNombre d'habitants:" + x[1] + "\nNombre de personne atteintes de covid: " + x[
                    0] + "\nNombre d'hopitaux: " + x[2] + "\nNombre de medecins: " + x[3])
            self.msg.show()
            print("fin")
    def f31(self):
        print("debut")
        wsjdid.sauvegarde()
        graph = wsjdid.default_world.as_rdflib_graph()
        prefixe = "prefix ns1: <http://www.w3.org/2002/07/owl#> \nprefix ns2: <file://PROJET.owl#> \nprefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \nprefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> \nprefix xml: <http://www.w3.org/XML/1998/namespace> \nprefix xsd: <http://www.w3.org/2001/XMLSchema#>\n "
        select1 = "SELECT (COUNT( ?x) AS ?nbpatteints)  \n WHERE{"
        select2 = "SELECT  (COUNT( ?z) AS ?nbhabitants) \n WHERE{"
        select3 = "SELECT (COUNT( ?w) AS ?nbhop) \n WHERE{"
        select4 = "SELECT (COUNT(?e) AS ?nbmed ) \n WHERE{"
        cmd = "OPTIONAL{?x a ns2:pCovid_grave."
        cmd1 = "?x ns2:habite_a <file://PROJET.owl#31.ORAN>.}}"
        cmd11 = "OPTIONAL{?e a ns2:Medecin."
        cmd12 = "?e ns2:habite_a <file://PROJET.owl#31.ORAN>.}}"
        cmd2 = "OPTIONAL{<file://PROJET.owl#31.ORAN> ns2:a_pour_habitant ?z.}}"
        cmd3 = "OPTIONAL{<file://PROJET.owl#31.ORAN> ns2:contient_hopital ?w}}"

        requete = prefixe + select1 + cmd + cmd1
        x = []
        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))

        requete = prefixe + select2 + cmd2

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        requete = prefixe + select3 + cmd3

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        requete = prefixe + select4 + cmd11 + cmd12

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        print(requete)
        self.msg = QtWidgets.QMessageBox()
        self.msg.setText(
            "WILAYA DE ORAN:\nNombre d'habitants:" + x[1] + "\nNombre de personne atteintes de covid: " + x[
                0] + "\nNombre d'hopitaux: " + x[2] + "\nNombre de medecins: " + x[3])
        self.msg.show()
        print("fin")
    def f32(self):
        print("debut")
        wsjdid.sauvegarde()
        graph = wsjdid.default_world.as_rdflib_graph()
        prefixe = "prefix ns1: <http://www.w3.org/2002/07/owl#> \nprefix ns2: <file://PROJET.owl#> \nprefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \nprefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> \nprefix xml: <http://www.w3.org/XML/1998/namespace> \nprefix xsd: <http://www.w3.org/2001/XMLSchema#>\n "
        select1 = "SELECT (COUNT( ?x) AS ?nbpatteints)  \n WHERE{"
        select2 = "SELECT  (COUNT( ?z) AS ?nbhabitants) \n WHERE{"
        select3 = "SELECT (COUNT( ?w) AS ?nbhop) \n WHERE{"
        select4 = "SELECT (COUNT(?e) AS ?nbmed ) \n WHERE{"
        cmd = "OPTIONAL{?x a ns2:pCovid_grave."
        cmd1 = "?x ns2:habite_a <file://PROJET.owl#32.ELBAYDH>.}}"
        cmd11 = "OPTIONAL{?e a ns2:Medecin."
        cmd12 = "?e ns2:habite_a <file://PROJET.owl#32.ELBAYDH>.}}"
        cmd2 = "OPTIONAL{<file://PROJET.owl#32.ELBAYDH> ns2:a_pour_habitant ?z.}}"
        cmd3 = "OPTIONAL{<file://PROJET.owl#32.ELBAYDH> ns2:contient_hopital ?w}}"

        requete = prefixe + select1 + cmd + cmd1
        x = []
        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))

        requete = prefixe + select2 + cmd2

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        requete = prefixe + select3 + cmd3

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        requete = prefixe + select4 + cmd11 + cmd12

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        print(requete)
        self.msg = QtWidgets.QMessageBox()
        self.msg.setText(
            "WILAYA DE ELBAYDH:\nNombre d'habitants:" + x[1] + "\nNombre de personne atteintes de covid: " + x[
                0] + "\nNombre d'hopitaux: " + x[2] + "\nNombre de medecins: " + x[3])
        self.msg.show()
        print("fin")


    def f33(self):
        print("debut")
        wsjdid.sauvegarde()
        graph = wsjdid.default_world.as_rdflib_graph()
        prefixe = "prefix ns1: <http://www.w3.org/2002/07/owl#> \nprefix ns2: <file://PROJET.owl#> \nprefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \nprefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> \nprefix xml: <http://www.w3.org/XML/1998/namespace> \nprefix xsd: <http://www.w3.org/2001/XMLSchema#>\n "
        select1 = "SELECT (COUNT( ?x) AS ?nbpatteints)  \n WHERE{"
        select2 = "SELECT  (COUNT( ?z) AS ?nbhabitants) \n WHERE{"
        select3 = "SELECT (COUNT( ?w) AS ?nbhop) \n WHERE{"
        select4 = "SELECT (COUNT(?e) AS ?nbmed ) \n WHERE{"
        cmd = "OPTIONAL{?x a ns2:pCovid_grave."
        cmd1 = "?x ns2:habite_a <file://PROJET.owl#33.ILLIZI>.}}"
        cmd11 = "OPTIONAL{?e a ns2:Medecin."
        cmd12 = "?e ns2:habite_a <file://PROJET.owl#33.ILLIZI>.}}"
        cmd2 = "OPTIONAL{<file://PROJET.owl#33.ILLIZI> ns2:a_pour_habitant ?z.}}"
        cmd3 = "OPTIONAL{<file://PROJET.owl#33.ILLIZI> ns2:contient_hopital ?w}}"

        requete = prefixe + select1 + cmd + cmd1
        x = []
        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))

        requete = prefixe + select2 + cmd2

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        requete = prefixe + select3 + cmd3

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        requete = prefixe + select4 + cmd11 + cmd12

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        print(requete)
        self.msg = QtWidgets.QMessageBox()
        self.msg.setText(
            "WILAYA DE ILLIZI:\nNombre d'habitants:" + x[1] + "\nNombre de personne atteintes de covid: " + x[
                0] + "\nNombre d'hopitaux: " + x[2] + "\nNombre de medecins: " + x[3])
        self.msg.show()
        print("fin")
    def f34(self):
        print("debut")
        wsjdid.sauvegarde()
        graph = wsjdid.default_world.as_rdflib_graph()
        prefixe = "prefix ns1: <http://www.w3.org/2002/07/owl#> \nprefix ns2: <file://PROJET.owl#> \nprefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \nprefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> \nprefix xml: <http://www.w3.org/XML/1998/namespace> \nprefix xsd: <http://www.w3.org/2001/XMLSchema#>\n "
        select1 = "SELECT (COUNT( ?x) AS ?nbpatteints)  \n WHERE{"
        select2 = "SELECT  (COUNT( ?z) AS ?nbhabitants) \n WHERE{"
        select3 = "SELECT (COUNT( ?w) AS ?nbhop) \n WHERE{"
        select4 = "SELECT (COUNT(?e) AS ?nbmed ) \n WHERE{"
        cmd = "OPTIONAL{?x a ns2:pCovid_grave."
        cmd1 = "?x ns2:habite_a <file://PROJET.owl#34.BORDJBOUARRERIDJ>.}}"
        cmd11 = "OPTIONAL{?e a ns2:Medecin."
        cmd12 = "?e ns2:habite_a <file://PROJET.owl#34.BORDJBOUARRERIDJ>.}}"
        cmd2 = "OPTIONAL{<file://PROJET.owl#34.BORDJBOUARRERIDJ> ns2:a_pour_habitant ?z.}}"
        cmd3 = "OPTIONAL{<file://PROJET.owl#34.BORDJBOUARRERIDJ> ns2:contient_hopital ?w}}"

        requete = prefixe + select1 + cmd + cmd1
        x = []
        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))

        requete = prefixe + select2 + cmd2

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        requete = prefixe + select3 + cmd3

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        requete = prefixe + select4 + cmd11 + cmd12

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        print(requete)
        self.msg = QtWidgets.QMessageBox()
        self.msg.setText(
            "WILAYA DE BORDJBOUARRERIDJ:\nNombre d'habitants:" + x[1] + "\nNombre de personne atteintes de covid: " + x[
                0] + "\nNombre d'hopitaux: " + x[2] + "\nNombre de medecins: " + x[3])
        self.msg.show()
        print("fin")
    def f35(self):
        print("debut")
        wsjdid.sauvegarde()
        graph = wsjdid.default_world.as_rdflib_graph()
        prefixe = "prefix ns1: <http://www.w3.org/2002/07/owl#> \nprefix ns2: <file://PROJET.owl#> \nprefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \nprefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> \nprefix xml: <http://www.w3.org/XML/1998/namespace> \nprefix xsd: <http://www.w3.org/2001/XMLSchema#>\n "
        select1 = "SELECT (COUNT( ?x) AS ?nbpatteints)  \n WHERE{"
        select2 = "SELECT  (COUNT( ?z) AS ?nbhabitants) \n WHERE{"
        select3 = "SELECT (COUNT( ?w) AS ?nbhop) \n WHERE{"
        select4 = "SELECT (COUNT(?e) AS ?nbmed ) \n WHERE{"
        cmd = "OPTIONAL{?x a ns2:pCovid_grave."
        cmd1 = "?x ns2:habite_a <file://PROJET.owl#35.BOUMERDES>.}}"
        cmd11 = "OPTIONAL{?e a ns2:Medecin."
        cmd12 = "?e ns2:habite_a <file://PROJET.owl#35.BOUMERDES>.}}"
        cmd2 = "OPTIONAL{<file://PROJET.owl#35.BOUMERDES> ns2:a_pour_habitant ?z.}}"
        cmd3 = "OPTIONAL{<file://PROJET.owl#35.BOUMERDES> ns2:contient_hopital ?w}}"

        requete = prefixe + select1 + cmd + cmd1
        x = []
        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))

        requete = prefixe + select2 + cmd2

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        requete = prefixe + select3 + cmd3

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        requete = prefixe + select4 + cmd11 + cmd12

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        print(requete)
        self.msg = QtWidgets.QMessageBox()
        self.msg.setText(
            "WILAYA DE BOUMERDES:\nNombre d'habitants:" + x[1] + "\nNombre de personne atteintes de covid: " + x[
                0] + "\nNombre d'hopitaux: " + x[2] + "\nNombre de medecins: " + x[3])
        self.msg.show()
        print("fin")
    def f36(self):
        print("debut")
        wsjdid.sauvegarde()
        graph = wsjdid.default_world.as_rdflib_graph()
        prefixe = "prefix ns1: <http://www.w3.org/2002/07/owl#> \nprefix ns2: <file://PROJET.owl#> \nprefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \nprefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> \nprefix xml: <http://www.w3.org/XML/1998/namespace> \nprefix xsd: <http://www.w3.org/2001/XMLSchema#>\n "
        select1 = "SELECT (COUNT( ?x) AS ?nbpatteints)  \n WHERE{"
        select2 = "SELECT  (COUNT( ?z) AS ?nbhabitants) \n WHERE{"
        select3 = "SELECT (COUNT( ?w) AS ?nbhop) \n WHERE{"
        select4 = "SELECT (COUNT(?e) AS ?nbmed ) \n WHERE{"
        cmd = "OPTIONAL{?x a ns2:pCovid_grave."
        cmd1 = "?x ns2:habite_a <file://PROJET.owl#36.ELTAREF>.}}"
        cmd11 = "OPTIONAL{?e a ns2:Medecin."
        cmd12 = "?e ns2:habite_a <file://PROJET.owl#36.ELTAREF>.}}"
        cmd2 = "OPTIONAL{<file://PROJET.owl#36.ELTAREF> ns2:a_pour_habitant ?z.}}"
        cmd3 = "OPTIONAL{<file://PROJET.owl#36.ELTAREF> ns2:contient_hopital ?w}}"

        requete = prefixe + select1 + cmd + cmd1
        x = []
        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))

        requete = prefixe + select2 + cmd2

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        requete = prefixe + select3 + cmd3

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        requete = prefixe + select4 + cmd11 + cmd12

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        print(requete)
        self.msg = QtWidgets.QMessageBox()
        self.msg.setText(
            "WILAYA DE ELTAREF:\nNombre d'habitants:" + x[1] + "\nNombre de personne atteintes de covid: " + x[
                0] + "\nNombre d'hopitaux: " + x[2] + "\nNombre de medecins: " + x[3])
        self.msg.show()
        print("fin")
    def f37(self):
        print("debut")
        wsjdid.sauvegarde()
        graph = wsjdid.default_world.as_rdflib_graph()
        prefixe = "prefix ns1: <http://www.w3.org/2002/07/owl#> \nprefix ns2: <file://PROJET.owl#> \nprefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \nprefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> \nprefix xml: <http://www.w3.org/XML/1998/namespace> \nprefix xsd: <http://www.w3.org/2001/XMLSchema#>\n "
        select1 = "SELECT (COUNT( ?x) AS ?nbpatteints)  \n WHERE{"
        select2 = "SELECT  (COUNT( ?z) AS ?nbhabitants) \n WHERE{"
        select3 = "SELECT (COUNT( ?w) AS ?nbhop) \n WHERE{"
        select4 = "SELECT (COUNT(?e) AS ?nbmed ) \n WHERE{"
        cmd = "OPTIONAL{?x a ns2:pCovid_grave."
        cmd1 = "?x ns2:habite_a <file://PROJET.owl#37.TINDOUF>.}}"
        cmd11 = "OPTIONAL{?e a ns2:Medecin."
        cmd12 = "?e ns2:habite_a <file://PROJET.owl#37.TINDOUF>.}}"
        cmd2 = "OPTIONAL{<file://PROJET.owl#37.TINDOUF> ns2:a_pour_habitant ?z.}}"
        cmd3 = "OPTIONAL{<file://PROJET.owl#37.TINDOUF> ns2:contient_hopital ?w}}"

        requete = prefixe + select1 + cmd + cmd1
        x = []
        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))

        requete = prefixe + select2 + cmd2

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        requete = prefixe + select3 + cmd3

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        requete = prefixe + select4 + cmd11 + cmd12

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        print(requete)
        self.msg = QtWidgets.QMessageBox()
        self.msg.setText(
            "WILAYA DE TINDOUF:\nNombre d'habitants:" + x[1] + "\nNombre de personne atteintes de covid: " + x[
                0] + "\nNombre d'hopitaux: " + x[2] + "\nNombre de medecins: " + x[3])
        self.msg.show()
        print("fin")
    def f38(self):

        print("debut")
        wsjdid.sauvegarde()
        graph = wsjdid.default_world.as_rdflib_graph()
        prefixe = "prefix ns1: <http://www.w3.org/2002/07/owl#> \nprefix ns2: <file://PROJET.owl#> \nprefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \nprefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> \nprefix xml: <http://www.w3.org/XML/1998/namespace> \nprefix xsd: <http://www.w3.org/2001/XMLSchema#>\n "
        select1 = "SELECT (COUNT( ?x) AS ?nbpatteints)  \n WHERE{"
        select2 = "SELECT  (COUNT( ?z) AS ?nbhabitants) \n WHERE{"
        select3 = "SELECT (COUNT( ?w) AS ?nbhop) \n WHERE{"
        select4 = "SELECT (COUNT(?e) AS ?nbmed ) \n WHERE{"
        cmd = "OPTIONAL{?x a ns2:pCovid_grave."
        cmd1 = "?x ns2:habite_a <file://PROJET.owl#38.TISSEMSILT>.}}"
        cmd11 = "OPTIONAL{?e a ns2:Medecin."
        cmd12 = "?e ns2:habite_a <file://PROJET.owl#38.TISSEMSILT>.}}"
        cmd2 = "OPTIONAL{<file://PROJET.owl#38.TISSEMSILT> ns2:a_pour_habitant ?z.}}"
        cmd3 = "OPTIONAL{<file://PROJET.owl#38.TISSEMSILT> ns2:contient_hopital ?w}}"

        requete = prefixe + select1 + cmd + cmd1
        x = []
        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))

        requete = prefixe + select2 + cmd2

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        requete = prefixe + select3 + cmd3

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        requete = prefixe + select4 + cmd11 + cmd12

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        print(requete)
        self.msg = QtWidgets.QMessageBox()
        self.msg.setText(
            "WILAYA DE TISSEMSILT:\nNombre d'habitants:" + x[1] + "\nNombre de personne atteintes de covid: " + x[
                0] + "\nNombre d'hopitaux: " + x[2] + "\nNombre de medecins: " + x[3])
        self.msg.show()
        print("fin")
    def f39(self):
        print("debut")
        wsjdid.sauvegarde()
        graph = wsjdid.default_world.as_rdflib_graph()
        prefixe = "prefix ns1: <http://www.w3.org/2002/07/owl#> \nprefix ns2: <file://PROJET.owl#> \nprefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \nprefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> \nprefix xml: <http://www.w3.org/XML/1998/namespace> \nprefix xsd: <http://www.w3.org/2001/XMLSchema#>\n "
        select1 = "SELECT (COUNT( ?x) AS ?nbpatteints)  \n WHERE{"
        select2 = "SELECT  (COUNT( ?z) AS ?nbhabitants) \n WHERE{"
        select3 = "SELECT (COUNT( ?w) AS ?nbhop) \n WHERE{"
        select4 = "SELECT (COUNT(?e) AS ?nbmed ) \n WHERE{"
        cmd = "OPTIONAL{?x a ns2:pCovid_grave."
        cmd1 = "?x ns2:habite_a <file://PROJET.owl#39.ELOUED>.}}"
        cmd11 = "OPTIONAL{?e a ns2:Medecin."
        cmd12 = "?e ns2:habite_a <file://PROJET.owl#39.ELOUED>.}}"
        cmd2 = "OPTIONAL{<file://PROJET.owl#39.ELOUED> ns2:a_pour_habitant ?z.}}"
        cmd3 = "OPTIONAL{<file://PROJET.owl#39.ELOUED> ns2:contient_hopital ?w}}"

        requete = prefixe + select1 + cmd + cmd1
        x = []
        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))

        requete = prefixe + select2 + cmd2

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        requete = prefixe + select3 + cmd3

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        requete = prefixe + select4 + cmd11 + cmd12

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        print(requete)
        self.msg = QtWidgets.QMessageBox()
        self.msg.setText(
            "WILAYA DE ELOUED:\nNombre d'habitants:" + x[1] + "\nNombre de personne atteintes de covid: " + x[
                0] + "\nNombre d'hopitaux: " + x[2] + "\nNombre de medecins: " + x[3])
        self.msg.show()
        print("fin")
    def f40(self):
        print("debut")
        wsjdid.sauvegarde()
        graph = wsjdid.default_world.as_rdflib_graph()
        prefixe = "prefix ns1: <http://www.w3.org/2002/07/owl#> \nprefix ns2: <file://PROJET.owl#> \nprefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \nprefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> \nprefix xml: <http://www.w3.org/XML/1998/namespace> \nprefix xsd: <http://www.w3.org/2001/XMLSchema#>\n "
        select1 = "SELECT (COUNT( ?x) AS ?nbpatteints)  \n WHERE{"
        select2 = "SELECT  (COUNT( ?z) AS ?nbhabitants) \n WHERE{"
        select3 = "SELECT (COUNT( ?w) AS ?nbhop) \n WHERE{"
        select4 = "SELECT (COUNT(?e) AS ?nbmed ) \n WHERE{"
        cmd = "OPTIONAL{?x a ns2:pCovid_grave."
        cmd1 = "?x ns2:habite_a <file://PROJET.owl#40.KHENCHLA>.}}"
        cmd11 = "OPTIONAL{?e a ns2:Medecin."
        cmd12 = "?e ns2:habite_a <file://PROJET.owl#40.KHENCHLA>.}}"
        cmd2 = "OPTIONAL{<file://PROJET.owl#40.KHENCHLA> ns2:a_pour_habitant ?z.}}"
        cmd3 = "OPTIONAL{<file://PROJET.owl#40.KHENCHLA> ns2:contient_hopital ?w}}"

        requete = prefixe + select1 + cmd + cmd1
        x = []
        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))

        requete = prefixe + select2 + cmd2

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        requete = prefixe + select3 + cmd3

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        requete = prefixe + select4 + cmd11 + cmd12

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        print(requete)
        self.msg = QtWidgets.QMessageBox()
        self.msg.setText(
            "WILAYA DE KHENCHLA:\nNombre d'habitants:" + x[1] + "\nNombre de personne atteintes de covid: " + x[
                0] + "\nNombre d'hopitaux: " + x[2] + "\nNombre de medecins: " + x[3])
        self.msg.show()
        print("fin")
    def f41(self):
        print("debut")
        wsjdid.sauvegarde()
        graph = wsjdid.default_world.as_rdflib_graph()
        prefixe = "prefix ns1: <http://www.w3.org/2002/07/owl#> \nprefix ns2: <file://PROJET.owl#> \nprefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \nprefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> \nprefix xml: <http://www.w3.org/XML/1998/namespace> \nprefix xsd: <http://www.w3.org/2001/XMLSchema#>\n "
        select1 = "SELECT (COUNT( ?x) AS ?nbpatteints)  \n WHERE{"
        select2 = "SELECT  (COUNT( ?z) AS ?nbhabitants) \n WHERE{"
        select3 = "SELECT (COUNT( ?w) AS ?nbhop) \n WHERE{"
        select4 = "SELECT (COUNT(?e) AS ?nbmed ) \n WHERE{"
        cmd = "OPTIONAL{?x a ns2:pCovid_grave."
        cmd1 = "?x ns2:habite_a <file://PROJET.owl#41.SOUKAHRASS>.}}"
        cmd11 = "OPTIONAL{?e a ns2:Medecin."
        cmd12 = "?e ns2:habite_a <file://PROJET.owl#41.SOUKAHRASS>.}}"
        cmd2 = "OPTIONAL{<file://PROJET.owl#41.SOUKAHRASS> ns2:a_pour_habitant ?z.}}"
        cmd3 = "OPTIONAL{<file://PROJET.owl#41.SOUKAHRASS> ns2:contient_hopital ?w}}"

        requete = prefixe + select1 + cmd + cmd1
        x = []
        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))

        requete = prefixe + select2 + cmd2

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        requete = prefixe + select3 + cmd3

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        requete = prefixe + select4 + cmd11 + cmd12

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        print(requete)
        self.msg = QtWidgets.QMessageBox()
        self.msg.setText(
            "WILAYA DE SOUKAHRASS:\nNombre d'habitants:" + x[1] + "\nNombre de personne atteintes de covid: " + x[
                0] + "\nNombre d'hopitaux: " + x[2] + "\nNombre de medecins: " + x[3])
        self.msg.show()
        print("fin")
    def f42(self):

        print("debut")
        wsjdid.sauvegarde()
        graph = wsjdid.default_world.as_rdflib_graph()
        prefixe = "prefix ns1: <http://www.w3.org/2002/07/owl#> \nprefix ns2: <file://PROJET.owl#> \nprefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \nprefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> \nprefix xml: <http://www.w3.org/XML/1998/namespace> \nprefix xsd: <http://www.w3.org/2001/XMLSchema#>\n "
        select1 = "SELECT (COUNT( ?x) AS ?nbpatteints)  \n WHERE{"
        select2 = "SELECT  (COUNT( ?z) AS ?nbhabitants) \n WHERE{"
        select3 = "SELECT (COUNT( ?w) AS ?nbhop) \n WHERE{"
        select4 = "SELECT (COUNT(?e) AS ?nbmed ) \n WHERE{"
        cmd = "OPTIONAL{?x a ns2:pCovid_grave."
        cmd1 = "?x ns2:habite_a <file://PROJET.owl#42.TIPAZA>.}}"
        cmd11 = "OPTIONAL{?e a ns2:Medecin."
        cmd12 = "?e ns2:habite_a <file://PROJET.owl#42.TIPAZA>.}}"
        cmd2 = "OPTIONAL{<file://PROJET.owl#42.TIPAZA> ns2:a_pour_habitant ?z.}}"
        cmd3 = "OPTIONAL{<file://PROJET.owl#42.TIPAZA> ns2:contient_hopital ?w}}"

        requete = prefixe + select1 + cmd + cmd1
        x = []
        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))

        requete = prefixe + select2 + cmd2

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        requete = prefixe + select3 + cmd3

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        requete = prefixe + select4 + cmd11 + cmd12

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        print(requete)
        self.msg = QtWidgets.QMessageBox()
        self.msg.setText(
            "WILAYA DE TIPAZA:\nNombre d'habitants:" + x[1] + "\nNombre de personne atteintes de covid: " + x[
                0] + "\nNombre d'hopitaux: " + x[2] + "\nNombre de medecins: " + x[3])
        self.msg.show()
        print("fin")

    def f43(self):

        print("debut")
        wsjdid.sauvegarde()
        graph = wsjdid.default_world.as_rdflib_graph()
        prefixe = "prefix ns1: <http://www.w3.org/2002/07/owl#> \nprefix ns2: <file://PROJET.owl#> \nprefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \nprefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> \nprefix xml: <http://www.w3.org/XML/1998/namespace> \nprefix xsd: <http://www.w3.org/2001/XMLSchema#>\n "
        select1 = "SELECT (COUNT( ?x) AS ?nbpatteints)  \n WHERE{"
        select2 = "SELECT  (COUNT( ?z) AS ?nbhabitants) \n WHERE{"
        select3 = "SELECT (COUNT( ?w) AS ?nbhop) \n WHERE{"
        select4 = "SELECT (COUNT(?e) AS ?nbmed ) \n WHERE{"
        cmd = "OPTIONAL{?x a ns2:pCovid_grave."
        cmd1 = "?x ns2:habite_a <file://PROJET.owl#43.MILA>.}}"
        cmd11 = "OPTIONAL{?e a ns2:Medecin."
        cmd12 = "?e ns2:habite_a <file://PROJET.owl#43.MILA>.}}"
        cmd2 = "OPTIONAL{<file://PROJET.owl#43.MILA> ns2:a_pour_habitant ?z.}}"
        cmd3 = "OPTIONAL{<file://PROJET.owl#43.MILA> ns2:contient_hopital ?w}}"

        requete = prefixe + select1 + cmd + cmd1
        x = []
        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))

        requete = prefixe + select2 + cmd2

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        requete = prefixe + select3 + cmd3

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        requete = prefixe + select4 + cmd11 + cmd12

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        print(requete)
        self.msg = QtWidgets.QMessageBox()
        self.msg.setText(
            "WILAYA DE MILA:\nNombre d'habitants:" + x[1] + "\nNombre de personne atteintes de covid: " + x[
                0] + "\nNombre d'hopitaux: " + x[2] + "\nNombre de medecins: " + x[3])
        self.msg.show()
        print("fin")
    def f44(self):
        print("debut")
        wsjdid.sauvegarde()
        graph = wsjdid.default_world.as_rdflib_graph()
        prefixe = "prefix ns1: <http://www.w3.org/2002/07/owl#> \nprefix ns2: <file://PROJET.owl#> \nprefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \nprefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> \nprefix xml: <http://www.w3.org/XML/1998/namespace> \nprefix xsd: <http://www.w3.org/2001/XMLSchema#>\n "
        select1 = "SELECT (COUNT( ?x) AS ?nbpatteints)  \n WHERE{"
        select2 = "SELECT  (COUNT( ?z) AS ?nbhabitants) \n WHERE{"
        select3 = "SELECT (COUNT( ?w) AS ?nbhop) \n WHERE{"
        select4 = "SELECT (COUNT(?e) AS ?nbmed ) \n WHERE{"
        cmd = "OPTIONAL{?x a ns2:pCovid_grave."
        cmd1 = "?x ns2:habite_a <file://PROJET.owl#44.AÏNDEFLA>.}}"
        cmd11 = "OPTIONAL{?e a ns2:Medecin."
        cmd12 = "?e ns2:habite_a <file://PROJET.owl#44.AÏNDEFLA>.}}"
        cmd2 = "OPTIONAL{<file://PROJET.owl#44.AÏNDEFLA> ns2:a_pour_habitant ?z.}}"
        cmd3 = "OPTIONAL{<file://PROJET.owl#44.AÏNDEFLA> ns2:contient_hopital ?w}}"

        requete = prefixe + select1 + cmd + cmd1
        x = []
        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))

        requete = prefixe + select2 + cmd2

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        requete = prefixe + select3 + cmd3

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        requete = prefixe + select4 + cmd11 + cmd12

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        print(requete)
        self.msg = QtWidgets.QMessageBox()
        self.msg.setText(
            "WILAYA DE AÏNDEFLA:\nNombre d'habitants:" + x[1] + "\nNombre de personne atteintes de covid: " + x[
                0] + "\nNombre d'hopitaux: " + x[2] + "\nNombre de medecins: " + x[3])
        self.msg.show()
        print("fin")
    def f45(self):

        print("debut")
        wsjdid.sauvegarde()
        graph = wsjdid.default_world.as_rdflib_graph()
        prefixe = "prefix ns1: <http://www.w3.org/2002/07/owl#> \nprefix ns2: <file://PROJET.owl#> \nprefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \nprefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> \nprefix xml: <http://www.w3.org/XML/1998/namespace> \nprefix xsd: <http://www.w3.org/2001/XMLSchema#>\n "
        select1 = "SELECT (COUNT( ?x) AS ?nbpatteints)  \n WHERE{"
        select2 = "SELECT  (COUNT( ?z) AS ?nbhabitants) \n WHERE{"
        select3 = "SELECT (COUNT( ?w) AS ?nbhop) \n WHERE{"
        select4 = "SELECT (COUNT(?e) AS ?nbmed ) \n WHERE{"
        cmd = "OPTIONAL{?x a ns2:pCovid_grave."
        cmd1 = "?x ns2:habite_a <file://PROJET.owl#45.NÂAMA>.}}"
        cmd11 = "OPTIONAL{?e a ns2:Medecin."
        cmd12 = "?e ns2:habite_a <file://PROJET.owl#45.NÂAMA>.}}"
        cmd2 = "OPTIONAL{<file://PROJET.owl#45.NÂAMA> ns2:a_pour_habitant ?z.}}"
        cmd3 = "OPTIONAL{<file://PROJET.owl#45.NÂAMA> ns2:contient_hopital ?w}}"

        requete = prefixe + select1 + cmd + cmd1
        x = []
        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))

        requete = prefixe + select2 + cmd2

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        requete = prefixe + select3 + cmd3

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        requete = prefixe + select4 + cmd11 + cmd12

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        print(requete)
        self.msg = QtWidgets.QMessageBox()
        self.msg.setText(
            "WILAYA DE NÂAMA:\nNombre d'habitants:" + x[1] + "\nNombre de personne atteintes de covid: " + x[
                0] + "\nNombre d'hopitaux: " + x[2] + "\nNombre de medecins: " + x[3])
        self.msg.show()
        print("fin")
    def f46(self):
        print("debut")
        wsjdid.sauvegarde()
        graph = wsjdid.default_world.as_rdflib_graph()
        prefixe = "prefix ns1: <http://www.w3.org/2002/07/owl#> \nprefix ns2: <file://PROJET.owl#> \nprefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \nprefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> \nprefix xml: <http://www.w3.org/XML/1998/namespace> \nprefix xsd: <http://www.w3.org/2001/XMLSchema#>\n "
        select1 = "SELECT (COUNT( ?x) AS ?nbpatteints)  \n WHERE{"
        select2 = "SELECT  (COUNT( ?z) AS ?nbhabitants) \n WHERE{"
        select3 = "SELECT (COUNT( ?w) AS ?nbhop) \n WHERE{"
        select4 = "SELECT (COUNT(?e) AS ?nbmed ) \n WHERE{"
        cmd = "OPTIONAL{?x a ns2:pCovid_grave."
        cmd1 = "?x ns2:habite_a <file://PROJET.owl#46.AÏNTEMOUCHENT>.}}"
        cmd11 = "OPTIONAL{?e a ns2:Medecin."
        cmd12 = "?e ns2:habite_a <file://PROJET.owl#46.AÏNTEMOUCHENT>.}}"
        cmd2 = "OPTIONAL{<file://PROJET.owl#46.AÏNTEMOUCHENT> ns2:a_pour_habitant ?z.}}"
        cmd3 = "OPTIONAL{<file://PROJET.owl#46.AÏNTEMOUCHENT> ns2:contient_hopital ?w}}"

        requete = prefixe + select1 + cmd + cmd1
        x = []
        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))

        requete = prefixe + select2 + cmd2

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        requete = prefixe + select3 + cmd3

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        requete = prefixe + select4 + cmd11 + cmd12

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        print(requete)
        self.msg = QtWidgets.QMessageBox()
        self.msg.setText(
            "WILAYA DE AÏNTEMOUCHENT:\nNombre d'habitants:" + x[1] + "\nNombre de personne atteintes de covid: " + x[
                0] + "\nNombre d'hopitaux: " + x[2] + "\nNombre de medecins: " + x[3])
        self.msg.show()
        print("fin")
    def f47(self):
        print("debut")
        wsjdid.sauvegarde()
        graph = wsjdid.default_world.as_rdflib_graph()
        prefixe = "prefix ns1: <http://www.w3.org/2002/07/owl#> \nprefix ns2: <file://PROJET.owl#> \nprefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \nprefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> \nprefix xml: <http://www.w3.org/XML/1998/namespace> \nprefix xsd: <http://www.w3.org/2001/XMLSchema#>\n "
        select1 = "SELECT (COUNT( ?x) AS ?nbpatteints)  \n WHERE{"
        select2 = "SELECT  (COUNT( ?z) AS ?nbhabitants) \n WHERE{"
        select3 = "SELECT (COUNT( ?w) AS ?nbhop) \n WHERE{"
        select4 = "SELECT (COUNT(?e) AS ?nbmed ) \n WHERE{"
        cmd = "OPTIONAL{?x a ns2:pCovid_grave."
        cmd1 = "?x ns2:habite_a <file://PROJET.owl#47.GHARDAÏA>.}}"
        cmd11 = "OPTIONAL{?e a ns2:Medecin."
        cmd12 = "?e ns2:habite_a <file://PROJET.owl#47.GHARDAÏA>.}}"
        cmd2 = "OPTIONAL{<file://PROJET.owl#47.GHARDAÏA> ns2:a_pour_habitant ?z.}}"
        cmd3 = "OPTIONAL{<file://PROJET.owl#47.GHARDAÏA> ns2:contient_hopital ?w}}"

        requete = prefixe + select1 + cmd + cmd1
        x = []
        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))

        requete = prefixe + select2 + cmd2

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        requete = prefixe + select3 + cmd3

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        requete = prefixe + select4 + cmd11 + cmd12

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        print(requete)
        self.msg = QtWidgets.QMessageBox()
        self.msg.setText(
            "WILAYA DE GHARDAÏA:\nNombre d'habitants:" + x[1] + "\nNombre de personne atteintes de covid: " + x[
                0] + "\nNombre d'hopitaux: " + x[2] + "\nNombre de medecins: " + x[3])
        self.msg.show()
        print("fin")

    def f48(self):
        print("debut")
        wsjdid.sauvegarde()
        graph = wsjdid.default_world.as_rdflib_graph()
        prefixe = "prefix ns1: <http://www.w3.org/2002/07/owl#> \nprefix ns2: <file://PROJET.owl#> \nprefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \nprefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> \nprefix xml: <http://www.w3.org/XML/1998/namespace> \nprefix xsd: <http://www.w3.org/2001/XMLSchema#>\n "
        select1 = "SELECT (COUNT( ?x) AS ?nbpatteints)  \n WHERE{"
        select2 = "SELECT  (COUNT( ?z) AS ?nbhabitants) \n WHERE{"
        select3 = "SELECT (COUNT( ?w) AS ?nbhop) \n WHERE{"
        select4 = "SELECT (COUNT(?e) AS ?nbmed ) \n WHERE{"
        cmd = "OPTIONAL{?x a ns2:pCovid_grave."
        cmd1 = "?x ns2:habite_a <file://PROJET.owl#48.RELIZANE>.}}"
        cmd11 = "OPTIONAL{?e a ns2:Medecin."
        cmd12 = "?e ns2:habite_a <file://PROJET.owl#48.RELIZANE>.}}"
        cmd2 = "OPTIONAL{<file://PROJET.owl#48.RELIZANE> ns2:a_pour_habitant ?z.}}"
        cmd3 = "OPTIONAL{<file://PROJET.owl#48.RELIZANE> ns2:contient_hopital ?w}}"

        requete = prefixe + select1 + cmd + cmd1
        x = []
        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))

        requete = prefixe + select2 + cmd2

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        requete = prefixe + select3 + cmd3

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        requete = prefixe + select4 + cmd11 + cmd12

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        print(requete)
        self.msg = QtWidgets.QMessageBox()
        self.msg.setText(
            "WILAYA DE RELIZANE:\nNombre d'habitants:" + x[1] + "\nNombre de personne atteintes de covid: " + x[
                0] + "\nNombre d'hopitaux: " + x[2] + "\nNombre de medecins: " + x[3])
        self.msg.show()
        print("fin")
    def f49(self):
        print("debut")
        wsjdid.sauvegarde()
        graph = wsjdid.default_world.as_rdflib_graph()
        prefixe = "prefix ns1: <http://www.w3.org/2002/07/owl#> \nprefix ns2: <file://PROJET.owl#> \nprefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \nprefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> \nprefix xml: <http://www.w3.org/XML/1998/namespace> \nprefix xsd: <http://www.w3.org/2001/XMLSchema#>\n "
        select1 = "SELECT (COUNT( ?x) AS ?nbpatteints)  \n WHERE{"
        select2 = "SELECT  (COUNT( ?z) AS ?nbhabitants) \n WHERE{"
        select3 = "SELECT (COUNT( ?w) AS ?nbhop) \n WHERE{"
        select4 = "SELECT (COUNT(?e) AS ?nbmed ) \n WHERE{"
        cmd = "OPTIONAL{?x a ns2:pCovid_grave."
        cmd1 = "?x ns2:habite_a <file://PROJET.owl#49.BORDJBADJIMOKHTAR>.}}"
        cmd11 = "OPTIONAL{?e a ns2:Medecin."
        cmd12 = "?e ns2:habite_a <file://PROJET.owl#49.BORDJBADJIMOKHTAR>.}}"
        cmd2 = "OPTIONAL{<file://PROJET.owl#49.BORDJBADJIMOKHTAR> ns2:a_pour_habitant ?z.}}"
        cmd3 = "OPTIONAL{<file://PROJET.owl#49.BORDJBADJIMOKHTAR> ns2:contient_hopital ?w}}"

        requete = prefixe + select1 + cmd + cmd1
        x = []
        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))

        requete = prefixe + select2 + cmd2

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        requete = prefixe + select3 + cmd3

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        requete = prefixe + select4 + cmd11 + cmd12

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        print(requete)
        self.msg = QtWidgets.QMessageBox()
        self.msg.setText(
            "WILAYA DE BORDJBADJIMOKHTAR:\nNombre d'habitants:" + x[1] + "\nNombre de personne atteintes de covid: " + x[
                0] + "\nNombre d'hopitaux: " + x[2] + "\nNombre de medecins: " + x[3])
        self.msg.show()
        print("fin")
    def f50(self):
        print("debut")
        wsjdid.sauvegarde()
        graph = wsjdid.default_world.as_rdflib_graph()
        prefixe = "prefix ns1: <http://www.w3.org/2002/07/owl#> \nprefix ns2: <file://PROJET.owl#> \nprefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \nprefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> \nprefix xml: <http://www.w3.org/XML/1998/namespace> \nprefix xsd: <http://www.w3.org/2001/XMLSchema#>\n "
        select1 = "SELECT (COUNT( ?x) AS ?nbpatteints)  \n WHERE{"
        select2 = "SELECT  (COUNT( ?z) AS ?nbhabitants) \n WHERE{"
        select3 = "SELECT (COUNT( ?w) AS ?nbhop) \n WHERE{"
        select4 = "SELECT (COUNT(?e) AS ?nbmed ) \n WHERE{"
        cmd = "OPTIONAL{?x a ns2:pCovid_grave."
        cmd1 = "?x ns2:habite_a <file://PROJET.owl#50.INSALAH>.}}"
        cmd11 = "OPTIONAL{?e a ns2:Medecin."
        cmd12 = "?e ns2:habite_a <file://PROJET.owl#50.INSALAH>.}}"
        cmd2 = "OPTIONAL{<file://PROJET.owl#50.INSALAH> ns2:a_pour_habitant ?z.}}"
        cmd3 = "OPTIONAL{<file://PROJET.owl#50.INSALAH> ns2:contient_hopital ?w}}"

        requete = prefixe + select1 + cmd + cmd1
        x = []
        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))

        requete = prefixe + select2 + cmd2

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        requete = prefixe + select3 + cmd3

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        requete = prefixe + select4 + cmd11 + cmd12

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        print(requete)
        self.msg = QtWidgets.QMessageBox()
        self.msg.setText(
            "WILAYA DE INSALAH:\nNombre d'habitants:" + x[1] + "\nNombre de personne atteintes de covid: " + x[
                0] + "\nNombre d'hopitaux: " + x[2] + "\nNombre de medecins: " + x[3])
        self.msg.show()
        print("fin")

    def f51(self):
        print("debut")
        wsjdid.sauvegarde()
        graph = wsjdid.default_world.as_rdflib_graph()
        prefixe = "prefix ns1: <http://www.w3.org/2002/07/owl#> \nprefix ns2: <file://PROJET.owl#> \nprefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \nprefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> \nprefix xml: <http://www.w3.org/XML/1998/namespace> \nprefix xsd: <http://www.w3.org/2001/XMLSchema#>\n "
        select1 = "SELECT (COUNT( ?x) AS ?nbpatteints)  \n WHERE{"
        select2 = "SELECT  (COUNT( ?z) AS ?nbhabitants) \n WHERE{"
        select3 = "SELECT (COUNT( ?w) AS ?nbhop) \n WHERE{"
        select4 = "SELECT (COUNT(?e) AS ?nbmed ) \n WHERE{"
        cmd = "OPTIONAL{?x a ns2:pCovid_grave."
        cmd1 = "?x ns2:habite_a <file://PROJET.owl#51.DJANET>.}}"
        cmd11 = "OPTIONAL{?e a ns2:Medecin."
        cmd12 = "?e ns2:habite_a <file://PROJET.owl#51.DJANET>.}}"
        cmd2 = "OPTIONAL{<file://PROJET.owl#51.DJANET> ns2:a_pour_habitant ?z.}}"
        cmd3 = "OPTIONAL{<file://PROJET.owl#51.DJANET> ns2:contient_hopital ?w}}"

        requete = prefixe + select1 + cmd + cmd1
        x = []
        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))

        requete = prefixe + select2 + cmd2

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        requete = prefixe + select3 + cmd3

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        requete = prefixe + select4 + cmd11 + cmd12

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        print(requete)
        self.msg = QtWidgets.QMessageBox()
        self.msg.setText(
            "WILAYA DE DJANET:\nNombre d'habitants:" + x[1] + "\nNombre de personne atteintes de covid: " + x[
                0] + "\nNombre d'hopitaux: " + x[2] + "\nNombre de medecins: " + x[3])
        self.msg.show()
        print("fin")
    def f52(self):
            print("debut")
            wsjdid.sauvegarde()
            graph = wsjdid.default_world.as_rdflib_graph()
            prefixe = "prefix ns1: <http://www.w3.org/2002/07/owl#> \nprefix ns2: <file://PROJET.owl#> \nprefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \nprefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> \nprefix xml: <http://www.w3.org/XML/1998/namespace> \nprefix xsd: <http://www.w3.org/2001/XMLSchema#>\n "
            select1 = "SELECT (COUNT( ?x) AS ?nbpatteints)  \n WHERE{"
            select2 = "SELECT  (COUNT( ?z) AS ?nbhabitants) \n WHERE{"
            select3 = "SELECT (COUNT( ?w) AS ?nbhop) \n WHERE{"
            select4 = "SELECT (COUNT(?e) AS ?nbmed ) \n WHERE{"
            cmd = "OPTIONAL{?x a ns2:pCovid_grave."
            cmd1 = "?x ns2:habite_a <file://PROJET.owl#52.INGUEZZEM>.}}"
            cmd11 = "OPTIONAL{?e a ns2:Medecin."
            cmd12 = "?e ns2:habite_a <file://PROJET.owl#52.INGUEZZEM>.}}"
            cmd2 = "OPTIONAL{<file://PROJET.owl#52.INGUEZZEM> ns2:a_pour_habitant ?z.}}"
            cmd3 = "OPTIONAL{<file://PROJET.owl#52.INGUEZZEM> ns2:contient_hopital ?w}}"

            requete = prefixe + select1 + cmd + cmd1
            x = []
            res = graph.query(requete)

            for i in res:
                x.append(str(i[0]))

            requete = prefixe + select2 + cmd2

            res = graph.query(requete)

            for i in res:
                x.append(str(i[0]))
            requete = prefixe + select3 + cmd3

            res = graph.query(requete)

            for i in res:
                x.append(str(i[0]))
            requete = prefixe + select4 + cmd11 + cmd12

            res = graph.query(requete)

            for i in res:
                x.append(str(i[0]))
            print(requete)
            self.msg = QtWidgets.QMessageBox()
            self.msg.setText(
                "WILAYA DE INGUEZZEM:\nNombre d'habitants:" + x[1] + "\nNombre de personne atteintes de covid: " + x[
                    0] + "\nNombre d'hopitaux: " + x[2] + "\nNombre de medecins: " + x[3])
            self.msg.show()
            print("fin")
    def f53(self):
        print("debut")
        wsjdid.sauvegarde()
        graph = wsjdid.default_world.as_rdflib_graph()
        prefixe = "prefix ns1: <http://www.w3.org/2002/07/owl#> \nprefix ns2: <file://PROJET.owl#> \nprefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \nprefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> \nprefix xml: <http://www.w3.org/XML/1998/namespace> \nprefix xsd: <http://www.w3.org/2001/XMLSchema#>\n "
        select1 = "SELECT (COUNT( ?x) AS ?nbpatteints)  \n WHERE{"
        select2 = "SELECT  (COUNT( ?z) AS ?nbhabitants) \n WHERE{"
        select3 = "SELECT (COUNT( ?w) AS ?nbhop) \n WHERE{"
        select4 = "SELECT (COUNT(?e) AS ?nbmed ) \n WHERE{"
        cmd = "OPTIONAL{?x a ns2:pCovid_grave."
        cmd1 = "?x ns2:habite_a <file://PROJET.owl#53.ELMGHAIER>.}}"
        cmd11 = "OPTIONAL{?e a ns2:Medecin."
        cmd12 = "?e ns2:habite_a <file://PROJET.owl#53.ELMGHAIER>.}}"
        cmd2 = "OPTIONAL{<file://PROJET.owl#53.ELMGHAIER> ns2:a_pour_habitant ?z.}}"
        cmd3 = "OPTIONAL{<file://PROJET.owl#53.ELMGHAIER> ns2:contient_hopital ?w}}"

        requete = prefixe + select1 + cmd + cmd1
        x = []
        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))

        requete = prefixe + select2 + cmd2

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        requete = prefixe + select3 + cmd3

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        requete = prefixe + select4 + cmd11 + cmd12

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        print(requete)
        self.msg = QtWidgets.QMessageBox()
        self.msg.setText(
            "WILAYA DE ELMGHAIER:\nNombre d'habitants:" + x[1] + "\nNombre de personne atteintes de covid: " + x[
                0] + "\nNombre d'hopitaux: " + x[2] + "\nNombre de medecins: " + x[3])
        self.msg.show()
        print("fin")
    def f54(self):
        print("debut")
        wsjdid.sauvegarde()
        graph = wsjdid.default_world.as_rdflib_graph()
        prefixe = "prefix ns1: <http://www.w3.org/2002/07/owl#> \nprefix ns2: <file://PROJET.owl#> \nprefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \nprefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> \nprefix xml: <http://www.w3.org/XML/1998/namespace> \nprefix xsd: <http://www.w3.org/2001/XMLSchema#>\n "
        select1 = "SELECT (COUNT( ?x) AS ?nbpatteints)  \n WHERE{"
        select2 = "SELECT  (COUNT( ?z) AS ?nbhabitants) \n WHERE{"
        select3 = "SELECT (COUNT( ?w) AS ?nbhop) \n WHERE{"
        select4 = "SELECT (COUNT(?e) AS ?nbmed ) \n WHERE{"
        cmd = "OPTIONAL{?x a ns2:pCovid_grave."
        cmd1 = "?x ns2:habite_a <file://PROJET.owl#54.TOUGGOURT>.}}"
        cmd11 = "OPTIONAL{?e a ns2:Medecin."
        cmd12 = "?e ns2:habite_a <file://PROJET.owl#54.TOUGGOURT>.}}"
        cmd2 = "OPTIONAL{<file://PROJET.owl#54.TOUGGOURT> ns2:a_pour_habitant ?z.}}"
        cmd3 = "OPTIONAL{<file://PROJET.owl#54.TOUGGOURT> ns2:contient_hopital ?w}}"

        requete = prefixe + select1 + cmd + cmd1
        x = []
        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        requete = prefixe + select2 + cmd2

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        requete = prefixe + select3 + cmd3

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        requete = prefixe + select4 + cmd11 + cmd12

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        print(requete)
        self.msg = QtWidgets.QMessageBox()
        self.msg.setText(
            "WILAYA DE TOUGGOURT:\nNombre d'habitants:" + x[1] + "\nNombre de personne atteintes de covid: " + x[
                0] + "\nNombre d'hopitaux: " + x[2] + "\nNombre de medecins: " + x[3])
        self.msg.show()
        print("fin")
    def f55(self):
        print("debut")
        wsjdid.sauvegarde()
        graph = wsjdid.default_world.as_rdflib_graph()
        prefixe = "prefix ns1: <http://www.w3.org/2002/07/owl#> \nprefix ns2: <file://PROJET.owl#> \nprefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \nprefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> \nprefix xml: <http://www.w3.org/XML/1998/namespace> \nprefix xsd: <http://www.w3.org/2001/XMLSchema#>\n "
        select1 = "SELECT (COUNT( ?x) AS ?nbpatteints)  \n WHERE{"
        select2 = "SELECT  (COUNT( ?z) AS ?nbhabitants) \n WHERE{"
        select3 = "SELECT (COUNT( ?w) AS ?nbhop) \n WHERE{"
        select4 = "SELECT (COUNT(?e) AS ?nbmed ) \n WHERE{"
        cmd = "OPTIONAL{?x a ns2:pCovid_grave."
        cmd1 = "?x ns2:habite_a <file://PROJET.owl#55.BÉNIABBES>.}}"
        cmd11 = "OPTIONAL{?e a ns2:Medecin."
        cmd12 = "?e ns2:habite_a <file://PROJET.owl#55.BÉNIABBES>.}}"
        cmd2 = "OPTIONAL{<file://PROJET.owl#55.BÉNIABBES> ns2:a_pour_habitant ?z.}}"
        cmd3 = "OPTIONAL{<file://PROJET.owl#55.BÉNIABBES> ns2:contient_hopital ?w}}"

        requete = prefixe + select1 + cmd + cmd1
        x = []
        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))

        requete = prefixe + select2 + cmd2

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        requete = prefixe + select3 + cmd3

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        requete = prefixe + select4 + cmd11 + cmd12

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        print(requete)
        self.msg = QtWidgets.QMessageBox()
        self.msg.setText(
            "WILAYA DE BÉNIABBES:\nNombre d'habitants:" + x[1] + "\nNombre de personne atteintes de covid: " + x[
                0] + "\nNombre d'hopitaux: " + x[2] + "\nNombre de medecins: " + x[3])
        self.msg.show()
        print("fin")

    def f56(self):


        print("debut")
        wsjdid.sauvegarde()
        graph = wsjdid.default_world.as_rdflib_graph()
        prefixe = "prefix ns1: <http://www.w3.org/2002/07/owl#> \nprefix ns2: <file://PROJET.owl#> \nprefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \nprefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> \nprefix xml: <http://www.w3.org/XML/1998/namespace> \nprefix xsd: <http://www.w3.org/2001/XMLSchema#>\n "
        select1 = "SELECT (COUNT( ?x) AS ?nbpatteints)  \n WHERE{"
        select2 = "SELECT  (COUNT( ?z) AS ?nbhabitants) \n WHERE{"
        select3 = "SELECT (COUNT( ?w) AS ?nbhop) \n WHERE{"
        select4 = "SELECT (COUNT(?e) AS ?nbmed ) \n WHERE{"
        cmd = "OPTIONAL{?x a ns2:pCovid_grave."
        cmd1 = "?x ns2:habite_a <file://PROJET.owl#56.TIMIMOUNE>.}}"
        cmd11 = "OPTIONAL{?e a ns2:Medecin."
        cmd12 = "?e ns2:habite_a <file://PROJET.owl#56.TIMIMOUNE>.}}"
        cmd2 = "OPTIONAL{<file://PROJET.owl#56.TIMIMOUNE> ns2:a_pour_habitant ?z.}}"
        cmd3 = "OPTIONAL{<file://PROJET.owl#56.TIMIMOUNE> ns2:contient_hopital ?w}}"

        requete = prefixe + select1 + cmd + cmd1
        x = []
        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))

        requete = prefixe + select2 + cmd2

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        requete = prefixe + select3 + cmd3

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        requete = prefixe + select4 + cmd11 + cmd12

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        print(requete)
        self.msg = QtWidgets.QMessageBox()
        self.msg.setText(
            "WILAYA DE TIMIMOUNE:\nNombre d'habitants:" + x[1] + "\nNombre de personne atteintes de covid: " + x[
                0] + "\nNombre d'hopitaux: " + x[2] + "\nNombre de medecins: " + x[3])
        self.msg.show()
        print("fin")

    def f57(self):
        print("debut")
        wsjdid.sauvegarde()
        graph = wsjdid.default_world.as_rdflib_graph()
        prefixe = "prefix ns1: <http://www.w3.org/2002/07/owl#> \nprefix ns2: <file://PROJET.owl#> \nprefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \nprefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> \nprefix xml: <http://www.w3.org/XML/1998/namespace> \nprefix xsd: <http://www.w3.org/2001/XMLSchema#>\n "
        select1 = "SELECT (COUNT( ?x) AS ?nbpatteints)  \n WHERE{"
        select2 = "SELECT  (COUNT( ?z) AS ?nbhabitants) \n WHERE{"
        select3 = "SELECT (COUNT( ?w) AS ?nbhop) \n WHERE{"
        select4 = "SELECT (COUNT(?e) AS ?nbmed ) \n WHERE{"
        cmd = "OPTIONAL{?x a ns2:pCovid_grave."
        cmd1 = "?x ns2:habite_a <file://PROJET.owl#57.OULDDJELEL>.}}"
        cmd11 = "OPTIONAL{?e a ns2:Medecin."
        cmd12 = "?e ns2:habite_a <file://PROJET.owl#57.OULDDJELEL>.}}"
        cmd2 = "OPTIONAL{<file://PROJET.owl#57.OULDDJELEL> ns2:a_pour_habitant ?z.}}"
        cmd3 = "OPTIONAL{<file://PROJET.owl#57.OULDDJELEL> ns2:contient_hopital ?w}}"

        requete = prefixe + select1 + cmd + cmd1
        x = []
        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))

        requete = prefixe + select2 + cmd2

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        requete = prefixe + select3 + cmd3

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        requete = prefixe + select4 + cmd11 + cmd12

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        print(requete)
        self.msg = QtWidgets.QMessageBox()
        self.msg.setText(
            "WILAYA DE OULDDJELEL:\nNombre d'habitants:" + x[1] + "\nNombre de personne atteintes de covid: " + x[
                0] + "\nNombre d'hopitaux: " + x[2] + "\nNombre de medecins: " + x[3])
        self.msg.show()
        print("fin")
    def f58(self):
        print("debut")
        wsjdid.sauvegarde()
        graph = wsjdid.default_world.as_rdflib_graph()
        prefixe = "prefix ns1: <http://www.w3.org/2002/07/owl#> \nprefix ns2: <file://PROJET.owl#> \nprefix rdf: <http://www.w3.org/1999/02/22-rdf-syntax-ns#> \nprefix rdfs: <http://www.w3.org/2000/01/rdf-schema#> \nprefix xml: <http://www.w3.org/XML/1998/namespace> \nprefix xsd: <http://www.w3.org/2001/XMLSchema#>\n "
        select1 = "SELECT (COUNT( ?x) AS ?nbpatteints)  \n WHERE{"
        select2 = "SELECT  (COUNT( ?z) AS ?nbhabitants) \n WHERE{"
        select3 = "SELECT (COUNT( ?w) AS ?nbhop) \n WHERE{"
        select4 = "SELECT (COUNT(?e) AS ?nbmed ) \n WHERE{"
        cmd = "OPTIONAL{?x a ns2:pCovid_grave."
        cmd1 = "?x ns2:habite_a <file://PROJET.owl#58.ELMENIA>.}}"
        cmd11 = "OPTIONAL{?e a ns2:Medecin."
        cmd12 = "?e ns2:habite_a <file://PROJET.owl#58.ELMENIA>.}}"
        cmd2 = "OPTIONAL{<file://PROJET.owl#58.ELMENIA> ns2:a_pour_habitant ?z.}}"
        cmd3 = "OPTIONAL{<file://PROJET.owl#58.ELMENIA> ns2:contient_hopital ?w}}"

        requete = prefixe + select1 + cmd + cmd1
        x = []
        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))

        requete = prefixe + select2 + cmd2

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        requete = prefixe + select3 + cmd3

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        requete = prefixe + select4 + cmd11 + cmd12

        res = graph.query(requete)

        for i in res:
            x.append(str(i[0]))
        print(requete)
        self.msg = QtWidgets.QMessageBox()
        self.msg.setText(
            "WILAYA DE ELMENIA:\nNombre d'habitants:" + x[1] + "\nNombre de personne atteintes de covid: " + x[
                0] + "\nNombre d'hopitaux: " + x[2] + "\nNombre de medecins: " + x[3])
        self.msg.show()
        print("fin")


