from app.database import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    role = db.Column(db.String, nullable=False)  # we will use 'admin' or 'subject'
    site_id = db.Column(db.Integer, db.ForeignKey('site.id'), nullable=True)
