from flask import jsonify
from flask_restful import Resource
from webargs import fields, validate
from webargs.flaskparser import use_kwargs, use_args

from app.models import Question, Answer
from app.schemas import question_schema, questions_schema, questions_output_schema
from app import db


class Questions(Resource):
    """Handles all batch requests about the Question entitiy as well as creating a new Question"""

    @use_kwargs({'limit': fields.Integer(missing=10, validate=validate.Range(min=1, max=100))})
    def get(self, limit):
        """Get all questions"""
        questions = Question.query.limit(limit).all()
        result = questions_output_schema.dump(questions)
        return jsonify({ 'questions': result.data })
        
    @use_args(question_schema)
    def post(self, question):
        """Create a new question"""
        db.session.add(question)
        db.session.commit()

        return 'OK', 201

    def delete(self):
        """Delete a list of questions"""
        return 'TODO'

    # @use_kwargs()
    def put(self):
        """Update a list of questions"""
        return 'TODO'
