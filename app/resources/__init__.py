from .questions import Questions
from .question import Question
from .. import api

api.add_resource(Questions, '/questions', methods=['post', 'get'])
api.add_resource(Question, '/question/<int:id>', methods=['get', 'delete', 'put'])
