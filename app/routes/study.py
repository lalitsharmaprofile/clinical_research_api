from flask_restx import Namespace, Resource, fields
from flask import request
from app.database import db
from app.models.study import Study

api = Namespace('studies', description='Study operations')

study_model = api.model('Study', {
    'name': fields.String(required=True),
})

@api.route('/')
class StudyList(Resource):
    @api.expect(study_model)
    def post(self):
        data = request.get_json()
        study = Study(name=data['name'])
        db.session.add(study)
        db.session.commit()
        return {'message': 'Study created', 'id': study.id}, 201
