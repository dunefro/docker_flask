from flask import Flask 
from helpers.docker_helper import list_containers , list_volumes
app = Flask(__name__) 
print(__name__)

@app.route('/')
def home_page():
    return 'Docker based web application'

@app.route('/list/containers',methods=['GET'])
def list_docker_containers():

    list_of_containers = list_containers()
    response = ''
    for container in list_of_containers:
        response += '{} ----> {}\n'.format(container.short_id,container.name)
    return response

@app.route('/list/volumes',methods=['GET'])
def list_docker_volumes():
    list_of_volumes = list_volumes()
    response = ''
    for volume in list_of_volumes:
        response += '{}'.format(volume.short_id)
    if response:
        return response
    else:
        return ' No Volumes created yet'

app.run(host='0.0.0.0',port=5000)