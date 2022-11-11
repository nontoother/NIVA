# Use TF-IDF method to find the most similar question
import random

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
import json
import numpy as np


def get_question_list():
    question_list = []
    with open('context/QA_pairs.json', 'r') as qa:
        qa_pairs = json.load(qa)["QAlist"]
        for i, pair in enumerate(qa_pairs):
            question_list.append(pair["question"])
    return question_list


def calculate_similarity(text, question_list):
    # Initialize an instance of tf-idf Vectorizer
    tfidf_vectorizer = TfidfVectorizer()

    # add question to the matrix
    question_list = [text] + question_list

    # Generate the tf-idf vectors for the corpus
    tfidf_matrix = tfidf_vectorizer.fit_transform(question_list)

    # compute and print the cosine similarity matrix
    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
    return cosine_sim[0][1:]


def get_stored_answer(result):
    question_list = get_question_list()
    # result = calculate_similarity(question, question_list)
    # the threshold to answer the question in given QA pairs
    # if max(result) > 0.1:
    most_similar_question = np.argmax(result)
    with open('context/QA_pairs.json', 'r') as qa:
        qa_pairs = json.load(qa)["QAlist"]
        answer_list = qa_pairs[most_similar_question]["answer"]
        return random.choice(answer_list)
    # else:
    #     return None


# res = get_context("What is your sex?")
# res = get_stored_answer("When is your birthday?")
# print(res)
