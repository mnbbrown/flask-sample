from flask import Blueprint, request, jsonify, abort, render_template, make_response, current_app
from guild.models import Member
from guild.lib.cache import redis
import json

members = Blueprint('members', __name__, url_prefix="/members")

def jsonResponse(data):
	resp = make_response(json.dumps(data, indent=4))
	resp.status_code = 200
	resp.mimetype = 'application/json'
	return resp

@members.route('', methods=['GET'])
@members.route('/', methods=['GET'])
def getMembers():
	members = Member.query.all()
	members = [ member.serialize() for member in members ]
	return jsonResponse(members)

@members.route('/<id>', methods=['GET'])
def getMember(id):
	member = Member.query.get_or_404(id).serialize()
	return jsonResponse(member)