from fhir_parser import FHIR, Patient, Observation
import csv
from XML import *
import datetime 

fhir = FHIR('https://localhost:5001/api/', verify_ssl=False) #can import this in multiple pages



def convertPatientToCSV(uuid): 
    patient = getSpecificPatient(uuid)
    attributes = dir(patient)
    filteredAttributes = list(filter(checkIfPropertyOrObservation, attributes))
    result = {}
    for attribute in filteredAttributes: 
        attributeObject = getattr(patient, attribute)
        if(attribute == "identifiers" or attribute == "extensions"): 
            
            for i in range(len(attributeObject)): 
                    result[attribute + str(i)] = str(attributeObject[i])
            
        elif(isinstance(attributeObject, list)):      
            # 0 is a hack for now, cuz actually this can be a list of addresses           
            listOfSubObj = dir(attributeObject[0])
            listOfSubObj = filter(checkIfPropertyOrObservation, listOfSubObj)
            dic = {}
            for subObj in listOfSubObj: 
                if(subObj != "extensions"): 
                    result[subObj] = str(getattr(attributeObject[0],subObj))
            
        elif(isinstance(attributeObject,  (int, bool, float, str))): 
            result[attribute] = attributeObject
        elif(isinstance(attributeObject,  datetime.date)): 
            result[attribute] = attributeObject.strftime('%m/%d/%Y')
        else: 
            currObj = attributeObject
            listOfObj = dir(attributeObject)
            filteredObj =  list(filter(checkIfPropertyOrObservation, listOfObj))
            
            if(len(filteredObj) != 0):
                for subObj in filteredObj: 
                    result[subObj] = str(getattr(currObj,subObj))
    
    randomNumber = random.randint(1, 1000)
    with open(str(randomNumber)+'.csv', 'w') as csvfile:
        w = csv.DictWriter(csvfile, result.keys())
        w.writeheader()
        w.writerow(result)
    return randomNumber

#maybe covert one observation to csv 

def convertPatientObservationsToCSV(uid): 
    patientObservations = fhir.get_patient_observations(uid)
    result = {}
    for observation in patientObservations: 
        attributes = dir(observation)
        filteredAttributes = filter(checkIfPropertyOrObservationOrComponents, attributes)
        for attribute in filteredAttributes: 
            attributeObject = getattr(observation, attribute)
            if(isinstance(attributeObject,  datetime.date)): 
                 ET.SubElement(specificObservationNode, attribute).text = attributeObject.strftime('%m/%d/%Y')
            else: 
                ET.SubElement(specificObservationNode, attribute).text = attributeObject

        
        
#convertPatientToCSV('8f789d0b-3145-4cf2-8504-13159edaa747')
