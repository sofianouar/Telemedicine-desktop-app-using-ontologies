from owlready2 import *
import pandas as pd
import rdflib
import re
import os

if os.path.exists("file_back3.sqlite3"):
  os.remove("file_back3.sqlite3")

if not os.path.exists("PROJET.owl"):
 X=open("PROJET.owl","w")
 X.close()


default_world.set_backend(filename="file_back3.sqlite3", exclusive=False)
ontologie = get_ontology("file://PROJET.owl").load() #https://urlinvente/WSproject1

with ontologie:
    class Symptomes(Thing): pass
    class SymptomesGrave(Symptomes):  pass
    class Personne(Thing): pass
    class Patient(Personne): pass
    class Sexe(DataProperty, FunctionalProperty):
        domain = [Personne]
        range = [str]


    class Homme(Patient):
        equivalent_to = [Patient & Sexe.value('Homme')]


    class Femme(Patient):
        equivalent_to = [Patient & Sexe.value('Femme')]


    class FemmeEnceinte(Femme):
        pass


    AllDisjoint([Homme, Femme])


    class Nom(DataProperty, FunctionalProperty):
        domain = [Personne]
        range = [str]


    class Prenom(DataProperty, FunctionalProperty):
        domain = [Personne]
        range = [str]


    class Age(DataProperty, FunctionalProperty):
        domain = [Personne]
        range = [int]


    class NumTel(DataProperty, FunctionalProperty):
        domain = [Personne]
        range = [int]


    class jrsSympt(DataProperty, FunctionalProperty):
        domain = [Personne]
        range = [str]
    class obesite(DataProperty, FunctionalProperty):
        domain = [Personne]
        range = [str]



    class MaladieChroniques(Thing):
        pass


    class typemaladie(DataProperty, FunctionalProperty):
        domain = [MaladieChroniques]
        range = [str]


    class Traitement(Thing):
        pass


    class a_Pour_Maladies(Patient >> MaladieChroniques):
        pass


    class MaladeChronique(Patient):
        equivalent_to = [Patient & a_Pour_Maladies.some(MaladieChroniques)]


    class a_Symptome(Patient >> Symptomes):
        pass


    class SymptomesFrequents(Symptomes):
        pass



    class pCovid_grave(Patient):

        equivalent_to = [(Patient & a_Symptome.min(1, SymptomesGrave))
                        |(a_Symptome.min(3, SymptomesFrequents) & Age.min(57))
                         |(a_Symptome.min(3,SymptomesFrequents) & MaladeChronique)
                         |(a_Symptome.min(4,SymptomesFrequents) & jrsSympt.value("+8 jrs"))
                         |(a_Symptome.min(4, SymptomesFrequents) & obesite.value("oui"))
                         |(a_Symptome.min(4,SymptomesFrequents) & FemmeEnceinte)
                         ]




        #class pCovid_Positif(Personne):
      #  equivalent_to = [(Personne & a_Symptome.some(Symptomes) & a_Symptome.min(3, SymptomesFrequents)&jrsSympt.value("4-8 jrs"))
     #                    |(Personne &a_Symptome.min(5,SymptomesFrequents) & jrsSympt.value("1-3 jrs"))]



    class pCovid_Depistage(Patient):

        equivalent_to = [(Patient  & a_Symptome.min(3, SymptomesFrequents)
                        & jrsSympt.value("4-8 jrs" or "+8 jrs"))|(Patient  & a_Symptome.min(4, SymptomesFrequents))
                         ]


    class affecte(MaladieChroniques >> Patient):
        inverse_property = a_Pour_Maladies


    class prend_traitement(Patient >> Traitement):
        pass


    class personne_atteinte(Symptomes >> Patient):
        inverse_property = a_Symptome


    class Medecin(Personne):
        pass


    class NomMed(DataProperty, FunctionalProperty):
        domain = [Medecin]
        range = [str]


    class specialité(DataProperty, FunctionalProperty):
        domain = [Medecin]
        range = [str]
    class domaine(DataProperty, FunctionalProperty):
        domain= [Medecin]
        range= [str]

    class adressemed(DataProperty, FunctionalProperty):
        domain = [Medecin]
        range = [str]


    class numtelmed(DataProperty, FunctionalProperty):
        domain = [Medecin]
        range = [int]


    class Emplacement(Thing):
        pass


    class Wilaya(Emplacement):
        pass


    # class Commune(Emplacement): pass



    class habite_a(Personne >> Wilaya):
        pass
    class mdp(DataProperty, FunctionalProperty):
        domain=[Medecin]
        range=[str]

    class a_pour_habitant(Wilaya >> Personne):
        inverse_property = habite_a
    class WilayaAtteinte(Wilaya):
        equivalent_to =[Wilaya & a_pour_habitant.some(pCovid_grave)]
    class a_pris_rdv(Patient >> Medecin):
        pass
    class est_soliciter_par(Medecin >> Patient):
        inverse_property = a_pris_rdv

    class Consultation(Thing): pass
    class DateC(DataProperty, FunctionalProperty):
        domain=[Consultation]
        range=[str]

    class practicien(Medecin >> Consultation ): pass
    class consultant(Patient >> Consultation): pass
    class hopital (Thing):
        pass
    class se_situe(hopital >> Wilaya):
        pass
    class contient_hopital(Wilaya >> hopital):
        inverse_property =se_situe
    AllDisjoint([hopital, Personne])


