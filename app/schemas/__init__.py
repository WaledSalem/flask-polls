from .question import QuestionSchema, QuestionOutputSchema

question_schema = QuestionSchema()
questions_schema = QuestionSchema(many=True)
questions_output_schema = QuestionOutputSchema(many=True)
