from flask import jsonify
from flask_restful import Resource
from webargs import fields, validate
from webargs.flaskparser import use_kwargs, use_args

from app.models import Question, Answer
from app.schemas import question_schema, questions_schema
from app import db


class Questions(Resource):
    """Handles all batch requests about the Question entitiy as well as creating a new Question"""

    @use_kwargs({'limit': fields.Integer(missing=10, locations=('query',), validate=validate.Range(min=1, max=100))})
    def get(self, limit):
        """Get all questions"""
        questions = Question.query.limit(limit).all()
        result = questions_schema.dump(questions)
        return jsonify({ 'questions': result.data })
        
    @use_args(question_schema)
    def post(self, question):
        """Create a new question"""
        db.session.add(question)
        db.session.commit()

        return 'OK', 201

    @use_kwargs({'ids': fields.Integer(many=True, locations=('json',))})
    def delete(self, ids):
        """Delete a list of questions"""
        questions = []
        # First make sure all questions can be found
        for id in ids:
            questions.append(Question.query.get_or_404(id=id))
        # Delete all of questions
        for question in questions:
            db.session.delete(question)
        db.session.commit()

        return 'OK', 200

    @use_args(questions_schema)
    def put(self, questions):
        """Update a list of questions"""
        # First make sure all questions can be found
        for question in questions:
            Question.query.get_or_404(id=question.id)
        db.session.commit()

        return 'OK', 204
