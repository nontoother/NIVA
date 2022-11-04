import nltk
from transformers import pipeline

be_list = ['is', 'was', 'am', 'is', 'are', 'was', 'were', 'be']
do_list = ['do', 'does', 'did', 'done', 'doing']


def modify(inputStr, answerStr):
    inputStr = inputStr.strip().lower()
    #     if(type(answerStr)=='float'):
    answerStr = str(answerStr).strip().lower()
    if inputStr[-1] == '?':
        inputStr = inputStr[:-1]
    tokens = nltk.word_tokenize(inputStr)
    tagged = nltk.pos_tag(tokens)

    result = ''
    token = ''

    # 处理并删除起始疑问词
    if tagged[0][0] == 'when':
        token = 'when'
        tagged.pop(0)
        tagged.append(('in', 'IN'))
    elif tagged[0][0] == 'where':
        token = 'where'
        tagged.pop(0)
        tagged.append(('in', 'IN'))
    elif (tagged[0][0] == 'who') | (tagged[0][0] == 'whom'):
        tagged.pop(0)
        tagged.insert(0, ('[MASK]', 'NN'))
        # who.append([' '.join([t[0] for t in tagged]) + '.', answerStr])
        return ' '.join([t[0] for t in tagged]) + '.'
    elif tagged[0][0] == 'whose':
        tagged.pop(0)
        tagged.insert(0, ('[MASK]\'s', 'NN'))
        # whose.append([' '.join([t[0] for t in tagged]) + '.', answerStr])
        return ' '.join([t[0] for t in tagged]) + '.'
    elif tagged[0][0] == 'why':
        token = 'why'
        tagged.pop(0)
        tagged.append(('because', 'IN'))
        tagged.append(('of', 'IN'))
    elif tagged[0][0] == 'which':
        token = 'which'
        tagged.pop(0)
    elif tagged[0][0] == 'what':
        token = 'what'
        tagged.pop(0)
    elif tagged[0][0] == 'how':
        token = 'how'
        tagged.pop(0)
        tagged.insert(len(tagged), ('by', 'IN'))
    else:
        tagged.append(('[MASK]', 'NN'))
        result = ' '.join([t[0] for t in tagged]) + '.'
        # others.append([result, answerStr])
        return

    for index in range(len(tagged)):
        if tagged[index][0] in be_list:
            verb_index = index
            verb_word = tagged[index]
            tagged = tagged[verb_index + 1:]
            # 判断最后是不是介词
            if (len(tagged) >= 1) & (tagged[len(tagged) - 1][1] not in ['IN', 'TO']):
                tagged.append(verb_word)
            tagged.append(('[MASK]', 'NN'))
            result = ' '.join([t[0] for t in tagged]) + '.'
            break
        if (tagged[index][0] in do_list) | (tagged[index][1] == 'MD'):
            verb_index = index
            tagged = tagged[verb_index + 1:]
            tagged.append(('[MASK]', 'NN'))
            result = ' '.join([t[0] for t in tagged]) + '.'
            break

    if len(result) == 0:
        tagged.append(('[MASK]', 'NN'))
        result = ' '.join([t[0] for t in tagged]) + '.'

    return result


#
# question_one = 'how can I survive?'
# question_two = 'What is the goal of life?'
# question_three = 'where is the capital of China?'
#
# original_question_list = [question_one, question_two, question_three]
# answer_list = []
# for question in original_question_list:
#     parsed_question = modify(question, '')
#     answer_list.append(answer)
#     print(question, answer[0]['sequence'])


def get_general_question_answer(question):
    unmasker = pipeline('fill-mask', model='bert-base-uncased')
    parsed_question = modify(question, '')
    answer = unmasker(parsed_question)
    return answer[0]['sequence']
