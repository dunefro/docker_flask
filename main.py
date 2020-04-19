from flask import Flask 

app = Flask(__name__) 
print(__name__)
@app.route('/')
def home_page():
    return 'Docker based web application'

app.run()