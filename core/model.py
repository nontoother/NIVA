from transformers import pipeline

question_answerer = pipeline('question-answering')
res = question_answerer({
    'question': 'What is your gender?',
    'context': 'NIVA is an intelligent virtual assistant in the form of software that will respond to users’ '
               'requests with an innovative, non-default, gender-neutral and anti-discriminative response. '
})
res2 = question_answerer({
    'question': 'What is your gender?',
    'context': 'NIVA is an intelligent virtual assistant in the form of software that will respond to users’ '
               'requests with an innovative, non-default, gender-neutral and anti-discriminative response. '
               "Nonhuman Intelligent Virtual Assistant(NIVA) is an artificial intelligence program that challenges "
               "capitalistic notions of gender as a result of growing technological monopolies by corporations in "
               "Silicon Valley such as Apple, Google, and Meta. In collaboration with fellow graduate students from "
               "the Master of Software Engineering program, NIVA is a cross-disciplinary project bridging "
               "technological software development and art. By commenting on the critical discourse surrounding "
               "machine learning ethics, queer posthumanism, and artificial intelligence, this project aims to "
               "deconstruct our unconscious biases about gender that are reinforced through the capitalization of "
               "humanistic AI. NIVA is a program that runs on seemingly algorithmic outputs that disrupt the "
               "perception of the “default.” The vocal outputs of this program are created through the random "
               "combination of variables between human or robotic, English or conlang, and masculine or feminine "
               "pitch. Since its creation, NIVA has been committed to challenging the marketing strategies of "
               "profitable tech companies by decentralizing humanity and providing gender inclusivity to artificial "
               "intelligence. "

})

print(res2['answer'])
