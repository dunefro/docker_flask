from flask import Flask 
from helpers.docker_helper import list_containers
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

app.run()