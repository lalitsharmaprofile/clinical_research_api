from flask_restx import Namespace, Resource, fields
from flask_jwt_extended import create_access_token
from app.models.user import User

api = Namespace('auth', description='Authentication')

login_model = api.model('Login', {
    'username': fields.String(required=True),
    'password': fields.String(required=True)
})

@api.route('/login')
class Login(Resource):
    @api.expect(login_model)
    def post(self):
        data = api.payload
        username = data.get("username")
        password = data.get("password")

        user = User.query.filter_by(username=username).first()
        if not user or not user.check_password(password):
            return {"message": "Invalid username or password"}, 401

        access_token = create_access_token(
            identity=str(user.id),  # JWT subject
            additional_claims={"role": user.role}
        )
        return {"access_token": access_token}
