import random
from app.models.user import User

def generate_unique_username():
    prefix = "VL"
    while True:
        digits = str(random.randint(1000, 9999))  # 4 digits
        username = prefix + digits
        if not User.query.filter_by(username=username).first():
            return username
