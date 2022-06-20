## cuando no digo nada, asume uno de la lista
import qi
import argparse
import sys
import time

def main(session):

    tts_service=session.service("ALTextToSpeech") # Permite hablar al robot
    tts_recognition_service=session.service("ALSpeechRecognition") # Reconocer sonidos en general
    memory_service=session.service("ALMemory") # Guardar en memoria los datos reconocidos

    # Wake up robot

    # Send robot to Stand Init

    #Move toward

    # Configure the speed to talk

    #tts_service.setParameter("speed",80)     # Configurar velocidad para hablar, por defecto esta en 100
    #tts_service.setParameter("defaultVoiceSpeed", 200)
    
    #Reset default speed to talk
    #tts_service.resetSpeed() # Vuelve al estado por defecto la velocidad de hablar del robot.

    #Changue the language
    tts_service.setLanguage('Spanish') # Lenguaje con el cual hablara el robot
    
    tts_recognition_service.pause(True)
    tts_recognition_service.setLanguage("Spanish") # Lenguaje con el cual reconocera las voces o sonidos.
    
    #Say Hello to user
#!------------------------------------------------------------------------------------
    tts_service.say("Hola, yo soy NAO y tu como te llamas?")
#!------------------------------------------------------------------------------------    
    #The robot talk to ask the user about her/his age

    tts_service.say("Y cuantos anios tienes?")

    
    
    vocabulary1=["cinco","seis","siete","ocho","nueve","diez","once","doce","trece","catorce","quince","dieciseis","diecisiete","dieciocho","diecinueve","veinte"]
    
    tts_recognition_service.setVocabulary(vocabulary1,False) # Falso : se refiere a que debes indicarle o hablar tal y cual es la palabra  // True : obviar palabras o frases ejemplo: <Tengo> cinco <anios> , obviara los que contengan <>
    # tts_recognition_service.setVocabulary(vocabulary) # Falso : se refiere a que debes indicarle o hablar tal y cual es la palabra  // True : obviar palabras o frases ejemplo: <Tengo> cinco <anios> , obviara los que contengan <>
    tts_recognition_service.subscribe("edad") # Genera el evento llamado edad
    memory_service.subscribeToEvent('WordRecognized',"edad","wordRecognized") # Escucha y reconoce la palabra que esta en el vocabulario.
    tts_recognition_service.pause(False)
    time.sleep(10)
    tts_recognition_service.unsubscribe("edad")  
    edad=memory_service.getData("WordRecognized")
    print("edad: %s" % edad[0])
    tts_service.say("Entiendo tienes"+str(edad[0])+"anios")
#!-------------------------------------------33[]33[]-----------------------------------------
    #The robot ask the user about her/his sex.
    tts_recognition_service.pause(True)
    tts_service.say("Dime cual es tu sexo: masculino o femenino ?")
    vocabulary2=['masculino','femenino','otro']
    tts_recognition_service.setVocabulary(vocabulary2,False)
    tts_recognition_service.subscribe("sexo")
    memory_service.subscribeToEvent('WordRecognized',"sexo","wordRecognized")
    tts_recognition_service.pause(False)
    time.sleep(10)
    tts_recognition_service.unsubscribe("sexo")
    sexo=memory_service.getData("WordRecognized")
    print("sexo: %s" %sexo[0])
    tts_service.say("Entiendo tu sexo es:" +str(sexo[0]))
