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
`GET http:localhost:8000/api/graphs/age_groups?`

#### Response 

Header: 
    HTTP/1.1 200 OK
    Date: Mon, 23 Mar 2020 17:23:26 GMT
    Status: 200 OK
    Connection: close
    Content-Type: image/png
    Content-Length: 13053

Body: 
![picture](/plot431.png)


```python
import foobar

foobar.pluralize('word') # returns 'words'
foobar.pluralize('goose') # returns 'geese'
foobar.singularize('phenomena') # returns 'phenomenon'
```

## Contributing
Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.

## License
[MIT](https://choosealicense.com/licenses/mit/)