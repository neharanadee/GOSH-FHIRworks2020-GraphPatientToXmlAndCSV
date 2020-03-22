# GraphPatientToXmlAndCSV

GraphPatientToXmlAndCSV is an API that takes FHIR Records and converts them to XML and XSV for every valid patient. It also generates few graphs on patient data. 

## Installation
1. Clone the project into a folder. 
2. Ensure you have python and pip downloaded  (https://www.python.org/downloads/)
3. Enssure you haev FHIR works api and use [github](https://github.com/greenfrogs/FHIRworks_2020) to install FHIRworks api
3. Use the package manager [pip](https://pypi.org/project/matplotlib/) to install matplotlib.
4. Use the package manager [pip](https://pypi.org/project/Flask/) to install flask.
5. Use the package manager [pip](https://pypi.org/project/FHIR-Parser/) to install Fhir-parser.
6. Use the package manager [pip](https://pypi.org/project/requests/) to install requests.

```bash
pip install foobar
```

## Usage

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