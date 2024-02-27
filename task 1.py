sentence = input().split()
count_word = {}
for i in range(len(sentence)):
    count_word[sentence.count(sentence[i])] = sentence[i]
for m in range(len(count_word)):
    print(count_word[max(count_word)])
    del count_word[max(count_word)]
