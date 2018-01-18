from marshmallow import Schema, fields

from app.models import Question
from app import ma

class QuestionSchema(ma.ModelSchema):
    """A Question recieved by the API"""
    class Meta(object):
        strict = True
        model = Question


class AnswerOutputSchema(Schema):
    """A Question return by the API"""
    body = fields.Str(required=True)

    class Meta(object):
        strict = True


class QuestionOutputSchema(Schema):
    """A Question returned by the API"""
    body = fields.Str(required=True)
    answers = fields.Nested(AnswerOutputSchema, many=True, required=True)
    id = fields.Integer(required=True)

    class Meta(object):
        strict = True
