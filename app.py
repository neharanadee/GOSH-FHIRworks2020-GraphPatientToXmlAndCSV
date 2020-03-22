from flask import Flask, jsonify, send_file, request, render_template
from graph import *
from XML import *
from CSV import *
import io
import os 

app = Flask(__name__)

@app.route('/')
def hello():
    return render_template('index.html')

#Graphs
@app.route('/api/graph/age_groups', methods=['GET'])
def get_graph_by_age_groups(): 
    imageNumber = graph_by_age_groups()
    fileName = 'plot'+str(imageNumber) + '.png'
    return_data = delete_file(fileName)
    return send_file(return_data, mimetype='image/png')

@app.route('/api/graph/marital_status', methods=['GET'])
def get_graph_by_marital_status(): 
    imageNumber = graph_marital_status()
    fileName = 'plot'+str(imageNumber) + '.png'
    return_data = delete_file(fileName)
    return send_file(return_data, mimetype='image/png')


@app.route('/api/graph/languages_spoken', methods=['GET'])
def get_graph_languages_spoken(): 
    imageNumber = graph_languages_spoken()
    fileName = 'plot'+str(imageNumber) + '.png'
    return_data = delete_file(fileName)
    return send_file(return_data, mimetype='image/png')

# XML
@app.route('/api/xml/observations/', methods=['GET'])
def get_xml_for_patient_observations(): 
    patientID = request.args.get('patientID')
    imageNumber = convertObservationToXML(patientID)
    fileName = str(imageNumber) + '.xml'
    return_data = delete_file(fileName)
    return send_file(return_data, mimetype='text/xml')

@app.route('/api/xml/properties/', methods=['GET'])
def get_xml_for_patient_properties(): 
    patientID = request.args.get('patientID')
    imageNumber = convertToXML(patientID)
    fileName = str(imageNumber) + '.xml'
    return_data = delete_file(fileName)
    return send_file(return_data, mimetype='text/xml')

# CSV 
@app.route('/api/csv/properties/', methods=['GET'])
def get_csv_for_patient_properties(): 
    patientID = request.args.get('patientID')
    imageNumber = convertPatientToCSV(patientID)
    fileName = str(imageNumber) + '.csv'
    return_data = delete_file(fileName)
    return send_file(return_data, mimetype='text/csv', as_attachment=True, attachment_filename="result.csv")


def delete_file(fileName): 
    return_data = io.BytesIO()
    with open(fileName, 'rb') as fo:
        return_data.write(fo.read())
    # (after writing, cursor will be at last byte, so move it to start)
    return_data.seek(0)
    os.remove(fileName)
    return return_data

if __name__ == '__main__':
    app.run(host='localhost',port=8000, debug=True,  use_reloader=False)
