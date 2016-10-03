import string
import csv

class ReservedWords:

    def __init__(self):
        pass

    def validate(self,text):
        file = open('reserved_words.csv','r')
        words = []
        row =	csv.reader(file, delimiter=' ')
        for word in row:
            words.append(word)
        file.close()

        for line in text:
            tmp = line.lower()
            for w in words:
                if tmp.find(w[0]) > -1:
                    uno = line[tmp.find(w[0]):tmp.find(w[0])+len(w[0])]
                    dos = w[0]
                    if uno != dos:
                        print 'Error de sintaxis 004: palabra {}'.format(uno)
                        print line
                        exit()
                    