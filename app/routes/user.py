from flask_restx import Namespace, Resource, fields
from flask import request
from app.database import db
from app.models.user import User

api = Namespace('users', description='User operations')

user_model = api.model('User', {
    'name': fields.String(required=True),
    'role': fields.String(required=True),  # we will use 'admin' or 'subject'
    'site_id': fields.Integer(required=False),
})

@api.route('/')
class UserList(Resource):
    @api.expect(user_model)
    def post(self):
        data = request.get_json()
        user = User(name=data['name'], role=data['role'], site_id=data.get('site_id'))
        db.session.add(user)
        db.session.commit()
        return {'message': 'User created', 'id': user.id}, 201
