from marshmallow import Schema, fields

class AnswerInputSchema(Schema):
    """An Answer returned by the API"""
    is_correct = fields.Bool(required=True)
    body = fields.Str(required=True)

    class Meta(object):
        strict = True
