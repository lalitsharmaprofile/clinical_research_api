from app.database import db
from datetime import datetime

class SubjectData(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    subject_name = db.Column(db.String, nullable=False)
    data = db.Column(db.Text, nullable=False)
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    site_id = db.Column(db.Integer, db.ForeignKey('site.id'), nullable=False)
