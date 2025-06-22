from flask_restx import Namespace, Resource, fields
from flask import request
from app.database import db
from app.models.subject_data import SubjectData

api = Namespace('subject_data', description='Subject Data upload')

data_model = api.model('SubjectData', {
    'subject_name': fields.String(required=True),
    'data': fields.String(required=True),
    'user_id': fields.Integer(required=True),
    'site_id': fields.Integer(required=True),
})

@api.route('/')
class SubjectDataUpload(Resource):
    @api.expect(data_model)
    def post(self):
        data = request.get_json()
        sd = SubjectData(
            subject_name=data['subject_name'],
            data=data['data'],
            user_id=data['user_id'],
            site_id=data['site_id'],
        )
        db.session.add(sd)
        db.session.commit()
        return {'message': 'Data uploaded', 'id': sd.id}, 201

@api.route('/site/<int:site_id>')
class SiteSubjectData(Resource):
    def get(self, site_id):
        data = SubjectData.query.filter_by(site_id=site_id).all()

        if not data:
            return {"message": "No subject data found for this site."}, 404

        return [
            {
                "id": entry.id,
                "subject_name": entry.subject_name,
                "data": entry.data,
                "timestamp": entry.timestamp.isoformat()
            }
            for entry in data
        ]
