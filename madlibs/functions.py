import os
import random

def get_madlib():
    num = random.randint(1,5)
    path = "madlibs\\madlib" + str(num) + ".txt"

    file = open(path)
    madlib = file.readline()
    file.close()

    return madlib

def get_subject_count(madlib):
    # nouns, verbs, adjectibes
    counts = []

    counts.append(madlib.count("NOUN"))
    counts.append(madlib.count("VERB"))
    counts.append(madlib.count("ADJECTIVE"))

    return counts

def replace_subjects(madlib, sub_count, index):
    # get subject
    if index==0:
        subject = "NOUN"
    elif index==1:
        subject = "VERB"
    else:
        subject = "ADJECTIVE"

    while(sub_count != 0):
        word = input(f"Enter a {subject.lower()}: ")
        madlib = madlib.replace(subject, word, 1)
        sub_count -= 1
        os.system("cls")

    return madlib