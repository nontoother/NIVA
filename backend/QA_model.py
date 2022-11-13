import time

from text_similarity import get_question_list, calculate_similarity, get_stored_answer
from niva_question import get_answer_about_niva
from general_question import get_general_question_answer
from transformers import pipeline


# 1.stored QA pair
# 2.question about Niva
# 3.normal question
def answer(question, question_answer_model, general_question_model):
    # get question from speech_text_conversion
    stored_question_list = get_question_list()
    similarity = calculate_similarity(question, stored_question_list)
    niva_key_word = ["you", "your", "NIVA", "niva"]
    if max(similarity) > 0.6:
        return get_stored_answer(similarity)
    elif any(word in question.split() for word in niva_key_word):
        return get_answer_about_niva(question, question_answer_model)
    else:
        return get_general_question_answer(question, general_question_model)


def main():
    questions = ["what is your gender?", "when is your birthday?", "what does niva stands for?", "what is your name?",
                 "what does niva aims to?", "where is the capital of China?"]
    question_answerer_model = pipeline('question-answering')
    general_question_model = pipeline('fill-mask', model='bert-base-uncased')
    for question in questions:
        res = answer(question, question_answerer_model, general_question_model)
        print(question, res)


if __name__ == "__main__":
    main()
