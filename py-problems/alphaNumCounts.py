def sentence(sentence):
    numCount = 0
    alphaCount = 0
    alphaNumCount = 0
    sentence = sentence.split(' ')
    print(sentence)
    for word in sentence:
        print(word, type(word))
        if word.isnumeric():
            numCount += 1
        elif word.isalpha():
            alphaCount += 1
        elif word.isalnum():
            alphaNumCount += 1
    return [numCount, alphaNumCount, alphaCount]

print(sentence("OK 12 7 1A A1 B2C3 Hello Aha A80"))