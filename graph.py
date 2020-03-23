from fhir_parser import FHIR, Patient, Observation
import matplotlib
import matplotlib.pyplot as plt
matplotlib.use('Agg')
import os
import random
from datetime import date
from requests.exceptions import ConnectionError

fhir = FHIR('https://localhost:5001/api/', verify_ssl=False) #can import this in multiple pages


def graph_marital_status(): 
    fhir = FHIR()
    patients = fhir.get_all_patients()

    marital_status = {}
    for patient in patients:
        if str(patient.marital_status) in marital_status:
            marital_status[str(patient.marital_status)] += 1
        else:
            marital_status[str(patient.marital_status)] = 1


    plt.bar(range(len(marital_status)), list(marital_status.values()), align='center')
    plt.xticks(range(len(marital_status)), list(marital_status.keys()))
    fig1 = plt.gcf()
    plt.draw()
    number = random.randint(1, 1000)
    fig1.savefig('plot'+str(number)+'.png', dpi=100)
    return number

def graph_languages_spoken(): 
    fhir = FHIR()
    patients = fhir.get_all_patients()

    languages = {}
    for patient in patients:
        for language in patient.communications.languages:
            languages.update({language: languages.get(language, 0) + 1})


    plt.bar(range(len(languages)), list(languages.values()), align='center')
    plt.xticks(range(len(languages)), list(languages.keys()), rotation='vertical')
    fig1 = plt.gcf()
    plt.draw()
    number = random.randint(1, 1000)
    fig1.savefig('plot'+str(number)+'.png', dpi=100)
    return number

def calculate_age(born):
    today = date.today()
    return today.year - born.year - ((today.month, today.day) < (born.month, born.day))

def graph_by_age_groups(): 
    fhir = FHIR()
    patients = fhir.get_all_patients()

    ageGroups = {'<10': 0, '10-20': 0, '20-30':0, '30-40':0, '40-50':0, '50-60':0, '60-70': 0, '70-80':0, '80-90':0, '90+':0}
    for patient in patients:
        birth = patient.birth_date
        patientAge  = calculate_age(birth)
        if(patientAge < 10): 
            ageGroups['<10'] += 1
        elif( 10 <= patientAge < 20): 
             ageGroups['10-20'] += 1
        elif( 20 <=patientAge < 30): 
             ageGroups['20-30'] += 1
        elif( 30 <=patientAge < 40): 
             ageGroups['30-40'] += 1
        elif( 40 <=patientAge< 50): 
             ageGroups['40-50'] += 1
        elif( 50 <=patientAge < 60): 
             ageGroups['50-60'] += 1
        elif( 60 <patientAge < 70 ): 
             ageGroups['60-70'] += 1
        elif( 70 <patientAge < 80 ): 
             ageGroups['70-80'] += 1
        elif( 80 <patientAge < 90 ): 
            ageGroups['80-90'] += 1
        elif( 90 <=patientAge ): 
            ageGroups['90+'] += 1
        

    plt.bar(range(len(ageGroups)), list(ageGroups.values()), align='center')
    plt.xticks(range(len(ageGroups)), list(ageGroups.keys()),  rotation='vertical')
    fig1 = plt.gcf()
    plt.draw()
    number = random.randint(1, 1000)
    fig1.savefig('plot'+str(number)+'.png', dpi=100)
    return number
    

    # fig = plt.figure()
    # fig.savefig('plot.png')
    #plt.show()

    #something
def graph_by_states(): 
    fhir = FHIR()
    patients = fhir.get_all_patients()

    states = {}
    for patient in patients:
        for addressArr in patient.addresses:     
            states.update({addressArr.state: states.get(addressArr.state, 0) + 1})


    plt.bar(range(len(states)), list(states.values()), align='center')
    plt.xticks(range(len(states)), list(states.keys()), rotation='vertical')
    plt.show()
    
def graph_by_countries(): 
    fhir = FHIR()
    patients = fhir.get_all_patients()

    countries = {}
    for patient in patients:
        for addressArr in patient.addresses:     
            countries.update({addressArr.country: countries.get(addressArr.country, 0) + 1})


    plt.bar(range(len(countries)), list(countries.values()), align='center')
    plt.xticks(range(len(countries)), list(countries.keys()), rotation='vertical')
    plt.show()

def graph_by_cities(): 
    fhir = FHIR()
    patients = fhir.get_all_patients()

    cities = {}
    for patient in patients:
        for addressArr in patient.addresses:     
            cities.update({addressArr.city: cities.get(addressArr.city, 0) + 1})


    plt.bar(range(len(cities)), list(cities.values()), align='center')
    plt.xticks(range(len(cities)), list(cities.keys()), rotation='vertical')
    # fig = plt.figure()
    # fig.savefig('plot.png')
    plt.show()
    

# need to think of what can we graph from the observation data
# def graph_by_diseases():  
#     fhir = FHIR()
#     patients = fhir.get_all_patients()
#     problems = {}
#     count = 0
#     for patient in patients: 
#         count = count + 1
#         if count == 4: 
#             break
#         print("YOOOO THIS IS THR FKING ID" + patient.uuid)
#         try:
#              observations = fhir.get_patient_observations(patient.uuid)
#         except:
#             continue
#         for observation in observations: 
#             print("observation 1")
#             components = observation.components
#             for component in components: 
#                 print(component.display)
#                 print(component.value)
    #             problems.update({component.display: problems.get(component.display, 0) + 1})
    # plt.bar(range(len(problems)), list(problems.values()), align = 'center')
    # plt.xticks(range(len(problems)),list(problems.keys()), rotation = 'vertical' )
    # plt.show(); 

   
# def graph_by_diseases(): 
# def graph_by_certain_age(age): 