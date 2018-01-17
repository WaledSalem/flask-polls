from .questions import Questions
from .. import api

api.add_resource(Questions, '/questions')
