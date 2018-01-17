USE poll;

INSERT INTO questions
    (id, question, currect_answer_id)
VALUES
    (0, 'How many companies Elon Musk manages?', 2),
    (1, 'In what year Tesla Roadster came to market?', 6),
    (2, 'What is Tesla Model S P100D 0-60mph record?', 12)
;


INSERT INTO answers 
    (id, question_id, answer)
VALUES
    (0, 0, '1'),
    (1, 0, '2'),
    (2, 0, '3'),
    (3, 0, '4'),
    (4, 0, '5'),
    (5, 1, '2000'),
    (6, 1, '2008'),
    (7, 1, '2010'),
    (8, 1, '2009'),
    (9, 2, '3.80 seconds'),
    (10, 2, '3.12 seconds'),
    (11, 2, '2.82 seconds'),
    (12, 2, '2.28 seconds')
;
