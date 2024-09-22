from functions import *

madlib = get_madlib()
# nouns, verbs, adjectives
counts = get_subject_count(madlib)

for index, count in enumerate(counts):
    if(count != 0):
        madlib = replace_subjects(madlib, count, index)

print(madlib)