import time

from text_similarity import get_question_list, calculate_similarity, get_stored_answer
from niva_question import get_answer_about_niva
from general_question import get_general_question_answer
from transformers import pipeline

'''
We have three strategies to answer the questions. We divided questions into three types as following: 
1.stored QA pair:
For the stored QA pair part, we use a json file to store some specific question-answer pairs, as the question we provide
may not be exactly the same as what we stored in json, we use TF-IDF to calculate the similarity between the given 
question and stored question. Once the result is greater than 0.3 which is our threshold, we would regard the given 
question as stored one, and randomly return an answer from the stored answer list.

2.question about Niva:
For the question about Niva part, we use a model in hugging face which is called question-answering, the strategy we use
is if we find any word like “you”, “your”, “niva” in the given question, we would regard this question as a question
about niva, then we would use the second way to get a answer. We stored some niva’s basic information in a json file as
niva’s context, and while calling this function, we would provide the stored information as context to the model, the
model would extract corresponding information according to the context and give out an answer.

3.normal question:
As for the last part, we use BERT as our general question answering model. BERT is a model to fill a masked area in a 
sentence. So we need to do is to modify the interrogative sentence into declarative sentence and put [mask] in the 
position where supposed to be answered. Then we can pass the declarative sentence into BERT and get the answer.

'''


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
    # main function is just for testing the model part
    questions = ["what is your gender?", "when is your birthday?", "what does niva stands for?", "what is your name?",
                 "What are you wearing?", "where is the capital of China?", "Do you have a boyfriend?"]
    question_answerer_model = pipeline('question-answering')
    general_question_model = pipeline('fill-mask', model='bert-base-uncased')
    for question in questions:
        res = answer(question, question_answerer_model, general_question_model)
        print(question, res)


if __name__ == "__main__":
    main()
