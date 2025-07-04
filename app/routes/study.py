from flask_restx import Namespace, Resource, fields
from flask import request
from app.database import db
from app.models.study import Study
from app.models.site import Site
from app.models.user import User
from flask_jwt_extended import jwt_required, get_jwt

api = Namespace('studies', description='Study operations')

study_model = api.model('Study', {
    'name': fields.String(required=True),
})

@api.route('/')
class StudyList(Resource):
    @api.expect(study_model)
    @jwt_required()
    def post(self):
        data = request.get_json()

        claims = get_jwt()
        role = claims.get('role')
        if role != 'admin':
            return {"message": "Admins only"}, 403

        study = Study(name=data['name'])
        db.session.add(study)
        db.session.commit()
        return {'message': 'Study created', 'id': study.id}, 201

    def get(self):
        studies = Study.query.all()
        return [
            {
                "id": study.id,
                "name": study.name
            }
            for study in studies
        ]


@api.route('/<int:study_id>/subjects')
class StudySubjects(Resource):
    def get(self, study_id):
        # Get all site IDs that belong to the study
        site_ids = [site.id for site in Site.query.filter_by(study_id=study_id).all()]

        if not site_ids:
            return {"message": "No sites found for this study."}, 404

        # Get all subjects assigned to any of these sites
        subjects = User.query.filter(User.site_id.in_(site_ids), User.role == 'subject').all()

        if not subjects:
            return {"message": "No subjects found for this study."}, 404

        return [
            {
                "id": s.id,
                "name": s.name,
                "role": s.role,
                "site_id": s.site_id
            }
            for s in subjects
        ]
