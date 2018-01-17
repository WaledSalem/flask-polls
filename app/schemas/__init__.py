from .answer_input import AnswerInputSchema
from .answer_output import AnswerOutputSchema
from .question_input import QuestionInputSchema
from .question_output import QuestionOutputSchema


answer_input_schema = AnswerInputSchema()
question_input_schema = QuestionInputSchema()
questions_output_schema = QuestionOutputSchema(many=True)
