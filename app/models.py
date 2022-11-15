from django.db import models
from random import randint




QUESTIONS = [
    {
        'id': question_id,
        'title': f"Question {question_id} header",
        'text': f"Question {question_id} text",
        'answers_count': question_id % 4,
        'like_count' : randint(1, 100),
        'tags': [f"tag{i}" for i in range(question_id)],

    } for question_id in range(30)
]


ANSWERS = [
    {
        question['id']: [{
            'id': answer_id,
            'text': f"Answer{answer_id} text",
            'like_count': randint(1, 100)
        } for answer_id in range(30)]

    }for question in QUESTIONS
]

