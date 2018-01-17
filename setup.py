from app import db
from app.models import Question, Answer, User

# Create all db tables 
db.create_all()

# Create two basic users 
admin = User(username='admin', email='admin@example.com')
guest = User(username='guest', email='guest@example.com')
db.session.add(admin)
db.session.add(guest)
db.session.commit()

# Seed poll questions
q1a1 = Answer(body='1')
q1a2 = Answer(body='2')
q1a3 = Answer(body='3')
q1a4 = Answer(body='4')
q1a5 = Answer(body='5')
q1 = Question(
    body='How many companies Elon Musk manages?',
    answers=[q1a1, q1a2, q1a3, q1a4, q1a5], 
    correct_answer=q1a3,
)
db.session.add(q1)



# See the data

    # (0, , 2),
    # (1, 'In what year Tesla Roadster came to market?', 6),
    # (2, 'What is Tesla Model S P100D 0-60mph record?', 12)
