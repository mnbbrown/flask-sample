from flask import Blueprint, request, jsonify, abort, render_template, make_response
from guild.models import Member
from sqlalchemy import and_
import json

register = Blueprint('register', __name__, url_prefix="/")

def jsonResponse(data):
	resp = make_response(json.dumps(data, indent=4))
	resp.status_code = 200
	resp.mimetype = 'application/json'
	return resp

@register.route('register', methods=['POST'])
def registerUser():	
	return "Success"

@register.route('confirmEmail', methods=['POST'])
def confirmUserEmail():
	member = Member.query.filter( (Member.email == request.json['email']) & (Member.token == request.json['token']) ).first_or_404()
	conf = member.confirmEmail(dec['token'])
	return jsonResponse(member.serialize())
