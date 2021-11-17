import urllib.request
import re,os
import pandas as pd
from pandas import DataFrame

def spec(ch):
    ch = ch.replace("&#233", "é")
    ch = ch.replace("&#176;", "°")
    ch = ch.replace("&#224;", "à")
    ch = ch.replace("&#39;", "'")
    ch = ch.replace("&#39;", "'")
    ch = ch.replace("&#232;", "è")
    ch = ch.replace("&#239;", "ï")
    ch=ch.replace("&#244","ô")
    ch=ch.replace(";","")
    return ch



url = "https://www.algerie-pratique.com/Medecins/Specialite?typeEntiteLibelle="
categ=["Rhumatologie","Endocrinologie","Cardiologie","Chirurgie%20Cardio%20Vasculaire","ORL","Gastro%20Enterologie","Nephrologie","Ophtalmologie","Psychiatrie","Urologie","Pneumo%20Phtisiologie","Chirurgie%20Urologique","Dermatologie","Oncologie%20Medicale","Hematologie","Gyneco%20Obstetrique","Immunologie"]
dico={}
for i in categ:
    chaine=url+i
    html = urllib.request.urlopen(chaine)
    contenu = html.read().decode("utf_8")

    liste_subst = re.findall('<a href="(.*)">', contenu)
    y=[]
    for j in  liste_subst:

        x=re.findall("(.*Medecin\d+)",j)
        if len(x)!=0:
            y.append(x[0])

    dico[i]=y
path = 'MEDECINS.xlsx'

