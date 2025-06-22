from app.database import db

class Site(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    study_id = db.Column(db.Integer, db.ForeignKey('study.id'), nullable=False)
    users = db.relationship('User', backref='site', lazy=True)
