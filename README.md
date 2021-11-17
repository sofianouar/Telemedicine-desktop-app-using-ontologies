# A telemedicine desktop app using RDF and ontologies.
This semantic ontology desktop app was developed to help connecting people and doctors during the pandemic of COVID-19. 
The user could rather do an online covid test (could be improved) and receive an orientation at the end, or choose to consult a doctor by selecting their disease. 
Pregnant women are also taken in consideration.
Doctors can register and create an account to manage the appointments.
The app gives also the statistics of covid cases per region (the project conerns the state of Algeria and its wilayas) and is updated in realtime.
For those who are familiar with ontologies, a sparql menu is made at disposition for any request.
For more details about the project, check the report file : "RAPPORT PROJET WS 2020.pdf"
WE developed the ontology used from scratch with RDF model using python and we visualized it in protege software.

As we lack knowledge in the medicine domain, the results of the covid test may not be as precise as possible. 
We were limited with time while implementing the project for the university, so we could't implement all the features we wanted to, such as : QRcode for a rendez-vous, a better ways to communicate with doctors (a dedicated message area as or redirection to google email) + scheduling consultations via video calls.

# About the project files
aide.txt : a file describing the ontology structure
H.xlsx : contains mostly all the name of hospitals of Algeria
Medecin.xlsx : contains names of the doctors connected (have already registered) to the app 
Projet.owl / Projet1.owl : are files generated containing the ontology, they're to run in protege

# How to use the project
You should as well dispose of any version of python. 
Method 1 : please check PROJECT CODE WS>App.py or download at : https://drive.google.com/file/d/1AN6UzI5df6FdnMpphOw2unhlyDWj9pqH/view?usp=sharing
    Run the Ikovid shortcut and don't forget to put it at the file 'executabale app' some ressources are needed.
    To visualize the ontology in protege :
        1-install protege software via https://protege.stanford.edu/
        2-open the PROJET.owl file generated in the software.
        
Method 2 : for the source code download "code version" and run "scriptLASTfinal"

In the displayed interface you can navigate and explore the app.

# Credits
My teammate AISSI Med Salim saissi1701@gmail.com

# More information
For further information, suggestion or reuse of code, please email : soffianouar@gmail.com / saissi1701@gmail.com

//made on july 2020
 
