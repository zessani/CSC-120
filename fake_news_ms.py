import string
import csv
import sys


class Word:
    def __init__(self, word):
        self._word = word
        self._count = 1

    def word(self):   
        return self._word

    def count(self):
        return self._count

    def incr(self):
        self._count += 1

    def __lt__(self, other):
        return (self.count() > other.count()) or \
               (self.count() == other.count() and \
                self.word() < other.word())

    def __str__(self):
        return self._word + " " + str(self._count)

def count_word(word, mylist):
    boolean = False
    for index in mylist:
        if index.word() == word:
            index.incr()
            boolean = True
    if not boolean:
        new = Word(word)
        mylist.append(new)

def merge(L1, L2):
    if not L1:
        return L2
    if not L2:
        return L1

    if L1[0] < L2[0]:
        return [L1[0]] + merge(L1[1:], L2)
    else:
        return [L2[0]] + merge(L1, L2[1:])

def msort(L):
    if len(L) <= 1:
        return L

    point = len(L) // 2
    L1 = L[:point]
    L2 = L[point:]
    return merge(msort(L1), msort(L2))

def main():
    sys.setrecursionlimit(4000)
    filename = input('File: ')
    data = int(input('N: '))

    file = csv.reader(open(filename))
    mylist = []

    for line in file:
        if '#' not in line[0]:
            title = line[4].lower()
            for element in string.punctuation:
                if element in title:
                    title = title.replace(element, " ")
            for word in title.split():
                if len(word) > 2:
                    count_word(word, mylist)

    sorted_list = msort(mylist)

    if data >= len(sorted_list):
        data = len(sorted_list) - 1

    for i in range(min(data + 1, len(sorted_list))):
        print("{} : {}".format(sorted_list[i].word(), sorted_list[i].count()))

main()
