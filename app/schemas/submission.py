from marshmallow import Schema, fields, validate
from app.models import Question, Answer, User, Submission
from .question import QuestionSchema, AnswerSchema
from .user import UserSchema
from app import ma

class SubmissionSchema(ma.ModelSchema):
    """Submission Schema"""
    question = fields.Nested(QuestionSchema, exclude=('id', 'answers'))
    answer = fields.Nested(AnswerSchema)
    user = fields.Nested(UserSchema, exclude=('email','id'))

    class Meta(object):
        strict = True
        model = Submission
        exclude=['id']
