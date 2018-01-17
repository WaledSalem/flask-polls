from marshmallow import Schema, fields

class AnswerOutputSchema(Schema):
    """A Question return by the API"""
    body = fields.Str(required=True)

    class Meta(object):
        strict = True