def sauvegarde():
  fichier = pd.read_excel("test.xlsx", "Sheet1")
  n = fichier.shape[0]
  pourcentage = n * 0.4
  SymptomesFrequents.equivalent_to = [Symptomes & personne_atteinte.min(int(pourcentage), Personne)]
  with ontologie:
    for i in range(0, n):
        coupe1 = str(fichier.loc[i, 'nom'])
        coupe1 = coupe1.replace(" ", "_")
        coupe2 = str(fichier.loc[i, 'prenom'])
        coupe2 = coupe2.replace(" ", "_")
        if (fichier.loc[i, 'femme enceinte'] == 'oui'):

            p1 = FemmeEnceinte(coupe1 + "_" + coupe2)
        else:
            p1 = Patient(coupe1 + "_" + coupe2)
        p1.Nom = fichier.loc[i, 'nom']
        p1.obesite=str(fichier.loc[i, 'soumna'])
        p1.Prenom = fichier.loc[i, 'prenom']
        p1.Age = int(fichier.loc[i, 'age'])
        p1.NumTel = int(fichier.loc[i, 'tel'])
        p1.Sexe = fichier.loc[i, 'sexe']
        if (str(fichier.loc[i, 'depuis quand avez-vous ces symptomes?']) != 'nan'):
            u = str(fichier.loc[i, 'depuis quand avez-vous ces symptomes?'])
            p1.jrsSympt = u

        x = str(fichier.loc[i, 'wilaya'])
        x = x.replace(" ", "")
        x=x.replace("-",".")
        print(x)
        w1 = Wilaya(x)
        p1.habite_a = [w1]

        if (str(fichier.loc[i, 'Maladie chronique']) != 'nan'):
            f = fichier.loc[i, 'Maladie chronique']

            M = re.findall("{.*?}", f, re.S)
            for o in M:
                x = re.search("{(.*):(.*),(traitement):(.*)}", o, re.S)
                K = x.group(2)
                K = K.split('\n')

                for w in K:

                    if (w != ""):
                        w = w.replace(" ", "_")
                        Maladie = MaladieChroniques(w)
                        p1.a_Pour_Maladies.append(Maladie)
                Maladie.typemaladie = str(x.group(1))
                T = x.group(4)
                T = T.split('\n')
                for j in T:
                    if (j != ""):
                        j = j.replace(" ", "_")
                        Traite = Traitement(j)

                        p1.prend_traitement.append(Traite)
        s = str(fichier.loc[i, 'symptomes'])
        s = s.split('|')
        shadox = []
        for z in range(0, len(s) - 1):
            b = s[z]
            b = b.replace(" ", "_")
            symp = Symptomes(b)

            shadox.append(symp)
            p1.a_Symptome.append(symp)
        if len(shadox) > 0:
            AllDifferent(shadox)
        sgrave = str(fichier.loc[i, 'Symptômes graves'])
        sgrave = sgrave.split('|')
        for sg1 in range(0, len(sgrave) - 1):
            b1 = sgrave[sg1]
            b1 = b1.replace(" ", "_")
            symptgrave = SymptomesGrave(b1)
            p1.a_Symptome.append(symptgrave)
    med = pd.read_excel("medecin.xlsx", "Sheet1")
    nm = med.shape[0]
    for t in range(0, nm):
        namme = str(med.loc[t, 'nom'])
        namme = namme.replace(" ", "_")
        xx = "Dr." + namme
        M = Medecin(xx)

        M.NomMed = namme
        sp = str(med.loc[t, 'specialité'])
        #sp = sp.replace(" ", "_")
        M.specialité = sp
        M.mdp=str(med.loc[t, "mot de passe"])
        dm=str(med.loc[t, "domaine"])
        M.domaine=dm
        ad = str(med.loc[t, 'adresse'])
        ad = ad.replace(" ", "_")
        M.adressemed = ad
        M.numtelmed = int(med.loc[t, 'tel'])
        wi = str(med.loc[t, 'wilaya'])
        wi = wi.replace(" ", "")
        wi = wi.replace("-", ".")


        wmed = Wilaya(wi)
        M.habite_a = [wmed]
    sbitar = pd.read_excel("H.xlsx", "Table 1")
    nh=sbitar.shape[0]
    for i in range(nh):
        wilayah=str(sbitar.loc[i,"Wilaya"])
        if(wilayah=="Adrar"):
            wilayah="1 - ADRAR"
        if(wilayah=="Chlef"):
            wilayah="2 - CHLEF"
        if(wilayah=="Laghouat"):
            wilayah="3 - LAGHOUAT"
        if(wilayah=="Oum El Bouaghi"):
           wilayah="4 - OUM BOUAGHI"
        if(wilayah=="Batna"):
            wilayah="5 - BATNA"
        if(wilayah=="Bejaia"):
            wilayah="6 - BEJAIA"
        if(wilayah=="Biskra"):
            wilayah="7 - BISKRA"
        if(wilayah=="Bechar"):
            wilayah="8 - BECHAR"
        if(wilayah=="Blida"):
            wilayah="9 - BLIDA"
        if(wilayah=="Bouira"):
            wilayah="10 - BOUIRA"
        if(wilayah=="Tamanrasset"):
            wilayah="11 - TAMANRASSET"
        if(wilayah=="Tebessa"):
            wilayah="12 - TEBESSA"
        if(wilayah=="Tlemcen"):
            wilayah="13 - TLEMCEN"
        if(wilayah=="Tiaret"):
            wilayah="14 - TIARET"
        if(wilayah=="Tizi Ouzou"):
            wilayah="15 - TIZI OUZOU"
        if (wilayah == "Alger"):
            wilayah="16 - ALGER"
        if (wilayah == "Djelfa"):
            wilayah="17 - DJELFA"
        if (wilayah == "Jijel"):
            wilayah="18 - JIJEL"
        if (wilayah == "Sétif"):
           wilayah="19 - SETIF"
        if (wilayah == "Saida"):
            wilayah="20 - SAIDA"
        if (wilayah == "Skikda"):
            wilayah="21 - SKIKDA"
        if (wilayah == "Sidi Bel Abbes"):
            wilayah="22 - SIDI BEL ABBES"
        if (wilayah == "Annaba"):
            wilayah="23 - ANNABA"
        if (wilayah == "Guelma"):
            wilayah="24 - GUELMA"
        if (wilayah == "Constantine"):
            wilayah="25 - CONSTANTINE"
        if (wilayah == "Médéa"):
            wilayah="26 - MEDEA"
        if (wilayah == "Mostaganem"):
            wilayah="27 - MOSTAGANEM"
        if (wilayah == "Msila"):
            wilayah="28 - M'SILA"
        if (wilayah == "Mascara"):
            wilayah="29 - MASCARA"
        if (wilayah == "Ouargla"):
            wilayah="30 - OUARGLA"
        if (wilayah == "Oran"):
            wilayah="31 - ORAN"
        if (wilayah == "El Bayadh"):
            wilayah="32 - EL BAYDH"
        if (wilayah == "Illizi"):
            wilayah="33 - ILLIZI"
        if (wilayah == "Bordj Bou Arreridj"):
            wilayah= "34 - BORDJ BOU ARRERIDJ"
        if (wilayah == "Boumerdes"):
            wilayah="35 - BOUMERDES"
        if (wilayah == "El Tarf"):
            wilayah="36 - EL TAREF"
        if (wilayah == "Tindouf"):
            wilayah="37 - TINDOUF"
        if (wilayah == "Tissemsilt"):
            wilayah="38 - TISSEMSILT"
        if (wilayah == "El Oued"):
            wilayah="39 - EL OUED"
        if (wilayah == "Khenchela"):
            wilayah="40 - KHENCHLA"
        if (wilayah == "Souk Ahras"):
            wilayah="41 - SOUK AHRASS"
        if (wilayah == "Tipaza"):
            wilayah="42 - TIPAZA"
        if (wilayah == "Mila"):
            wilayah="43 - MILA"
        if (wilayah == "Ain Defla"):
            wilayah="44 - AÏN DEFLA"
        if (wilayah == "Naama"):
           wilayah= "45 - NÂAMA"
        if (wilayah == "Ain Temouchent"):
            wilayah="46 - AÏN TEMOUCHENT"
        if (wilayah == "Ghardaia"):
            wilayah="47 - GHARDAÏA"
        if (wilayah == "Relizane"):
            wilayah="48 - RELIZANE"
        wilayah=str(wilayah)
        wilayah = wilayah.replace(" ", "")
        wilayah= wilayah.replace("-", ".")
        wiwi=Wilaya(wilayah)
        hp = str(sbitar.loc[i, "Hôpital"])
        hp=hp.replace(" ",'_')
        hp=hp.replace("'","_")
        moustachfa=hopital(hp)
        wiwi.contient_hopital.append(moustachfa)
        print(hp)
    print(nh)
    with ontologie:
     sync_reasoner_pellet(infer_property_values=True)

    ontologie.save(file="PROJET.owl", format="ntriples")
    default_world.save()
    graph = default_world.as_rdflib_graph()
    graph.serialize("PROJET1.owl", "turtle")
    print("fin exec ws")



#sauvegarde()