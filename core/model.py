from transformers import pipeline
question_answerer = pipeline('question-answering')
res = question_answerer({
    'question': 'What is the gender of NIVA ?',
    'context': 'NIVA is an intelligent virtual assistant in the form of software that will respond to  users’ '
               'requests with an innovative, non-default, gender-neutral and anti-discriminative response. '
})
print(res['answer'])