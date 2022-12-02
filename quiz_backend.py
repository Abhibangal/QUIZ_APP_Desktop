import json


def get_all_questions():
    with open('quiz_question.json', 'r') as qr:
        data = qr.read()

        return json.loads(data)

