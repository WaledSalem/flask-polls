from .questions import Questions
from .question import Question
from .submissions import Submissions
from .. import api

api.add_resource(Questions, '/questions', methods=['post', 'get', 'put'])
api.add_resource(Question, '/question/<int:id>', methods=['get', 'delete', 'put'])
api.add_resource(Submissions, '/submissions', methods=['get', 'post'])
