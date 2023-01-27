sentence="way a is there will a is there where"
def reverse_sentence(sentence):
    sentence=sentence.split(' ')
    sentence.reverse()
    return ' '.join(sentence)

print(reverse_sentence(sentence))

