import json
from transformers import pipeline


def get_answer_about_niva(question):
    question_answerer = pipeline('question-answering')
    with open('context/niva_context.json', 'r') as niva_context_json:
        context = json.load(niva_context_json)["niva_context"]

    res = question_answerer({
        'question': question,
        'context': context

    })

    return res["answer"]
