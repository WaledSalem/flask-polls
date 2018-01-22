from flask_restful import Resource
from webargs.flaskparser import use_kwargs, use_args

from app import models
from app.schemas import question_schema
from app import db

class Question(Resource):
    """Handle single questions"""

    def get(self, id):
        """Get a single question"""
        question = models.Question.query.get_or_404(id)
        result = question_schema.dump(question)
        return {'question': result.data}, 200

    def delete(self, id):
        """Delete a single question"""
        question = models.Question.query.get_or_404(id)
        db.session.delete(question)
        db.session.commit()
        return 'OK', 200
    
    @use_args(question_schema)
    def put(self, id, question):
        """Update a single question"""
        question = models.Question.query.get_or_404(id)
        db.session.delete(question)
        db.session.commit()
        return 'OK', 204
