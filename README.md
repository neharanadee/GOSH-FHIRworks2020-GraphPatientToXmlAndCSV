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
Run the app.py file
```bash
python app.py
```

## Usage
Three possible Get Requests. 

### Graphs 

#### Request 
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

### XML

#### Request 
`GET /api/xml/observations/?patientID=d9eb4cf6-2894-4627-b912-bbdca07b0401`

#### Response 

Header: 
    HTTP/1.1 200 OK,
    Date: Mon, 23 Mar 2020 05:53:05 GMT
    Status: 200 OK,
    Content-Type: text/xml,
    Content-Length: 64077

Body: 
![xml](/906.xml)

#### Request 
`GET /api/xml/properties/?patientID=d9eb4cf6-2894-4627-b912-bbdca07b0401`

#### Response 

Header: 
    HTTP/1.1 200 OK,
    Date: Mon, 23 Mar 2020 05:57:16 GMT
    Status: 200 OK,
    Content-Type: text/xml,
    Content-Length: 2840

Body: 
![xml](/847.xml)



## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)