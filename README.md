# GraphPatientToXmlAndCSV

GraphPatientToXmlAndCSV is an API that takes FHIR Records and converts them to XML and XSV for every valid patient. It also generates few graphs on patient data. 

## Installation
1. Clone the project into a folder. 
2. Ensure you have python and pip downloaded  (https://www.python.org/downloads/)
3. Ensure you have FHIRWorks API or use (https://github.com/greenfrogs/FHIRworks_2020) to install FHIRworks api
4. Use pip to install matplotlib 3.2.1
```bash
pip install matplotlib
```
5. Use the package manager pip to install flask 1.1.1.
```bash
pip install flask
```
6. Use the package manager pip to install Fhir-parser 0.1.5.
```bash
pip install FHIR-Parser
```
7. Use the package manager pip to install requests 2.23.0. 
```bash
pip install requests
```

## Run the app 
1. Run the FHIRWorks API in one terminal
```bash
dotnet run
```
2. Run the app.py in another terminal simultaneously 
```bash
python app.py
```

## Usage
Three possible Get Requests; xml, graph, csv. 

### XML

#### Request 
This gets all the observations of a patient with a given patient ID in a XML format. 
For example,for patient ID 'd9eb4cf6-2894-4627-b912-bbdca07b0401', the get request is

`GET /api/xml/observations/?patientID=d9eb4cf6-2894-4627-b912-bbdca07b0401`

#### Response 

Header: 
    HTTP/1.1 200 OK,
    Date: Mon, 23 Mar 2020 05:53:05 GMT
    Status: 200 OK,
    Content-Type: text/xml,
    Content-Length: 64077


```xml 

<?xml version="1.0" ?>
<patient>
    <observation>
        This contains observations for patient number d9eb4cf6-2894-4627-b912-bbdca07b0401
        <Observation1>
            <effective_datetime>01/09/2011</effective_datetime>
            <encounter_uuid>5591633b-1e91-4029-818a-366631ccb952</encounter_uuid>
            <issued_datetime>01/09/2011</issued_datetime>
            <patient_uuid>d9eb4cf6-2894-4627-b912-bbdca07b0401</patient_uuid>
            <status>final</status>
            <type>vital-signs</type>
            <uuid>541b3ad4-b3f1-4750-87d4-ef38b370ef0d</uuid>
            <Component11>
                <Value1>Body Mass Index</Value1>
                <Value2>29.67</Value2>
                <Value3>kg/m2</Value3>
                <Value4>29.67kg/m2</Value4>
                <Value5>39156-5</Value5>
                <Value6>http://loinc.org</Value6>
            </Component11>
        </Observation1>
        <?other observations from 1 to 75.................... ?>
        <Observation75>
            <effective_datetime>11/10/2019</effective_datetime>
            <encounter_uuid>b216caef-e88b-4837-abf8-904f7c02ef0a</encounter_uuid>
            <issued_datetime>11/10/2019</issued_datetime>
            <patient_uuid>d9eb4cf6-2894-4627-b912-bbdca07b0401</patient_uuid>
            <status>final</status>
            <type>survey</type>
            <uuid>7b4b3677-b24a-4df3-a5fc-860ccd92055b</uuid>
            <Component751>
                <Value1>Tobacco smoking status NHIS</Value1>
                <Value2>None</Value2>
                <Value3/>
                <Value4>N/A</Value4>
                <Value5>72166-2</Value5>
                <Value6>http://loinc.org</Value6>
            </Component751>
        </Observation75>
    </observation>
</patient>
```
#### Request 
This gets all the properties of a patient with a given patient ID in a XML format. 
For example, for patient ID 'd9eb4cf6-2894-4627-b912-bbdca07b0401', the get request is 

`GET /api/xml/properties/?patientID=d9eb4cf6-2894-4627-b912-bbdca07b0401`

#### Response 

Header: 
    HTTP/1.1 200 OK,
    Date: Mon, 23 Mar 2020 05:57:16 GMT
    Status: 200 OK,
    Content-Type: text/xml,
    Content-Length: 2840

```xml
<?xml version="1.0" ?>
<patient>
    <properties>
        <addresses>
            <city name="0">Blackstone</city>
            <country name="0">US</country>
            <full_address name="0">358 Oberbrunner Approach Apt 4Blackstone, Massachusetts, US</full_address>
            <latitude name="0">42.05283200979602</latitude>
            <lines name="0">['358 Oberbrunner Approach Apt 4']</lines>
            <longitude name="0">-71.52523247435127</longitude>
            <postal_code name="0"/>
            <state name="0">Massachusetts</state>
        </addresses>
        <birth_date>10/21/1973</birth_date>
        <communications>
            <codes>['en-US']</codes>
            <communication>[('en-US', 'English')]</communication>
            <languages>['English']</languages>
        </communications>
        <extensions>
            <extensions name="Identifier: 1">us-core-race: White</extensions>
            <extensions name="Identifier: 2">us-core-ethnicity: Not Hispanic or Latino</extensions>
            <extensions name="Identifier: 3">patient-mothersMaidenName: Jeremy766 Gleichner915</extensions>
            <extensions name="Identifier: 4">us-core-birthsex: M</extensions>
            <extensions name="Identifier: 5">patient-birthPlace: Sharon, Massachusetts, US</extensions>
            <extensions name="Identifier: 6">disability-adjusted-life-years: 0.016479540110564225</extensions>
            <extensions name="Identifier: 7">quality-adjusted-life-years: 45.983520459889434</extensions>
        </extensions>
        <gender>male</gender>
        <identifiers>
            <identifiers name="Identifier: 1"> d9eb4cf6-2894-4627-b912-bbdca07b0401</identifiers>
            <identifiers name="Identifier: 2">Medical Record Number d9eb4cf6-2894-4627-b912-bbdca07b0401</identifiers>
            <identifiers name="Identifier: 3">Social Security Number 999-67-4686</identifiers>
            <identifiers name="Identifier: 4">Driver's License S99910651</identifiers>
            <identifiers name="Identifier: 5">Passport Number X34975298X</identifiers>
        </identifiers>
        <marital_status>
            <marital_status>M</marital_status>
        </marital_status>
        <multiple_birth/>
        <name>
            <family>Weissnat378</family>
            <full_name>Mr. Abram53 Weissnat378</full_name>
            <given>Abram53</given>
            <given_list>['Abram53']</given_list>
            <prefix>Mr.</prefix>
            <prefix_list>['Mr.']</prefix_list>
        </name>
        <telecoms>
            <number name="0">555-560-7469</number>
            <system name="0">phone</system>
            <use name="0">home</use>
        </telecoms>
        <uuid>d9eb4cf6-2894-4627-b912-bbdca07b0401</uuid>
    </properties>
</patient>

```
### Graphs 

#### Request 
This creates a graph based on patient age groups of all patients, according to patient properties data. 

`GET /api/graph/age_groups?`

#### Response 

Header: 
    HTTP/1.1 200 OK,
    Date: Mon, 23 Mar 2020 17:23:26 GMT,
    Status: 200 OK,
    Content-Type: image/png,
    Content-Length: 13053

Body: 
![picture](/plot431.png)

#### Request 
This creates a graph based on marital status of all patients, according to patient properties data. 

`GET /api/graph/marital_status?`

#### Response 

Header: 
    HTTP/1.1 200 OK,
    Date: Mon, 23 Mar 2020 05:39:46 GMT,
    Status: 200 OK,
    Content-Type: image/png,
    Content-Length: 10676

Body: 
![picture](/plot561.png)

#### Request 
This creates a graph based on languages spoken by all patients, according to patient properties data. 

`GET /api/graph/languages_spoken?`

#### Response 

Header: 
    HTTP/1.1 200 OK,
    Date: Mon, 23 Mar 2020 05:44:20 GMT
    Status: 200 OK,
    Content-Type: image/png,
    Content-Length: 17696
    
Body: 
![picture](/plot572.png)


### CSV 

#### Request 
This gets all the properties of a patient with a given patient ID in a CSV format. 
For example, for patient ID 'd9eb4cf6-2894-4627-b912-bbdca07b0401', the get request is 

`GET /api/csv/properties/?patientID=d9eb4cf6-2894-4627-b912-bbdca07b0401`

#### Response    
Header: 
    HTTP/1.1 200 OK,
    Date: Mon, 23 Mar 2020 06:18:00 GMT
    Status: 200 OK,
    Content-Type: text/xml,
    Content-Length: 1210
    Content-Disposition:attachment; filename=result.csv

```csv
city,country,full_address,latitude,lines,longitude,postal_code,state,birth_date,codes,communication,languages,extensions0,extensions1,extensions2,extensions3,extensions4,extensions5,extensions6,gender,identifiers0,identifiers1,identifiers2,identifiers3,identifiers4,marital_status,multiple_birth,family,full_name,given,given_list,prefix,prefix_list,number,system,use,uuid,Blackstone,US,"358 Oberbrunner Approach Apt 4 Blackstone, Massachusetts
, US",42.05283200979602,['358 Oberbrunner Approach Apt 4'],-71.52523247435127,,Massachusetts,10/21/1973,['en-US'],"[('en-US', 'English')]",['English'],us-core-race: White,us-core-ethnicity: Not Hispanic or Latino,patient-mothersMaidenName: Jeremy766 Gleichner915,us-core-birthsex: M,"patient-birthPlace: Sharon, Massachusetts, US",disability-adjusted-life-years: 0.016479540110564225,quality-adjusted-life-years: 45.983520459889434,male, d9eb4cf6-2894-4627-b912-bbdca07b0401,Medical Record Number d9eb4cf6-2894-4627-b912-bbdca07b0401,Social Security Number 999-67-4686,Driver's License S99910651,Passport Number X34975298X,M,False,Weissnat378,Mr. Abram53 Weissnat378,Abram53,['Abram53'],Mr.,['Mr.'],555-560-7469,phone,home,d9eb4cf6-2894-4627-b912-bbdca07b0401
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

## License
