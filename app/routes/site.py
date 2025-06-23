from flask_restx import Namespace, Resource, fields
from flask import request
from app.database import db
from app.models.site import Site
from app.models.user import User
from flask_jwt_extended import jwt_required, get_jwt

api = Namespace('sites', description='Site operations')

site_model = api.model('Site', {
    'name': fields.String(required=True),
    'study_id': fields.Integer(required=True),
})

@api.route('/')
class SiteList(Resource):
    @api.expect(site_model)
    @jwt_required()
    def post(self):
        data = request.get_json()
        
        claims = get_jwt()
        role = claims.get('role')
        if role != 'admin':
            return {"message": "Admins only"}, 403

        site = Site(name=data['name'], study_id=data['study_id'])
        db.session.add(site)
        db.session.commit()
        return {'message': 'Site created', 'id': site.id}, 201

    def get(self):
        sites = Site.query.all()
        return [
            {
                "id": site.id,
                "name": site.name,
                "study_id": site.study_id
            }
            for site in sites
        ]


@api.route('/<int:site_id>/subjects')
class SiteSubjects(Resource):
    def get(self, site_id):
        subjects = User.query.filter_by(site_id=site_id, role='subject').all()
        if not subjects:
            return {"message": "No subjects found for this site."}, 404
        return [
            {
                "id": s.id,
                "name": s.name,
                "role": s.role
            }
            for s in subjects
        ]