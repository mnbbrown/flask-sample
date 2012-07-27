from flask import Blueprint, request, jsonify, abort, render_template, make_response, current_app, Response
from guild.models import Organisation
import json

organisations = Blueprint('organisations', __name__, url_prefix="/organisations")

def jsonResponse(data, status_code=None, headers=None):
	resp = make_response(json.dumps(data, indent=4))
	resp.status_code = status_code if status_code is not None else 200
	if status_code is not None: resp.headers = headers
	resp.mimetype = 'application/json'
	return resp

from functools import wraps
def checkKey(apiKey):
	return True

def authenticate(f):
	@wraps(f)
	def decorator(*args, **kwargs):
		if not request.authorization or not checkKey(request.authorization.username):
			return jsonResponse({'error': 'Authorization Required'}, 401, {'WWW-Authenticate': 'Basic realm'})
		return f(*args, **kwargs)
	return decorator

@organisations.route('/', methods=['GET'])
@authenticate
def getOrganisations():	
	organisations = Organisation.query.all()
	organisations = [ organisation.serialize() for organisation in organisations ]
	return jsonResponse(organisations)

@organisations.route('/<id>', methods=['GET'])
def getOrganisation(id):
	organisation = Organisation.query.get_or_404(id).serialize()
	return jsonResponse(organisation)