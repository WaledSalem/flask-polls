from marshmallow import Schema, fields, validates_schema, ValidationError, validate

from app.schemas import AnswerInputSchema

class QuestionInputSchema(Schema):
    """A Question recieved by the API"""
    body = fields.Str(required=True)
    answers = fields.Nested(
        AnswerInputSchema,
        many=True,
        required=True,
        validate=validate.Length(min=2)
    )

    @validates_schema(pass_many=True)
    def validate_answers(self, question, many):
        answers = question['answers']
        has_not_seen_correct_answer = True
        for answer in answers:
            if answer['is_correct']:
                if has_not_seen_correct_answer:
                    has_not_seen_correct_answer = False
                else:
                    raise ValidationError('A question can not have multiple correct answers')

    class Meta(object):
        strict = True
