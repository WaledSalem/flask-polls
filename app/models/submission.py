from app import db

class Submission(db.Model):
    __tablename__ = 'submission'
    id = db.Column(db.Integer, primary_key=True)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    answer_id = db.Column(db.Integer, db.ForeignKey('answer.id'))
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'))

    user = db.relationship('User', lazy=True)
    answer = db.relationship('Answer', lazy=True)
    question = db.relationship('Question', lazy=True)

    def __repr__(self):
        return '<Submission %r...>' % self.body[:8]
