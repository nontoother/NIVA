from text_similarity import get_question_list, calculate_similarity, get_stored_answer
from niva_question import get_answer_about_niva
from general_question import get_general_question_answer


# 1.stored QA pair
# 2.question about Niva
# 3.normal question
def answer(question):
    # get question from speech_text_conversion
    stored_question_list = get_question_list()
    similarity = calculate_similarity(question, stored_question_list)
    niva_key_word = ["you", "your", "NIVA", "niva"]
    if max(similarity) > 0.3:
        return get_stored_answer(similarity)
    elif any(word in question.split() for word in niva_key_word):
        return get_answer_about_niva(question)
    else:
        return get_general_question_answer(question)


def main():
    questions = ["what is your gender?", "what is your sex?", "what does niva stands for?", "where is the capital of "
                                                                                            "China?"]
    for question in questions:
        res = answer(question)
        print(question, res)


if __name__ == "__main__":
    main()
