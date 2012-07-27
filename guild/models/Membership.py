from guild.lib.db import db
from datetime import datetime
from dateutil.parser import parse
from collections import OrderedDict
from uuid import uuid4
from flask import request, current_app
import Member, Organisation

class Membership(db.Model):
    __tablename__ = 'memberships'

    member_id = db.Column(db.Integer, db.ForeignKey('members.id', ondelete='CASCADE'), nullable=False, primary_key=True)
    organisation_id = db.Column(db.Integer, db.ForeignKey('organisations.id', ondelete='CASCADE'), nullable=False, primary_key=True,)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id', ondelete='CASCADE'), nullable=False)

    #All relationships created through backrefs
    #member
    #organisation
    #role
    
    createdAt = db.Column(db.DateTime)
    updatedAt = db.Column(db.DateTime)

    def __init__(self, user_id, organisation_id, position_id):
        self.user_id = int(user_id)
        self.organisation_id = int(organisation_id)
        self.position_id = int(position_id)

    def serialize(self):
        return OrderedDict([
            ('user_id' , self.member_id),
            ('organisation_id', self.organisation_id),
            ('position_id' , self.role_id)
        ])