from app import db 

class Question(db.Model):
    __tablename__ = 'question'
    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.String(1000), nullable=False)
    answers = db.relationship('Answer', lazy=True)

    def __repr__(self):
        return '<Question %r...>' % self.body[:8]
