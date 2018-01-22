from flask_restful import Resource
from webargs import fields, validate
from webargs.flaskparser import use_kwargs, use_args

from app import models
from app.schemas import submission_schema, submissions_schema, answer_schema, user_schema, question_schema
from app import db


class Submissions(Resource):
    """Handle survery submissions"""

    @use_kwargs({'limit': fields.Integer(missing=100, locations=('query',), validate=validate.Range(min=1, max=100))})
    def get(self, limit):
        """Get user submissions"""
        # no auth system yet. getting all submission
        submissions = models.Submission.query.limit(limit).all()
        data, error = submissions_schema.dump(submissions)
        if error:
            return 'Error', 400
        return { 'submissions': data }

    @use_kwargs({
        'question_id': fields.Integer(required=True, locations=('json',)),
        'answer': fields.String(required=True, locations=('json',)),
    })
    def post(self, question_id, answer):
        "Submit an answer to a question"
        question = models.Question.query.get_or_404(question_id)
        user = models.User.query.get(1) # no auth system yet

        found_answer = None 
        for question_answer in question.answers:
            if question_answer.body == answer:
                found_answer = question_answer
        if found_answer is None:
            return 'Invalid answer', 400

        submission = models.Submission(question=question, answer=found_answer, user=user)
        db.session.add(submission)
        db.session.commit()

        return 'OK', 204