for e in dico:
    print(e+"\n\n\n")
    z=list(dico[e])
    e=e.replace("%20"," ")
    for k in z:
        if (not os.path.exists(path)):
            fichier = pd.DataFrame(columns=['nom', 'domaine','specialité', 'adresse', 'tel', 'wilaya', 'mot de passe'])
            fichier.to_excel("MEDECINS.xlsx", index=False)
        fichier = pd.read_excel("MEDECINS.xlsx", "Sheet1")
        n = fichier.shape[0]
        chaine = "https://www.algerie-pratique.com" + k
        html = urllib.request.urlopen(chaine)
        contenu = html.read().decode("utf_8")
        nom= re.search('<title>Médecin (.*)-.*sur Algerie-Pratique.com', contenu,re.I)
        num = re.search('itemprop="telephone"> ((\d+\s*\.*)+)', contenu)
        adr = re.search('itemprop="streetAddress">(.*)<.*>', contenu)
        wilaya = re.search('itemprop="addressLocality">(.*)<.*>', contenu)
        #print(nom.group(1)+" "+num.group(1) + " " + adr.group(1) + " " + wilaya.group(1))
        name=nom.group(1)
        name=spec(name)

        fichier.loc[n,'nom']=name
        if num !=None:
            nmt= num.group(1)
            nmt=nmt.replace("."," ")
            nmt=nmt.replace(" ","")

            fichier.loc[n, 'tel'] =nmt
        else:
                fichier.loc[n, 'tel'] = 0
                print("ani hna")

        if adr!=None:
            ad=adr.group(1)
            ad=spec(ad)
            fichier.loc[n, 'adresse'] = ad
        wil=wilaya.group(1)
        wil=spec(wil)

        if str(wil)=="Aïn Defla":
            wil="44 - AÏN DEFLA"

        if str(wil)=="Aïn Témouchent":
                wil =  "46 - AÏN TEMOUCHENT"

        if str(wil)=="Alger":
                    wil = "16 - ALGER"

        if str(wil)=="Annaba":
                        wil = "23 - ANNABA"

        if str(wil)=="Batna":
                            wil = "5 - BATNA"
        if str(wil)=="Béchar":
                            wil = "8 - BECHAR"

        if str(wil)=="Béjaïa":
                            wil ="6 - BEJAIA"
        if str(wil)=="Biskra":
                            wil = "7 - BISKRA"
        if str(wil)=="Blida":
                            wil = "9 - BLIDA"

        if str(wil)=="Bordj Bou Arréridj":
                            wil = "34 - BORDJ BOU ARRERIDJ"

        if str(wil)=="Bouira":
                            wil = "10 - BOUIRA"
        if str(wil)=="Boumerdes":
                            wil =  "35 - BOUMERDES"

        if str(wil)=="Chlef":
                            wil =   "2 - CHLEF"

        if str(wil)=="Constantine":
            wil = "25 - CONSTANTINE"
        if str(wil)=="Dely Brahim":
                wil =  "16 - ALGER"
        if str(wil)=="Djelfa":
                    wil = "17 - DJELFA"

        if str(wil)=="El bayadh":
                    wil = "32 - EL BAYDH"

        if str(wil)=="El-Tarf":
                    wil = "36 - EL TAREF"
        if str(wil)=="Ghardaïa":
                    wil =  "47 - GHARDAÏA"

        if str(wil)=="Guelma":
                    wil =  "24 - GUELMA"


        if str(wil)=="Jijel":
                    wil =  "18 - JIJEL"

        if str(wil)=="Khenchela":
                    wil =   "40 - KHENCHLA"


        if str(wil)=="Mascara":
                    wil =  "29 - MASCARA"

        if str(wil)=="Medea":
                    wil =  "26 - MEDEA"


        if str(wil)=="Mostaganem":
                    wil =  "27 - MOSTAGANEM"


        if str(wil)=="M'sila":
                    wil =  "28 - M'SILA"


        if str(wil)=="Naama":
                    wil =  "45 - NÂAMA"




        if str(wil)=="Oran":
                    wil ="31 - ORAN"


        if str(wil)=="Oum El-Bouaghi":
                    wil ="4 - OUM BOUAGHI"

        if str(wil)=="Relizane":
            wil ="48 - RELIZANE"

        if str(wil)=="Saida":
            wil ="20 - SAIDA"

        if str(wil)=="Sidi Bel Abbes":
                wil =  "22 - SIDI BEL ABBES"

        if str(wil)=="Skikda":
                    wil ="21 - SKIKDA"


        if str(wil)=="Tébessa":
                    wil = "12 - TEBESSA"

        if str(wil)=="Tiaret" or str(wil)=="Tiaret ":
                        wil ="14 - TIARET"
        if str(wil)=="Tipaza":
                        wil = "42 - TIPAZA"


        if str(wil)=="Tissemsilt":
                        wil ="38 - TISSEMSILT"



        if str(wil)=="Tizi-Ouzou":
                        wil ="15 - TIZI OUZOU"

        if str(wil)=="Tlemcen":
                        wil ="13 - TLEMCEN"



        fichier.loc[n, 'wilaya'] = wil




        x=""
        fichier.loc[n, 'domaine'] = e
        if e=="Endocrinologie":
            x="maladies endocriniennes"
        if e =="Cardiologie" or e =="Chirurgie Cardio Vasculaire":
            x="Maladies cardiovasculaires"
        if e =="Hematologie":
            x="maladies du sang"
        if e =="ORL" or e == "Pneumo Phtisiologie":
            x="maladies respiratoires et ORL"
        if e =="Gastro Enterologie":
            x="maladies du système digestif"
        if e =="Nephrologie" or e == "Chirurgie Urologique" or e=="Gyneco Obstetrique":
            x="maladies rénales, génitales et urinaires"
        if e =="Ophtalmologie":
            x="maladies des yeux"
        if e =="Psychiatrie":
           x="maladies psychiatriques et psychologiques"
        if e =="Rhumatologie":
            x="maladies rhumatologiques"
        if e =="Urologie":
            x="maladies rénales, génitales et urinaires"
        if e =="Dermatologie":
            x="maladies de la peau"
        if e =="Oncologie Medicale":
            x="maladie cancéreuse"
        if e== "Immunologie":
            x="COVID-19"
        fichier.loc[n, 'specialité'] = x
        name=name.replace(" ","")
        name = name.replace(".", "")
        fichier.loc[n,'mot de passe']=str(n)+name
        fichier.to_excel("MEDECINS.xlsx", index=False)










