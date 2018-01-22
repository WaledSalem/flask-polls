from marshmallow import Schema, fields, validate
from app.models import Question, Answer
from app import ma

class AnswerSchema(ma.ModelSchema):
    """Answer Schema"""
    class Meta(object):
        strict = True
        model = Answer
        exclude = ['id']

class QuestionSchema(ma.ModelSchema):
    """Question Schema"""
    answers = fields.Nested(AnswerSchema, many=True, validate=[validate.Length(min=2)])
    class Meta(object):
        strict = True
        model = Question
