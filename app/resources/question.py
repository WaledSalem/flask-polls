from flask import jsonify, abort
from flask_restful import Resource
from webargs.flaskparser import use_kwargs, use_args

from app import models
from app.schemas import question_input_schema, question_output_schema
from app import db

class Question(Resource):
    """Handle single questions"""

    def get(self, id):
        """Get a single question"""
        question = models.Question.query.get(id)
        if question is None:
            abort(404)
        result = question_output_schema.dump(question)
        return jsonify({ 'question': result.data })
    

    def delete(self, id):
        """Delete a single question"""
        question = models.Question.query.get(id)
        if question is None:
            abort(404)
        db.session.delete(question)
        db.session.commit()
        return 'OK', 204
    
    # TODO: use Marshmallow for most of the logic here and questions#post
    @use_args(question_input_schema)
    def put(self, id, question):
        """Update a single question"""
        return 'TODO'
