from .question import QuestionSchema, AnswerSchema
from .submission import SubmissionSchema
from .user import UserSchema

user_schema = UserSchema()
answer_schema = AnswerSchema()
question_schema = QuestionSchema()
questions_schema = QuestionSchema(many=True)
submission_schema = SubmissionSchema()
submissions_schema = SubmissionSchema(many=True)
