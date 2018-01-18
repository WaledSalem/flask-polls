from marshmallow import Schema, fields

from app.models import Question, Answer
from app import ma

class AnswerSchema(ma.ModelSchema):
    """Answer Schema"""
    class Meta(object):
        strict = True
        model = Answer

class QuestionSchema(ma.ModelSchema):
    """A Question recieved by the API"""
    correct_answer = fields.Nested(AnswerSchema, load_only=True)
    answers = fields.Nested(AnswerSchema, many=True, exclude=('id'))
    class Meta(object):
        strict = True
        model = Question
