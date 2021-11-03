
   
import requests
from flask import Flask, jsonify, request

app = Flask(__name__)

osrm_url = '10.154.0.2:80'


@app.route('/', methods=['GET', 'POST'])
def index():
	if request.method == 'POST':               # user posts info, which can be sent to model/database/whatever
		some_json = request.get_json()           # takes whatever the user sent in the API query ...
		full_query_text = osrm_url + some_json['main_string']
		result = os.popen("curl '" + full_query_text + "'").read()
		return jsonify({'result': result})   # ... and showing it back to them, with a response code of 201
	else:
		return jsonify({'hello': 'no success re OSRM :('})


# '/table/v1/driving/' + latlong_first_string + ';' + latlong_destination_string + ';' + latlong_text_for_query
