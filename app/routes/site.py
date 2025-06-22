from flask_restx import Namespace, Resource, fields
from flask import request
from app.database import db
from app.models.site import Site

api = Namespace('sites', description='Site operations')

site_model = api.model('Site', {
    'name': fields.String(required=True),
    'study_id': fields.Integer(required=True),
})

@api.route('/')
class SiteList(Resource):
    @api.expect(site_model)
    def post(self):
        data = request.get_json()
        site = Site(name=data['name'], study_id=data['study_id'])
        db.session.add(site)
        db.session.commit()
        return {'message': 'Site created', 'id': site.id}, 201
