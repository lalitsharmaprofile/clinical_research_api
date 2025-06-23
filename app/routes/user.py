from flask_restx import Namespace, Resource, fields
from flask import request
from app.database import db
from app.models.user import User
from app.utils.helpers import generate_unique_username

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
        data = api.payload
        username = generate_unique_username()

        user = User(
            name=data['name'],
            role=data['role'],
            site_id=data.get('site_id'),
            username=username
        )
        user.set_password(data['password'])
        db.session.add(user)
        db.session.commit()

        return {
            "message": "User created",
            "username": user.username
        }, 201

    def get(self):
        users = User.query.all()
        return [
            {
                "id": user.id,
                "name": user.name,
                "role": user.role,
                "site_id": user.site_id
            }
            for user in users
        ]
