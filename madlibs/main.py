from functions import *

madlib = get_madlib()
subjects = get_subjects(madlib)
madlib = replace_subjects(madlib, subjects)

print(madlib)