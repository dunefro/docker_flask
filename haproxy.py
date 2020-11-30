from flask import Flask 
# from helpers.docker_helper import list_containers , list_volumes , list_images
import logging
import os

logging.basicConfig(level=logging.INFO)

app = Flask(__name__)

port = os.getenv('PORT_NO')

@app.route('/')
def home_page():
    return 'Docker based web application: Port is ----> {}'.format(port)

@app.route('/admin')
def admin():
    return 'Admin page: Port is -----> {}'.format(port)

@app.route('/list/<string:name>')
def check_app_page(name):

    return '{} page: Port is -------> {}'.format(name , port)


app.run(host='0.0.0.0',port=5000)