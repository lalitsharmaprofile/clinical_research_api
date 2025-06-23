from flask_restx import Api

from .study import api as study_ns
from .site import api as site_ns
from .user import api as user_ns
from .subject_data import api as subject_data_ns
from .auth import api as auth_api

api = Api(
    title='Clinical Research API',
    version='1.0',
    description='API for studies, sites, users, and subject_data',
    doc='/swagger'
)

api.add_namespace(study_ns, path='/studies')
api.add_namespace(site_ns, path='/sites')
api.add_namespace(user_ns, path='/users')
api.add_namespace(subject_data_ns, path='/subject-data')
api.add_namespace(auth_api, path='/auth')
