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

# @app.route('/list/containers',methods=['GET'])
# def list_docker_containers():

#     logging.info(log_template.format('Listing Containers') + '\n')
#     list_of_containers = list_containers()
#     response = ''
#     for container in list_of_containers:
#         response += '{} ----> {}\n'.format(container.short_id,container.name)
#     if response:
#         return response
#     else:
#         return 'No containers created yet'

# @app.route('/list/volumes',methods=['GET'])
# def list_docker_volumes():
#     list_of_volumes = list_volumes()
#     response = ''
#     for volume in list_of_volumes:
#         response += '{}\n'.format(volume.short_id)
#     if response:
#         return response
#     else:
#         return 'No Volumes created yet'

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
        for volume in list_of_obj:
            response += '{}\n'.format(obj.short_id)

    elif name == 'containers':
        list_of_obj = list_containers()
        for container in list_of_obj:
            response += '{} ----> {}\n'.format(obj.short_id,obj.name)

    else:
        return 'No resource named {}'.format(name)

    if response:
        return response
    else:
        return 'No {} created yet'.format(name)

app.run(host='0.0.0.0',port=5000)