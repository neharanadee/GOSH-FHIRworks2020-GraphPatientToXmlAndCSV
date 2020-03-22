from fhir_parser import FHIR, Patient, Observation
from xml.etree import ElementTree as ET
from xml.dom import minidom
import random
from xml.etree.ElementTree import Element, SubElement, Comment

import datetime 

fhir = FHIR('https://localhost:5001/api/', verify_ssl=False) #can import this in multiple pages


def prettify(xmlStr):
    INDENT = "    "
    rough_string = ET.tostring(xmlStr, 'utf-8')
    reparsed = minidom.parseString(rough_string)
    return reparsed.toprettyxml(indent=INDENT)

def getSpecificPatient(uuid): 
    fhir = FHIR()
    patients = fhir.get_all_patients()
    specific_patient = fhir.get_patient(uuid)
    return specific_patient

def checkIfPropertyOrObservation(text): 
    if((text.startswith("__") and text.endswith("__")) or text.startswith("get_")):
        return False
    return True
    
def checkIfPropertyOrObservationOrComponents(text): 
    if((text.startswith("__") and text.endswith("__")) or text.startswith("get_") or text == "components"):
        return False
    return True


def convertObservationToXML(uid): 
    root = Element('patient')
    observationNode = SubElement(root, 'observation')
    observationNode.text = 'This contains observations for patient number ' + str(uid)
    patientObservations = fhir.get_patient_observations(uid)
    counter = 0
    for observation in patientObservations: 
        # for other attributes in an observation
        counter = counter + 1
        specificObservationNode = ET.SubElement(observationNode, "Observation" + str(counter))
        attributes = dir(observation)
        filteredAttributes = filter(checkIfPropertyOrObservationOrComponents, attributes)
        for attribute in filteredAttributes: 
            attributeObject = getattr(observation, attribute)
            if(isinstance(attributeObject,  datetime.date)): 
                 ET.SubElement(specificObservationNode, attribute).text = attributeObject.strftime('%m/%d/%Y')
            else: 
                ET.SubElement(specificObservationNode, attribute).text = attributeObject

        # for components
        
        components = observation.components
        componentCounter = 0
        for component in components: 
            componentCounter = componentCounter + 1
            componentNode = ET.SubElement(specificObservationNode, "Component" + str(counter) + str(componentCounter))
            valueOneNode = ET.SubElement(componentNode, "Value1" ).text = component.display
            ET.SubElement(componentNode, "Value2").text = str(component.value)
            ET.SubElement(componentNode, "Value3").text = component.unit 
            ET.SubElement(componentNode, "Value4").text = str(component.quantity())
            ET.SubElement(componentNode,  "Value5").text = str(component.code)
            ET.SubElement(componentNode,  "Value6").text = component.system
    prettified_xmlStr = prettify(root)
    randomNumber = random.randint(1, 1000)
    output_file = open(str(randomNumber) + ".xml", "w")
    output_file.write(prettified_xmlStr)
    return randomNumber

#maybe? converting csv and making it into a record object. 
def convertToXML(uid): 
    patient = getSpecificPatient(uid)
    attributes = dir(patient)
    filteredAttributes = filter(checkIfPropertyOrObservation, attributes)
    
    root = ET.Element("patient")
    properties = ET.SubElement(root, "properties")
    for attribute in filteredAttributes: 
        #attribute = telecom
        attributeObject = getattr(patient, attribute)
        if(attribute == "identifiers" or attribute == "extensions"): 
            attributeNode = ET.SubElement(properties, attribute)
            # attributeobject is a dictionary
            for i in range(len(attributeObject)): 
                print(str(attributeObject[i]))
                ET.SubElement(attributeNode, attribute, name = "Identifier: " + str(i+1)).text = str(attributeObject[i])

        elif(isinstance(attributeObject, list)): 
            attributeNode = ET.SubElement(properties, attribute)
            listOfAttributeObj = attributeObject
            for i in range(len(listOfAttributeObj)): 
                #this loop has to be done for all the atributes for subobjects
                listOfSubObj = dir(listOfAttributeObj[i])
                listOfSubObj = filter(checkIfPropertyOrObservation, listOfSubObj)
                for subObj in listOfSubObj: 
                    if(subObj != "extensions"): 
                        ET.SubElement(attributeNode, subObj, name = str(i)).text = str(getattr(listOfAttributeObj[i],subObj))

        elif(isinstance(attributeObject,  (int, bool, float, str))): 
            ET.SubElement(properties, attribute).text = attributeObject
        elif(isinstance(attributeObject,  datetime.date)): 
             ET.SubElement(properties, attribute).text = attributeObject.strftime('%m/%d/%Y')
        else: 
          
            currObj = attributeObject
            listOfObj = dir(attributeObject)
            filteredObj =  list(filter(checkIfPropertyOrObservation, listOfObj))
            if(len(filteredObj) != 0):
                attributeNode = ET.SubElement(properties, attribute)
                for subObj in filteredObj: 
                    ET.SubElement(attributeNode, subObj).text = str(getattr(currObj,subObj))
    #addObservation(root, uid)  
    #tree = ET.ElementTree(root)
    prettified_xmlStr = prettify(root)
    randomNumber = random.randint(1, 1000)
    output_file = open(str(randomNumber) + ".xml", "w")
    output_file.write(prettified_xmlStr)
    return randomNumber
    #tree.write("output.xml")

#convertObservationToXML('d9eb4cf6-2894-4627-b912-bbdca07b0401')
