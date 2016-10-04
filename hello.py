from flask import Flask
from flask import render_template
from flask import request
from algorithm import *

import yaml


app = Flask(__name__)

import logging
logging.basicConfig(filename='example.log',level=logging.DEBUG)

@app.route('/')
def hello_world():
    return 'Hello, World!'


@app.route('/compute', methods=['GET', 'POST'])
def compute():
	if request.method == 'GET':
		    return render_template('compute.html', result=0)
	else:
		input1 = request.form['input1']
		app.logger.debug(input1)
        

       

        yamlInput1 = yaml.safe_load(input1)
        app.logger.debug(yamlInput1)
        print 'yamlInput1: ' + str(yamlInput1)
        

        result = sum(yamlInput1)
        print result
        return render_template('compute.html', result=result)

if __name__ == "__main__":
	app.run()
