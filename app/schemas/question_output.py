from marshmallow import Schema, fields

from app.schemas import AnswerOutputSchema

class QuestionOutputSchema(Schema):
    """A Question returned by the API"""
    body = fields.Str(required=True)
    answers = fields.Nested(AnswerOutputSchema, many=True, required=True)
    id = fields.Integer(required=True)

    class Meta(object):
        strict = True
