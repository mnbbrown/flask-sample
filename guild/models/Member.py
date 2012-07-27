from datetime import datetime
from dateutil.parser import parse
from collections import OrderedDict
from uuid import uuid4
from flask import request, current_app

from guild.lib.db import db
from sqlalchemy.orm.collections import attribute_mapped_collection
from sqlalchemy.ext.associationproxy import association_proxy

import Membership
from utils import serializeObjs

class Member(db.Model):
    __tablename__ = 'members'
    
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(80))
    lastname = db.Column(db.String(80))
    studentNo = db.Column(db.Integer)
    email = db.Column(db.String(80))
    phone = db.Column(db.Integer)
    token =db.Column(db.String(40))
    confirmed = db.Column(db.Boolean)

    _rel_membership = db.relationship('Membership', primaryjoin='Member.id==Membership.member_id', collection_class=attribute_mapped_collection('organisation'), cascade='all,delete-orphan', backref='member')
    organisations = association_proxy('_rel_membership', 'role', creator=(lambda org, role: Membership(organisation=org, role=role)))

    def __init__(self, firstname, lastname, studentNo, email, phone, confirmed):
        self.firstname = firstname
        self.lastname = lastname
        self.studentNo = int(studentNo)
        self.email = email
        self.phone = int(phone)
        self.confirmed = bool(confirmed)
        self.token = self.genNewToken()

    def genNewToken(self):
        return uuid4()

    def confirmEmail(self, token):
        if(token == self.token):
            self.confirmed = True
            self.token = self.genNewToken()
        db.session.commit()
        return self.confirmed

    def serialize(self, recurse=True):
        return OrderedDict([
            ('id' , self.id),
            ('studentNo', self.studentNo),
            ('firstName' , self.firstname),
            ('lastName' , self.lastname),
            ('email' , self.email),
            ('phone' , self.phone),
            ('confirmed', self.confirmed),
            ('organisations', serializeObjs(self.organisations) if recurse is not False else len(self.organisations))
        ])