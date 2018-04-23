import csv

from train import Word2Vec

w2v = Word2Vec('test2.model')
csv_file = csv.reader(open('/home/risan/Desktop/train.csv'))

f = 0
t = 0
threshold = 0.6
for line in csv_file:
    wordList1 = line[1].split()
    wordList2 = line[2].split()
    simlarity = w2v.sentence_similarity(wordList1, wordList2)
    print("s1|s2: " + str(simlarity), end='')
    if round(simlarity, 5) >= threshold:
        print(' TRUE ', end='')
    else:
        print('False ', end='')
    print(' ' + line[5])
    if round(simlarity, 5) >= threshold and line[5] == 'TRUE':
        t += 1
    elif round(simlarity, 5) >= threshold and line[5] == 'FALSE':
        f += 1
    elif round(simlarity, 5) < threshold and line[5] == 'TRUE':
        f += 1
    else:
        t += 1

print('true number = ' + str(t))
print('false number = ' + str(f))
print('正确率:' + str(t/(t+f)))

