from app.database import db
from werkzeug.security import generate_password_hash, check_password_hash

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    role = db.Column(db.String, nullable=False)  # we will use 'admin' or 'subject'
    site_id = db.Column(db.Integer, db.ForeignKey('site.id'), nullable=True)
    password_hash = db.Column(db.String(128), nullable=False)
    username = db.Column(db.String(12), unique=True, nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)
    
