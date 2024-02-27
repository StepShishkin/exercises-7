n = int(input())
all_word = []
translate_sentence = ''
for i in range(n):
    word = input().split()
    all_word.append(word)
translate = dict(all_word)
sentence = input().split()
for m in range(len(sentence)):
    if sentence[m] in translate:
        translate_sentence = translate_sentence + ' ' + translate[sentence[m]]
    else:
        translate_sentence = translate_sentence + ' ' + sentence[m]
print(translate_sentence)
