import nltk

be_list = ['is', 'was', 'am', 'is', 'are', 'was', 'were', 'be']
do_list = ['do', 'does', 'did', 'done', 'doing']

# modify function is used to make interrogative sentences into declarative sentences
def modify(inputStr, answerStr):
    inputStr = inputStr.strip().lower()
    answerStr = str(answerStr).strip().lower()
    if inputStr[-1] == '?':
        inputStr = inputStr[:-1]
    tokens = nltk.word_tokenize(inputStr)
    tagged = nltk.pos_tag(tokens)

    result = ''

    if tagged[0][0] == 'when':
        tagged.pop(0)
        tagged.append(('in', 'IN'))
    elif tagged[0][0] == 'where':
        tagged.pop(0)
        tagged.append(('in', 'IN'))
    elif (tagged[0][0] == 'who') | (tagged[0][0] == 'whom'):
        tagged.pop(0)
        tagged.insert(0, ('[MASK]', 'NN'))
        return ' '.join([t[0] for t in tagged]) + '.'
    elif tagged[0][0] == 'whose':
        tagged.pop(0)
        tagged.insert(0, ('[MASK]\'s', 'NN'))
        return ' '.join([t[0] for t in tagged]) + '.'
    elif tagged[0][0] == 'why':
        tagged.pop(0)
        tagged.append(('because', 'IN'))
        tagged.append(('of', 'IN'))
    elif tagged[0][0] == 'which':
        tagged.pop(0)
    elif tagged[0][0] == 'what':
        tagged.pop(0)
    elif tagged[0][0] == 'how':
        tagged.pop(0)
        tagged.insert(len(tagged), ('by', 'IN'))
    else:
        tagged.append(('[MASK]', 'NN'))
        return

    for index in range(len(tagged)):
        if tagged[index][0] in be_list:
            verb_index = index
            verb_word = tagged[index]
            tagged = tagged[verb_index + 1:]
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


def get_general_question_answer(question, unmasker):
    parsed_question = modify(question, '')
    answer = unmasker(parsed_question)
    return answer[0]['sequence']