#!------------------------------------------------------------------------------------
    #The robot says some symptoms to the user
    #Condicional COVID else continue
    #Start of While

    covid_sintomas=[]
    while len(covid_sintomas) < 3:
        tts_recognition_service.pause(True)
        tts_service.say("\\style=joyfull\\Entonces cuentame?\\pau=1000\\ \\style=didactic\\como te encuentras el dia de hoy?")
        tts_service.say("Te mostraremos una lista de sintomas para descartar el COVID 19")
        tts_service.say("Dime tienes algunos de estos sintomas: Tos, Dificultad para respirar, Dolores, Fatiga , Diarrea, Congestion Nasal, Nauseas, Fiebre, Vomitos ")
        vocabulary4=["tos","dificultad","respirar","dolores","fatiga","diarrea","congestion", "nasal","nauseas","fiebre","vomitos", "no"]
        tts_recognition_service.setVocabulary(vocabulary4,False) 
        tts_recognition_service.subscribe("sintoma_covid") 
        memory_service.subscribeToEvent('WordRecognized',"sintoma_covid","wordRecognized")
        tts_recognition_service.pause(False)
        time.sleep(10)
        tts_recognition_service.unsubscribe("sintoma_covid")
        sintoma_voi=memory_service.getData("WordRecognized")
        print("sintoma: %s" %sintoma_voi[0])
        sintoma_voi.append(str(covid_sintomas))        
        tts_service.say("Entiendo tu sintoma es: " + str(sintoma_voi[0]))
        if sintoma_voi[0]=='no':
            break    
        if len(covid_sintomas) == 3:
            tts_service.say("Por favor, realice la prueba del COVID 19")    

    if covid_sintomas[0] == 'no':
        tts_recognition_service.pause(True)
        tts_service.say("\\style=joyfull\\Entonces cuentame?\\pau=1000\\ \\style=didactic\\como te encuentras el dia de hoy?")
        tts_service.say("Dime tienes algunos de estos sintomas: Tos, Dificultad para respirar, Dolores, Perdida de Peso, Fatiga , Molestias Generales ")
        vocabulary3=["tos","dificultad","respirar","dolores","perdida","peso","fatiga","molestias"]
        tts_recognition_service.setVocabulary(vocabulary3,False) 
        tts_recognition_service.subscribe("sintoma") 
        memory_service.subscribeToEvent('WordRecognized',"sintoma","wordRecognized")
        tts_recognition_service.pause(False)
        time.sleep(10)
        tts_recognition_service.unsubscribe("sintoma")
        sintoma_vo=memory_service.getData("WordRecognized")
        print("sintoma: %s" %sintoma_vo[0])
        tts_service.say("Entiendo tu sintoma es: " + str(sintoma_vo[0]))
        
        sintomas=[]
        if sintoma_vo[0]=='tos':
            tts_recognition_service.pause(True)
            tts_service.say("Te mencionare otros posibles sintomas: tosiendo sangre, tos amarilla, tos cronica, tos seca, tos verdosa, tos sibilante, congestion nasal")
            vocabulary=['tosiendo sangre','tos amarilla','tos cronica','tos seca','tos verdosa','tos sibilante','congestion nasal']
            tts_recognition_service.setVocabulary(vocabulary,False)
            tts_recognition_service.subscribe("sintoma")
            memory_service.subscribeToEvent('WordRecognized',"sintoma","wordRecognized")
            tts_recognition_service.pause(False)
            time.sleep(10)
            tts_recognition_service.unsubscribe("sintoma")
            sintoma=memory_service.getData("WordRecognized")
            sintomas.append(str(sintoma))
            

        elif sintoma_vo[0]=='dificultad' or sintoma_vo[0]=='respirar':
            tts_recognition_service.pause(True)
            tts_service.say("Te mencionare otros posibles sintomas: opresion en el pecho,dolor de pecho, congestion en el pecho, falta de aliento, latidos rapidos")
            vocabulary=['opresion en el pecho','dolor de pecho', 'congestion en el pecho', 'falta de aliento', 'latidos rapidos']
            tts_recognition_service.setVocabulary(vocabulary,False)
            tts_recognition_service.subcribe("sintoma")
            memory_service.subscribeToEvent('WordRecognized',"sintoma","wordRecognized")
            tts_recognition_service.pause(False)
            time.sleep(10)
            tts_recognition_service.unsubscribe("sintoma")
            sintoma=memory_service.getData("WordRecognized")
            sintomas.append(str(sintoma))
            

        elif sintoma_vo[0]=='dolores':
            tts_recognition_service.pause(True)
            tts_service.say("Te mencionare otros posibles sintomas: dolor de cabeza,dolor de pecho, dolor de garganta, dolor de espalda baja")
            vocabulary=['dolor de cabeza','dolor de pecho', 'dolor de garganta', 'dolor de espalda baja']
            tts_recognition_service.setVocabulary(vocabulary,False)
            tts_recognition_service.subcribe("sintoma")
            memory_service.subscribeToEvent('WordRecognized',"sintoma","wordRecognized")
            tts_recognition_service.pause(False)
            time.sleep(10)
            tts_recognition_service.unsubscribe("sintoma")
            sintoma=memory_service.getData("WordRecognized")
            sintomas.append(str(sintoma))
                        
        else:
            pass

    #End While

 #!------------------------------------------------------------------------------------   
    # Go to rest position


if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--ip", type=str, default="127.0.0.1",
                        help="Robot IP address. On robot or Local Naoqi: use '127.0.0.1'.")
    parser.add_argument("--port", type=int, default=9559,
                        help="Naoqi port number")

    args = parser.parse_args()
    session = qi.Session()
    try:
        print("tcp://" + args.ip + ":" + str(args.port))
        session.connect("tcp://" + args.ip + ":" + str(args.port))
    except RuntimeError:
        print ("Can't connect to Naoqi at ip \"" + args.ip + "\" on port " + str(args.port) +".\n"
               "Please check your script arguments. Run with -h option for help.")
        sys.exit(1)
    main(session)
