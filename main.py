from flask import Flask 
from helpers.docker_helper import list_containers , list_volumes , list_images
import logging

logging.basicConfig(level=logging.INFO)

app = Flask(__name__) 
print(__name__)
log_template = '------------------------- {} ----------------------------------'
@app.route('/')
def home_page():
    return 'Docker based web application\n'


@app.route('/list/<string:name>',methods=['GET'])
def list_objects(name):
    
    logging.info(log_template.format('Listing {}'.format(name)) + '\n')
    response = ''
    
    if name == 'images':
        list_of_obj = list_images()
        for obj in list_of_obj:
            response += '{}------------{}\n'.format(obj.short_id,obj.tags)

    elif name == 'volumes':
        list_of_obj = list_volumes()
        for obj in list_of_obj:
            response += '{}\n'.format(obj.short_id)

    elif name == 'containers':
        list_of_obj = list_containers()
        for obj in list_of_obj:
            response += '{} ----> {}\n'.format(obj.short_id,obj.name)

    else:
        return 'No resource named {}'.format(name)

    if response:
        return response
    else:
        return 'No {} created yet'.format(name)

@app.errorhandler(404):
def error():
    return 'Check the api'

app.run(host='0.0.0.0',port=5000)