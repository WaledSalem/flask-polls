from flask import jsonify
from flask_restful import Resource
from webargs.flaskparser import use_kwargs

from app.models import Question, Answer
from app.schemas import question_input_schema, questions_output_schema
from app import db


class Questions(Resource):
    """Handles all batch requests about the Question entitiy """

    def get(self):
        """Get all questions"""
        questions = Question.query.limit(10).all()
        result = questions_output_schema.dump(questions)
        return jsonify({ 'questions': result.data })
        

    @use_kwargs(question_input_schema)
    def post(self, body, answers):
        """
        Create a new question
        """
        correct_answer = None

        def make_answer(ans):
            result = Answer(body=ans['body'])
            if ans['is_correct']:
                correct_answer = result
            return result

        mapped_answers = [make_answer(ans) for ans in answers]
        question = Question(
            body=body,
            answers=mapped_answers,
            correct_answer=correct_answer
        )
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
