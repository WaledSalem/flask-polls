from app import db 

class Question(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(1000), nullable=False)
    correct_answer = db.relationship('Answer', lazy=True, uselist=False)
    answers = db.relationship('Answer', lazy=True)

    def __repr__(self):
        return '<Question %r...>' % self.body[:8]
