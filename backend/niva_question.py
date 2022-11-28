import json


def get_answer_about_niva(question, question_answerer):
    context = ""
    with open('../context/niva_context.json', 'r') as niva_context_json:
    # with open('context/niva_context.json', 'r') as niva_context_json:
        context_list = json.load(niva_context_json)["niva_context"]
        for con in context_list:
            context += con

    res = question_answerer({
        'question': question,
        'context': context
    })

    return res["answer"]
