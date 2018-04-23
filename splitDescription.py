import csv
from gensim.models import Word2Vec

csv_file = csv.reader(open('/home/risan/Desktop/train.csv'))
wf = open('/home/risan/Desktop/text', 'a')
for line in csv_file:
    wf.write(line[1])
    wf.write(' ')
    wf.write(line[2])
    wf.write(' ')
wf.close()